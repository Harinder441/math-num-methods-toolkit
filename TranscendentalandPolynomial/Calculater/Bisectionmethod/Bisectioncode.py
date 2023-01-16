from sympy import *

x = symbols("x")


def trunc(n, d):  # defining a function for truncuation
    s = 10 ** d
    k = int(n * s)
    return k / s


def nsub(x):
    normal = "0123456789+-=()"
    sub_s = "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


class Bisec:
    def __init__(self, f, d, a=None, b=None):
        self.f = simplify(f)
        self.d = d
        self.a = a
        self.b = b
        self.rlist = []
        self.boollist = []

    def getroot(self):
        self.inf = None
        f = self.f
        d = self.d
        p = None
        q = None
        if (self.a != None and self.b != None):
            st = self.a
            en = self.b
        else:
            st = -10
            en = 10
        for i in range(st, en + 1):  # finding interval
            if "I" in str(N(f.subs(x, i))):
                return "image"
            if ((N(f.subs(x, i)) == zoo) or (N(f.subs(x, i)) == oo)):
                return "infinity"
            if ((N(f.subs(x, i)) > 0 and N(f.subs(x, i + 1)) < 0) or (N(f.subs(x, i)) < 0 and N(f.subs(x, i + 1)) > 0)):
                p = i
                q = i + 1
                break
            elif N(f.subs(x, i)) == 0:
                if (N(f.subs(x, i - 0.1)) * N(f.subs(x, i + 0.1)) < 0):
                    p = i - 0.1
                    q = i + 0.1
                    break
        if (p == None):
            return "tryagain"
        if (N(f.subs(x, p)) > 0):
            p, q = q, p
        self.a = p
        self.b = q
        rootlist = []
        bolist = []
        i = 1
        while i <= 100:  # iterations
            t = (p + q) / 2
            tr = trunc(t, self.d + 2)
            rootlist.append(tr)
            if (N(f.subs(x, tr)) > 0):
                q = tr
                bolist.append(1)
            elif (N(f.subs(x, tr)) < 0):
                p = tr
                bolist.append(0)
            pr = trunc(p, d)
            qr = trunc(q, d)
            if (pr == qr):
                self.itr = i - 1
                self.boollist = bolist
                self.rlist = rootlist
                return pr
            i = i + 1
        self.boollist = bolist
        self.rlist = rootlist
        self.inf = "not"
        return "notfound"

    def getiter(self):
        return self.itr

    def showiter(self):
        rl = self.rlist
        bl = self.boollist
        if rl == []:
            return "empty"
        if self.inf == "not":
            itrl = 25
        else:
            itrl = len(rl) - 1
        file = open("../../showiteration", 'w')
        file.write("Function =" + str(self.f) + "\n")
        p = self.a
        q = self.b
        file.write("Interval choosen is [" + str(p) + "," + str(q) + "]\n")
        j = 0
        for i in range(itrl):
            file.write("\n")
            file.write("$ Iteration  " + str(i + 1) + " $\n")
            file.write("        x" + str(i + 1) + " = " + "(" + str(p) + " + " + str(q) + ")" +"/" + "2  =  " + str(rl[i + 1]))
            if (bl[i + 1] == 0):
                k = 60
                rpl = p
                p = rl[i + 1]

            else:
                k = 62
                rpl = q
                q = rl[i + 1]
            file.write(" , f(x" + str(i + 1) + ")" + chr(k) + "0 which implies x" +
                str(i + 1) + " will replace " + str(rpl) + "\n")
            file.write("     Therefore,new interval is [" + str(p) + ", " + str(q) + "]\n")
            j = i
        if self.inf == "not":
            file.write("Root not found after 25 iterations.Click Table format to view more iterations. \n")
        else:
            file.write("Both ends of interval in " + str(j + 1) + "th iteration are equal upto " + str(
                self.d) + " decimal places \n")
            rt = trunc(p, self.d)
            file.write("Hence " + str(rt) + " is correct root upto " + str(self.d) + " decimal places \n")
        file.close()

    def showiter2(self):
        rl = self.rlist
        bl = self.boollist
        if not rl:
            return "empty"
        file = open(
            "../../showiterationtb",
            'w')
        file.write("Function =" + str(self.f) + "\n")
        p = self.a
        q = self.b
        file.write("Interval chosen is [" + str(p) + "," + str(q) + "]\n")
        if self.inf == 'not':
            file.write("Root not found after 100 iterations.\n")
        file.write(
            "----------------------------------------------------ITERATION TABLE---------------------------------------------------\n")
        file.write("\n")
        file.write("       Iteration                                 Approximation     \n")
        file.write("--------------------------------------------------------------------------------------\n")
        j = 0
        for i in range(len(rl) - 1):
            if (bl[i + 1] == 0):
                rpl = p
                p = rl[i + 1]

            else:
                rpl = q
                q = rl[i + 1]
            file.write(
                "          " + str(i + 1) + "                                            [" + str(p) + ", " + str(
                    q) + "]\n")
            file.write("---------------------------------------------------------------------------------------\n")
            j = i
        if self.inf != 'not':
            file.write("\nBoth ends of interval in " + str(j + 1) + "th iteration are equal upto " + str(
                self.d) + " decimal places \n")
            rt = trunc(p, self.d)
            file.write("Hence " + str(rt) + " is correct root unto " + str(self.d) + " decimal places \n")
        file.close()


if __name__ == "__main__":
    f = "x**4-x-10"
    d = 1
    a = 0
    c = 10
    b = Bisec(f, d, a, c)
    r = b.getroot()
    b.showiter()
    print(r)
