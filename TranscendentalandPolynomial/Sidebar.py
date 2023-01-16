from tkinter import *
from tkinter import messagebox
class Sidebar:
    def __init__(self,sidebar,it=None,Calframe=None,main=None):
        self.Exch=1
        self.CF=Calframe
        self.It=it
        self.MD='Bisec'
        fn="Gill_Sans"
        fn1="Stencil_Std"
        fs=" 13"
        Mcolor="#2f5d62"
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        self.Main=main
        x1=0
        y1=4
        Y1=4
        y1r=6

        Methods=Label(sidebar,text="CALCULATOR",font=fn1+" 15"+" bold",relief=GROOVE,pady=7,padx=40,bg=Mcolor,fg="white")
        Methods.pack()
        #yspace=Label(sidebar,pady=7)
       #yspace.pack(fill=X)
        #colors
        bwr=0
        color="white"
        Bisection=Button(sidebar,text="  Bisection",font=fn+fs,padx=x1,pady=y1r,command=lambda :self.bclick("Bisec"),anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry)
        Bisection.pack(fill=X)
        Secant=Button(sidebar,text="  Secant",font=fn+fs,padx=x1,pady=y1r,command=lambda :self.bclick("Secant"),anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry)
        Secant.pack(fill=X)
        Regula=Button(sidebar,text="  Regula Falsi",font=fn+fs,padx=x1,pady=y1r,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry)
        Regula.pack(fill=X)
        Newton=Button(sidebar,text="  Newton Raphson",font=fn+fs,padx=x1-5,pady=y1r,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry)
        Newton.pack(fill=X)
        Iterative=Button(sidebar,text="  Iterative",font=fn+fs,padx=x1,pady=y1r,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry)
        Iterative.pack(fill=X)
        Muller=Button(sidebar,text="  Muller's Method",font=fn+fs,padx=x1,pady=y1r,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry)
        Muller.pack(fill=X)
        Horner=Button(sidebar,text="  Horner",font=fn+fs,padx=x1,pady=y1r,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry)
        Horner.pack(fill=X)
        yspace1=Label(sidebar,pady=10,bg=color)
        yspace1.pack(fill=X)
        #COMPARISON
        self.check1= IntVar()
        self.check2= IntVar()
        self.check3= IntVar()
        self.check4= IntVar()
        self.check5= IntVar()
        self.check6= IntVar()

        Compare=Label(sidebar,text="Compare",font=fn+" 14"+" bold",relief=GROOVE,pady=7,bg=Mcolor,fg="white")
        Compare.pack(fill=X)
        Bisection=Checkbutton(sidebar,text="Bisection",font=fn+fs,padx=x1,pady=y1,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry,onvalue = 1,offvalue = 0,variable=self.check1)
        Bisection.pack(fill=X)
        Secant=Checkbutton(sidebar,text="Secant",font=fn+fs,padx=x1,pady=y1,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry,onvalue = 1,offvalue = 0,variable=self.check2)
        Secant.pack(fill=X)
        Regula=Checkbutton(sidebar,text="Regula Falsi",font=fn+fs,padx=x1,pady=y1,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry,onvalue = 1,offvalue = 0,variable=self.check3)
        Regula.pack(fill=X)
        Newton=Checkbutton(sidebar,text="Newton Raphson",font=fn+fs,padx=x1,pady=y1,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry,onvalue = 1,offvalue = 0,variable=self.check4)
        Newton.pack(fill=X)
        Muller=Checkbutton(sidebar,text="Muller's Method",font=fn+fs,padx=x1,pady=y1r,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry,onvalue = 1,offvalue = 0,variable=self.check5)
        Muller.pack(fill=X)
        Horner=Checkbutton(sidebar,text="Horner's Method",font=fn+fs,padx=x1,pady=y1r,anchor="w",bd=bwr,bg=color,activebackground=ABcolor,activeforeground=AFcolor,highlightbackground=Bdry,onvalue = 1,offvalue = 0,variable=self.check6)
        Horner.pack(fill=X)
        Letsgo=Button(sidebar,text="Let's Go",font=fn+fs,padx=x1,pady=y1,bg="#a7c4bc",command=self.Letgo)
        Letsgo.pack(fill=X)
        if self.Main!=None:
            self.Cal1=self.Main.Calculator(self.Main.Middle,self.Main.Iteration)
            self.Cal1.packi()
            self.bclick('Bisec')
    def bclick(self,number):
        if self.Exch==0:
            self.Cal1.packi()
        self.Cal1.method(number)
        self.Exch=1
        # self.clear_Frame(self.CF)
        # B=CalcArea(self.CF)
        # B.Method(number,self.It)
    def Letgo(self):
        self.checkvalue={'Bisec':self.check1.get(),'Secant':self.check2.get(),'Regula':self.check3.get(),'Newton':self.check4.get(),'Muller':self.check5.get(),'Horner':self.check6.get()}
        sum=0
        for i in self.checkvalue.values():
              sum=sum+i
        if sum>=2:
            self.Main.Compare(self.checkvalue)
            self.Exch=0
        else:
            messagebox.showinfo("Can't Compare","Select atleast two Methods")
    def clear_Frame(self,frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

if __name__=="__main__":
    root=Tk()
    root.geometry("200x700")
    Fc="white"
    root.configure(bg=Fc)
    b=Sidebar(root)
    root.mainloop()

