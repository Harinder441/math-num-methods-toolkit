from tkinter import *
from Bisectioncode import *
class newwindow(Toplevel):
    def __init__(self,master=None):
        super().__init__(master=master)
        self.title("Bisection_Method")
        self.geometry("430x410")
        #let us start the code
        #commands
        def bclick(number):
            cr=E1.get()
            E1.delete(0,END)
            E1.insert(0,str(cr)+str(number))
        def getoutput():
            f=E1.get()
            d=int(E4.get())
            if(check1.get()==1):
                B=Bisec(f,d)
                r=B.getroot()
            else:
                a=int(E2.get())
                b=int(E3.get())
                B=Bisec(f,d,a,b)
                r=B.getroot()
            E5.delete(0,END)
            E5.insert(0,str(r))
        def bclear():
            E1.delete(0,END)
            E5.delete(0,END)
            E6.delete(0,END)
        #total 9 columns
        #first row
        x=5
        y=10
        entryv1=StringVar()
        L1 = Label(self, text="Enter Function",font=("Nimbus Roman",14),pady=y).grid(row=0, column=0, columnspan=3)
        E1 = Entry(self, width=35, borderwidth=5,textvariable=entryv1)
        E1.grid(row=0, column=3, columnspan=6)
    
        #2nd row
        fs1=12
        check1=IntVar()
        entryv2=StringVar()
        entryv3=StringVar()
        C1 = Checkbutton(self,text="Any_self  or",font=("Nimbus Roman",fs1),pady=y,onvalue = 1,offvalue = 0,variable=check1)
        C1.grid(row=1, column=0, columnspan=3)
        L2 = Label(self, text="Between",font=("Nimbus Roman",fs1),pady=y).grid(row=1,column=3, columnspan=3)
        E2 = Entry(self, width=5, borderwidth=2,textvariable=entryv2)
        E2.grid(row=1, column=6)
        L3 = Label(self, text="to",pady=y,font=("Nimbus Roman",fs1)).grid(row=1, column=7)
        E3 = Entry(self, width=5, borderwidth=2,textvariable=entryv3)
        E3.grid(row=1, column=8)
        #pre inserts
        E2.insert(0,"-20")
        E3.insert(0,"20")
        #3rd row
        entryv4=StringVar()
        L4 = Label(self, text="Decimal Value =",font=("Nimbus Roman",fs1),pady=y).grid(row=2, column=0, columnspan=4)
        E4 = Entry(self,width=5, borderwidth=2,textvariable=entryv4)
        E4.grid(row=2, column=4)
        #pre inserts
        E4.insert(0,"4")
        #buttons
        '''
        b1 b2 b3 bs1
        b4 b5 b6 bs2
        b7 b8 b9 bs3
        10 11 12 bs4
        '''
        px = 25
        py = 15
        b1=Button(self, text="x**2", padx=px+3, pady=py, command=lambda: bclick("x**2")).grid(row=4, column=0, columnspan=2)
        b2=Button(self, text="x**3", padx=px+3, pady=py, command=lambda: bclick("x**3")).grid(row=4, column=2, columnspan=2)
        b3=Button(self, text=" ** ", padx=px+7, pady=py, command=lambda: bclick("**")).grid(row=4, column=4, columnspan=2)
        b4=Button(self, text="sinx", padx=px+4, pady=py, command=lambda: bclick("sin(x)")).grid(row=5, column=0, columnspan=2)
        b5=Button(self, text="cosx", padx=px+4, pady=py, command=lambda: bclick("cos(x)")).grid(row=5, column=2, columnspan=2)
        b6=Button(self, text="tanx", padx=px+4, pady=py, command=lambda: bclick("tan(x)")).grid(row=5, column=4, columnspan=2)
        b7=Button(self, text="sin-1x", padx=px-3, pady=py, command=lambda: bclick("asin(x)")).grid(row=6, column=0, columnspan=2)
        b8=Button(self, text="cos-1x", padx=px-3, pady=py, command=lambda: bclick("acos(x)")).grid(row=6, column=2, columnspan=2)
        b9=Button(self, text="tan-1x", padx=px-3, pady=py, command=lambda: bclick("atan(x)")).grid(row=6, column=4, columnspan=2)
        b10=Button(self, text="logx", padx=px+3, pady=py, command=lambda: bclick("log(x)")).grid(row=7, column=0, columnspan=2)
        b11=Button(self, text="log10x", padx=px-2, pady=py, command=lambda: bclick("log10(x)")).grid(row=7, column=2, columnspan=2)
        b12=Button(self, text="e^x", padx=px+5, pady=py, command=lambda: bclick("exp(x)")).grid(row=7, column=4, columnspan=2)
        #side buttons
        px1=25
        py1=15
        bs1=Button(self, text="      Clear    ", padx=30, pady=py1, command=bclear).grid(row=4, column=6, columnspan=3)
        bs2=Button(self, text="   Get output  ", padx=px1, pady=py1, command=getoutput)
        bs2.grid(row=5, column=6, columnspan=3)
        bs3=Button(self, text="Show Iteration", padx=23, pady=py1, command=lambda: bclick(7)).grid(row=6, column=6, columnspan=3)
        bs4=Button(self, text="   Why error   ", padx=px1, pady=py1, command=lambda: bclick(7)).grid(row=7, column=6, columnspan=3)
        #last column
        entryv5=StringVar()
        entryv6=StringVar()
        L5 = Label(self, text="Root =",font=("Nimbus Roman",12),pady=y).grid(row=9, column=0, columnspan=2)
        E5 = Entry(self, width=38, borderwidth=2,textvariable=entryv5)
        E5.grid(row=9, column=2, columnspan=7)
        L6 = Label(self, text="Total iteration=",font=("Nimbus Roman",12),pady=y).grid(row=10, column=0, columnspan=4)
        E6 = Entry(self, width=10, borderwidth=2,textvariable=entryv6)
        E6.grid(row=10, column=4)
    
