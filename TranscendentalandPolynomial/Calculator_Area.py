from tkinter import *
#from . import Bisectionmethod

from NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.Calculater.Bisectionmethod import BisectionFrame as Bw
from NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.Calculater.Secant_Method import SecantFrame as SF
from NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.Calculater.Bisectionmethod.Theory.theory import theory
from NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.Calculater.Bisectionmethod.Help.help import Help
class CalcArea:
    def __init__(self,Calc,home,popi='i'):
        self.pp=popi
        self.home1=home
        self.Calc=Calc

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
        #now packing inner frames
        methodname=Label(calc1,font=fn+"30"+"Bold",relief=GROOVE,pady=7,padx=170,**hoption)
        methodname.pack(side=TOP)
        #Tools
        bx=2
        B1=Menubutton(calc1,text="Tools",**btoption)
        self.toolses(B1)
        B2=Button(calc1,text="Theory",**btoption,command=self.theory1)
        #B2.bind("<Button>",lambda e: theory(Calc))
        B3=Button(calc1,text="Help",**btoption,command=self.help1)
        B1.pack(side=LEFT,fill=X,padx=bx)
        B2.pack(side=LEFT,fill=X,padx=bx)
        B3.pack(side=LEFT,fill=X,padx=bx)
        spacel1=Label(calc1,padx=110,bg=Bdry)
        spacel1.pack(side=LEFT)
        B0=Button(calc1,text="pop",padx=5,**btoption,command=self.popio)
        B0.pack(side=LEFT,fill=X)
        self.calc1=calc1
        self.calc2=calc2
        self.name=methodname
    def Method(self,name,It): #L=['Bisec','Regula']
        self.mtname=name
        if name=='Bisec':
            self.name.config(text="Bisection Method")
            self.Bs=Bw.BisecCalc(self.calc2,It)
        elif name=='Secant':
            self.name.config(text="Secant Method")
            Bs=SF.SecantCalc(self.calc2,It)
    def theory1(self):
        t1=Toplevel(self.Calc,bg='white')
        t1.title("Bisection Method Theory")
        t1.geometry("800x700")
        theory(t1)
        t1.resizable(False, False)
        #t1.overrideredirect(1)
        t1.mainloop()
    def help1(self):
        h1=Toplevel(self.Calc,bg="white")
        h1.title("Help")
        h1.geometry("400x380")
        Help(h1)
        h1.resizable(False, False)
        h1.mainloop()

    def popio(self):
        if self.pp =='i':
            self.home1.popout('Calc1',self.mtname)
        else:
            self.home1.popin()
    def toolses(self,tools):
        moption={'activebackground':"#a7c4bc",'activeforeground':"white"}
        tools.menu =  Menu ( tools, tearoff = 0 )
        tools.menu.choice=Menu(tools.menu, tearoff = 0)
        tools["menu"] =  tools.menu
        tools.menu.choice.add_command(label="x**3+x-1",**moption,command=lambda :self.tclick("x**3+x-1"))
        tools.menu.choice.add_command(label="x-2*sin(x)",**moption,command=lambda :self.tclick("x-2*sin(x)"))
        tools.menu.choice.add_command(label="x-e^(-x)",**moption,command=lambda :self.tclick("x-exp(-x)"))
        tools.menu.choice.add_command(label="x+log(x)-2",**moption,command=lambda :self.tclick("x+log(x)-2"))
        tools.menu.choice.add_command(label="x**4-x-10",**moption,command=lambda :self.tclick("x**4-x-10"))
        tools.menu.choice.add_command(label="3*x-cos(x)-1",**moption,command=lambda :self.tclick("3*x-cos(x)-1"))
        tools.menu.choice.add_command(label="x-tan(x)",**moption,command=lambda :self.tclick("x-tan(x)"))
        tools.menu.choice.add_command(label="sin(x)+cos(x)-1",**moption,command=lambda :self.tclick("sin(x)+cos(x)-1"))
        tools.menu.choice.add_command(label="log(x)-cos(x)",**moption,command=lambda :self.tclick("log(x)-cos(x)"))
        tools.menu.add_cascade (label="Some function",menu=tools.menu.choice,**moption)
        tools.menu.add_command(label="Why Error",**moption,command=self.fwhyerror)
        tools.pack()
    def tclick(self,num):
        self.Bs.addsomefunc(num)
    def fwhyerror(self):
        pass
if __name__=="__main__":
    root=Tk()
    root.geometry("485x465")
    b=CalcArea(root,None)
    b.Method("Bisec",None)
    root.mainloop()

