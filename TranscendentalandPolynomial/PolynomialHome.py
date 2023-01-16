from tkinter import *
if __name__=="__main__":
    from tips import tipstricks
    from Show_Iteration import ShowIteration
    from Calculator_Area import CalcArea
    from Sidebar import Sidebar
    from Compare import CompareArea
    from Topbar1 import Topbar
    from Bottombar1 import Btbar
else:
    from .tips import tipstricks
    from .Show_Iteration import ShowIteration
    from .Calculator_Area import CalcArea
    from .Sidebar import Sidebar
    from .Compare import CompareArea

from NUMERICAL_METHOD_Calculator.Basicmodule.widgetopr import clear_Frame

class TPE:
    def __init__(self,root,home):
        global home1
        home1=home
        if __name__=="__main__":
            self.bottombar=Frame(root,bd=2,pady=2,bg="#a7c4bc")
            self.bottombar.pack(side=BOTTOM,fill=X)
            self.topbar=Frame(root,bd=2,pady=2,bg="#a7c4bc")
            self.topbar.pack(side=TOP,fill=X)
            T1=Topbar(self.topbar,None)
            B1=Btbar(self.bottombar)

        self.Iteration=Frame(root,bd=2)
        self.Iteration.pack(side=RIGHT,fill=Y)
        self.Mcolor="white"

        self.sidebar=Frame(root,bd=4,bg=self.Mcolor)
        self.sidebar.pack(side=LEFT,fill=Y)
        self.Middle=Frame(root)
        self.Middle.pack(fill=Y)

        # packing Top Bar

        # Cal1=self.Calculator(self.Middle,self.Iteration)
        # Cal1.method('Bisec')
        S=Sidebar(self.sidebar,main=self)
        #packing Tips Area

    class Calculator:
        def __init__(self,Middle,Iter):
            self.Middle=Middle
            self.Iteration=Iter
        def packi(self):
            clear_Frame(self.Middle)
            clear_Frame(self.Iteration)
            M1color="#d1d9d9"
            self.Calc=Frame(self.Middle,bg=M1color)
            self.Calc.pack(side=TOP,anchor="nw",padx=2)
            Tips=Frame(self.Middle,bd=0,relief=GROOVE,bg="#a7c4bc")
            Tips.pack(side=TOP,anchor=N,fill=Y,pady=5,expand=1,padx=0)
            self.I1=ShowIteration(self.Iteration)
            T=tipstricks(Tips)
        def method(self,meth):
            clear_Frame(self.Calc)
            b=CalcArea(self.Calc,home1)
            b.Method(meth,self.I1)


    def Compare(self,checkvalue):
        M1color="#d1d9d9"
        clear_Frame(self.Middle)
        clear_Frame(self.Iteration)
        Label(self.Middle,padx=100).pack()
        Com=Frame(self.Middle,bd=2,bg=M1color)
        Com.pack(side=TOP,anchor="nw",fill=Y)
        self.I1=ShowIteration(self.Iteration)
        b=CompareArea(Com,checkvalue)
        b.Method(self.I1)
if __name__=="__main__":
    root = Tk()
    root.title("Numerical Method Calculator")
    root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
    ob=TPE(root,None)
    root.configure(bg=ob.Mcolor)
    root.mainloop()
