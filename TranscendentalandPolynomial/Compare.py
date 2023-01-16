from tkinter import *
#from . import Bisectionmethod
from  NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.compare import MethodsFrame as Bw

#from Calculater.Secant_Method import SecantFrame as SF
class CompareArea:
    def __init__(self,Calc,checkvalue):
        self.Ch=checkvalue
        fn="American_Typewriter"
        #fn="Gill_Sans"
        Mcolor="#d1d9d9"
        self.Mcolor=Mcolor
        fcolor='black'
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        Foption={'bg':Bdry}
        Eoption={}
        hoption={'bg':Bdry}
        btoption={'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        #Now packing Calculator area
        calc1=Frame(Calc,bd=2,**Foption)
        calc1.pack(side=TOP,anchor="nw")
        calc2=Frame(Calc,bd=2,padx=25,bg=Mcolor)
        calc2.pack(side=TOP,anchor="nw")
        calc3=Frame(Calc,bd=2,bg=Mcolor)
        calc3.pack(side=TOP,anchor="nw",fill=X)
        #now packing inner frames
        methodname=Label(calc1,font=fn+"30"+"Bold",relief=GROOVE,pady=7,padx=170,**hoption)
        methodname.pack(side=TOP)
        #Tools
        bx=2
        B1=Button(calc1,text="Tools",**btoption)
        B2=Button(calc1,text="Theory",**btoption)
        B3=Button(calc1,text="Help",**btoption)
        B1.pack(side=LEFT,fill=X,padx=bx)
        B2.pack(side=LEFT,fill=X,padx=bx)
        B3.pack(side=LEFT,fill=X,padx=bx)
        spacel1=Label(calc1,padx=110,bg=Bdry)
        spacel1.pack(side=LEFT)
        B0=Button(calc1,text="pop",padx=5,**btoption)
        B0.pack(side=LEFT,fill=X)
        self.calc1=calc1
        self.calc2=calc2
        self.calc3=calc3
        self.name=methodname
    def Method(self,It): #L=['Bisec','Regula'
        self.name.config(text="Compairing Methods")
        Bs=Bw.BisecCalc(self.calc2,self.calc3,It,self.Ch)
        #Bs.comparing(self.calc3)

if __name__=="__main__":
    root=Tk()
    root.geometry("485x465")
    b=CompareArea(root,None)
    b.Method(None)
    root.mainloop()
