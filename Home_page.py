from tkinter import *
from NUMERICAL_METHOD_Calculator.Bottombar import Btbar
from NUMERICAL_METHOD_Calculator.Topbar import Topbar
from NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.PolynomialHome import TPE
from NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.Calculator_Area import CalcArea
from NUMERICAL_METHOD_Calculator.Basicmodule.widgetopr import clear_Frame


class TopicW:
    def __init__(self, root):
        self.root1 = root
        self.mframe = Frame(self.root1)
        self.mframe.pack()
        self.popin()

    def popin(self):
        clear_Frame(self.mframe)
        # self.root1.geometry("1366x768")

        self.bottombar = Frame(self.mframe, bd=2, pady=0, bg="#a7c4bc")
        self.bottombar.pack(side=BOTTOM, fill=X)
        self.topbar = Frame(self.mframe, bd=2, pady=0, bg="#a7c4bc")
        self.topbar.pack(side=TOP, fill=X)
        self.center = Frame(self.mframe, padx=0, pady=0, bg="white")
        self.center.pack(fill=X)
        TP = TPE(self.center, self)
        T1 = Topbar(self.topbar, self)
        B1 = Btbar(self.bottombar)

    def popout(self, func, method=None):
        # self.root1.geometry("485x465")
        # self.root1.iconify()
        clear_Frame(self.mframe)
        if func == "Calc1":
            C = CalcArea(self.mframe, self, 'o')
            C.Method(method, None)


if __name__ == '__main__':
    root = Tk()
    root.title("Numerical Method Calculator")
    # root.minsize(150,100)
    o1 = TopicW(root)
    root.mainloop()
