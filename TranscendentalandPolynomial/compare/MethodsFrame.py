from tkinter import *
#if __name__=='__main__':
from  NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.Calculater.Bisectionmethod import Bisectioncode
# else:
#       from ..Calculater.Bisectionmethod import Bisectioncode
from NUMERICAL_METHOD_Calculator.Basicmodule.widgetopr import clear_Frame
from tkinter import messagebox
from sympy import *
x=symbols('x')
class BisecCalc:
    def __init__(self,root,root1,It,checkvalue):
        self.r1=root1
        self.checkvalue=checkvalue
        fn="Gill_Sans"
        Mcolor="white"
        self.Mcolor=Mcolor
        fcolor='black'
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        Foption={'bg':Bdry}
        Eoption={}
        hoption={'bg':Bdry}
        btoption={'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        self.It=It
        Top=Frame(root,**Foption)
        Top.pack(fill=X)
        Middle=Frame(root)
        Middle.pack(fill=X)
        Bottom =Frame(root)
        Bottom.pack(fill=X)
        self.Bcompare=Frame(root)
        self.Bcompare.pack(fill=X)
        # packing Top
        T1=Frame(Top,**Foption)
        T1.pack(fill=X)
        T2=Frame(Top,**Foption)
        T2.pack(fill=X)
        T3=Frame(Top,**Foption)
        T3.pack(fill=X,pady=3)
        #packing Middle
        M1=Frame(Middle,**Foption)
        M1.pack(side=LEFT,fill=X)
        M2=Frame(Middle,**Foption)
        M2.pack(side=LEFT,fill=X,expand=true)
        #packing Bottom
        B1=Frame(Bottom,**Foption)
        B1.pack(fill=X)
        # B2=Frame(Bottom,**Foption)
        # B2.pack(fill=X)
        #packing Frames of Top
        x=5
        y=10
        # packing T1
        entryv1=StringVar()
        L1 = Label(T1, text="Enter Function",font=("Nimbus Roman",14),pady=y,**hoption)
        L1.pack(side=LEFT,padx=5)
        E1 = Entry(T1, width=35, borderwidth=5,textvariable=entryv1 ,**Eoption)
        E1.pack(side=LEFT,padx=5)
        E1.insert(0,"x**4-x-10")
        #packing T2
        fs1=13 # fonts
        entryv2=StringVar()
        entryv3=StringVar()
        L2 = Label(T2, text="Find root Between",font=("Nimbus Roman",fs1),**hoption )
        L2.pack(side=LEFT,padx=5)
        E2 = Entry(T2, width=5, borderwidth=2,textvariable=entryv2)
        E2.pack(side=LEFT,padx=3)
        L3 = Label(T2, text="to",font=("Nimbus Roman",fs1),**hoption ).pack(side=LEFT)
        E3 = Entry(T2, width=5, borderwidth=2,textvariable=entryv3)
        E3.pack(side=LEFT,padx=3)
        #pre inserts
        E2.insert(0,"-20")
        E3.insert(0,"20")
        #packing T3
        entryv4=StringVar()
        L4 = Label(T3, text="Decimal Value =",font=("Nimbus Roman",fs1) ,**hoption).pack(side=LEFT,padx=5)
        E4 = Entry(T3,width=5,textvariable=entryv4)
        E4.pack(side=LEFT,padx=5)
        #pre inserts
        E4.insert(0,"4")
        #packing Middle Frame
        #packing M1
        Row1=Frame(M1)
        Row1.pack()
        Row2=Frame(M1)
        Row2.pack(fill=X,expand=TRUE)
        Row3=Frame(M1)
        Row3.pack(fill=X)
        Row4=Frame(M1)
        Row4.pack(fill=X)
        #packing frames of M2
        px = 25
        py = 15
        #row1
        b1=Button(Row1, text="x²", padx=px+12, pady=py, command=lambda: self.bclick("x**2"),**btoption).pack(side=LEFT)
        b2=Button(Row1, text="x³", padx=px+12, pady=py, command=lambda: self.bclick("x**3"),**btoption).pack(side=LEFT)
        b3=Button(Row1, text=" ** ", padx=px+8, pady=py, command=lambda: self.bclick("**"),**btoption).pack(side=LEFT)
        #row2
        b4=Button(Row2, text="sinx",  pady=py, command=lambda: self.bclick("sin(x)"),**btoption).pack(side=LEFT,fill=X,expand=TRUE)
        b5=Button(Row2, text="cosx",  pady=py, command=lambda: self.bclick("cos(x)"),**btoption).pack(side=LEFT,fill=X,expand=TRUE)
        b6=Button(Row2, text="tanx", pady=py, command=lambda: self.bclick("tan(x)"),**btoption).pack(side=LEFT,fill=X,expand=TRUE)
        #row3
        b7=Button(Row3, text="sin⁻¹x", pady=py, command=lambda: self.bclick("asin(x)"),**btoption).pack(side=LEFT,fill=X,expand=TRUE)
        b8=Button(Row3, text="cos⁻¹x", pady=py, command=lambda: self.bclick("acos(x)"),**btoption).pack(side=LEFT,fill=X,expand=TRUE)
        b9=Button(Row3, text="tan⁻¹x", pady=py, command=lambda: self.bclick("atan(x)"),**btoption).pack(side=LEFT,fill=X,expand=TRUE)
        #row4
        b10=Button(Row4, text="logx",padx=13, pady=py, command=lambda: self.bclick("log(x)"),**btoption).pack(side=LEFT,expand=TRUE,fill=X)
        b11=Button(Row4, text="log₁₀x", pady=py, command=lambda: self.bclick("log10(x)"),**btoption).pack(side=LEFT,expand=TRUE,fill=X)
        b12=Button(Row4, text="eˣ", padx=22,pady=py, command=lambda: self.bclick("exp(x)"),**btoption).pack(side=LEFT,expand=TRUE,fill=X)
        #packing M2
        #side buttons
        px1=25
        py1=15
        bs1=Button(M2, text="Clear", pady=py1, command=self.bclear,**btoption).pack(fill=X)
        bs2=Button(M2, text="Compare", pady=py1, command=self.getoutput,**btoption)
        bs2.pack(fill=X)
        bs3=Button(M2, text="Show Iteration", pady=py1, command=self.show_iteration,**btoption).pack(fill=X)
        bs4=Button(M2, text="Why error", pady=py1, command=lambda: self.bclick(7),**btoption).pack(fill=X)
        #packing Bottom Frame
        entryv5=StringVar()
        entryv6=StringVar()
        #B1
        L5 = Label(B1, text="Root =",font=("Nimbus Roman",12),pady=y,**hoption)
        L5.pack(side=LEFT,padx=5)
        E5 = Entry(B1, width=38,textvariable=entryv5)
        E5.pack(side=LEFT,padx=5)
        #B2
        # L6 = Label(B2, text="Total iteration=",font=("Nimbus Roman",12),pady=y,**hoption).pack(side=LEFT,padx=5)
        # E6 = Entry(B2, width=10,textvariable=entryv6)
        # E6.pack(side=LEFT,padx=5)
        self.E1=E1
        self.E2=E2
        self.E3=E3
        self.E4=E4
        self.E5=E5
    def bclick(self,number):
        E1=self.E1
        cr=E1.get()
        E1.delete(0,END)
        E1.insert(0,str(cr)+str(number))
    def bclear(self):
        E1=self.E1
        E5=self.E5
        #E6=self.E6
        E1.delete(0,END)
        E5.delete(0,END)
        #E6.delete(0,END)
    def getoutput(self):
        E1=self.E1
        E2=self.E2
        E3=self.E3
        E4=self.E4
        E5=self.E5
        #E6=self.E6
        f=E1.get()
        d=E4.get()
        a=E2.get()
        b=E3.get()
        CE=self.CheckError(f,d,a,b)
        if(CE=="OK"):
            d=int(E4.get())
            a=int(E2.get())
            b=int(E3.get())
            B= Bisectioncode.Bisec(f, d, a, b)
            r=B.getroot()
            if(r=="tryagain"):
                messagebox.showinfo("Root Not Found", "There is no root in given Interval \n Please change Interval")
            else:
                #itr=B.getiter()
                E5.delete(0,END)
                E5.insert(0,str(r))
                self.comparing(self.r1)
                self.Br=B
                return B

        else:
            return "ERROR"
    def show_iteration(self):
        B1=self.getoutput()
        if B1!="ERROR":
            B1.showiter()
            self.It.insertiteration()
    def CheckError(self,f,d,a,b):
         sim=None
         if f=="":
            messagebox.showinfo("Empty Input","Function input is empty\n"
                                              "Please enter a Function")
            return "ERROR"
         if "=" in f:
            messagebox.showinfo("Found  \"=\" in input","Don't write the equal to zero \npart of eq\n"
                                                       "i.e if you have f(x)=0 then   \n write only f(x)")
            return "ERROR"
         try:
             sim=eval(f)
         except NameError as e:
            messagebox.showinfo("NameError",e)
            return "ERROR"
         except Exception:
            messagebox.showinfo("SyntaxError","May be you have include symbols \nother than ( ) * - + /\n or brackets are not closed \nPlease correct it")
            return "ERROR"
         if a=="" or b=="":
            messagebox.showinfo("Empty Input","Interval values are Left empty \nPlease enter  a integer value")
            return "ERROR"
         try:
            int(a)
            int(b)
         except Exception:
            messagebox.showinfo("ValueError","Values other then integers  are\n not allowed for interval values ")
            return "ERROR"
         if d=="":
            messagebox.showinfo("Empty Input","Decimal values are Left empty \nPlease enter  a positive integer value")
            return "ERROR"
         try:
            int(d)
         except Exception:
            messagebox.showinfo("ValueError","values other then integers \nare not allowed for Decimal values ")
            return "ERROR"
         if int(d)<1:
            messagebox.showinfo("ValueError","Negetive values  are not \nallowed for Decimal values ")
            return "ERROR"
         return "OK"
    def comparing(self,root):
        clear_Frame(root)
        Bcompare=self.Bcompare
        D=self.checkvalue
        E1=self.E1
        E2=self.E2
        E3=self.E3
        E4=self.E4
        E5=self.E5
        #E6=self.E6
        f=E1.get()
        d=E4.get()
        a=E2.get()
        b=E3.get()
        #{'Bisec':0,'Secant':0,'Regula':0,'Newton':0,'Muller':0,'Horner':0}
        DL={}
        if D['Bisec']==1:
            B= Bisectioncode.Bisec(f, int(d), int(a), int(b))
            B.getroot()
            itr=B.getiter()
            DL['Bisec']=itr
        if D['Secant']==1:
            itr=7
            DL['Secant']=itr
        if D['Regula']==1:
            itr=4
            DL['Regula']=itr
        if D['Newton']==1:
            itr=5
            DL['Newton']=itr
        if D['Muller']==1:
            itr=4
            DL['Muller']=itr
        if D['Horner']==1:
            itr=5
            DL['Horner']=itr
        DL=self.arrange(DL)
        rank=['1st','2nd','3rd','4th','5th','6th']
        r=0
        for d,dv in DL.items():
            Bdry="#a7c4bc"
            fn="Gill_Sans"
            hoption={'bg':Bdry,'font':fn+" 11"}
            Label(root,text=self.lists(rank[r],d,dv),**hoption).pack(fill=X)
            r=r+1
    def lists(self,rank,name,itr):
        if name=='Bisec':
            s= rank+" Bisection Method converged to root in "+str(itr)+" iteration."
            return s
        if name=='Secant':
            s= rank+" Secant Method converged to root in "+str(itr)+" iteration."
            return s
        if name=='Regula':
            s= rank+" Regula Method converged to root in "+str(itr)+" iteration."
            return s
        if name=='Newton':
            s= rank+" Newton Method converged to root in "+str(itr)+" iteration."
            return s
        if name=='Muller':
            s= rank+" Muller Method converged to root in "+str(itr)+" iteration."
            return s
        if name=='Horner':
            s= rank+" Horner Method converged to root in "+str(itr)+" iteration."
            return s
    def arrange(self,d):
        s={}
        t=[]
        for i in d.values():
            t.append(i)
        t.sort()
        for k in t:
            for i in d:
                if d[i]==k:
                    d.pop(i)
                    s[i]=k
                    break
        return s


if __name__=="__main__":
    root=Tk()
    root.geometry("400x400")
    Fc="#a7c4bc"
    root.configure(bg=Fc)
    b=BisecCalc(root,None,None,None)
    root.mainloop()
