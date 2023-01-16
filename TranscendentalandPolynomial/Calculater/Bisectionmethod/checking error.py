from sympy import *
from tkinter import messagebox
x=symbols('x')
f="x**4-x-"
a="g"
b=2
d=4
def CheckError():
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
E=CheckError()
print(E)
