from sympy import *
x=symbols("x")
def trunc(n,d):  #  defining a function for truncuation
    s=10**d
    k=int(n*s)
    return k/s
def nsub(x):
    normal = "0123456789+-=()"
    sub_s = "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)
class Secant:
    def __init__(self,f,d,a=None,b=None):
        self.f=simplify(f)
        self.d=d
        self.a=a
        self.b=b
        self.rlist=[]
        self.boollist=[]
        self.ylist=[]
        self.xlist=[]
    def getroot(self):
        self.inf=None
        f=self.f
        d=self.d
        p=None
        q=None
        st=self.a
        en=self.b
        for i in range(st,en+1):# finding interval
            if  "I" in str(N(f.subs(x,i))):
                return "image"
            if((N(f.subs(x,i))==zoo)or(N(f.subs(x,i))==oo)):
                return "infinity"
            if((N(f.subs(x,i))>0 and N(f.subs(x,i+1))<0) or (N(f.subs(x,i))<0 and N(f.subs(x,i+1))>0)):
                p=i
                q=i+1
                break
            elif N(f.subs(x,i))==0:
                if(N(f.subs(x,i-0.1))*N(f.subs(x,i+0.1))<0):
                    p=i-0.1
                    q=i+0.1
                    break
        if(p==None):
            return "tryagain"
        self.a=p
        self.b=q
        rootlist=[]
        ylist=[]
        bolist= []
        xlist=[p,q]
        i=1
        x0,x1=p,q
        while(i<=20):
           if x1-x0==0:
               return "fail"
           if(trunc(xlist[i],d)!=trunc(xlist[i+1],d)):
               m=(f(x1)-f(x0))/(x1-x0)
               x2= x0-f(x0)/m
               x2r=trunc(x2,d+2)

               x0=x1
               x1=x2r
               xlist.append(x2r)
           else:
                print("answer =", xlist[i])
                break
           i=i+1
        self.boollist=bolist
        self.rlist=rootlist
        self.inf="not"
        return "notfound"
    
if __name__=="__main__":
    f="x**4-x-10"
    d=1
    a=0
    c=10
    b=Secant(f,d,a,c)
    r=b.getroot()
    print(r)




