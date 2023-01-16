from tkinter import *

class tipstricks:
    def __init__(self,root):
        fn="Gill_Sans"
        Mcolor="#d1d9d9"
        self.Mcolor=Mcolor
        fcolor='black'
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        Foption={'bg':Bdry}
        Eoption={}
        hoption={'bg':Bdry,'font':fn+" 11"}
        btoption={'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        L1=Label(root,text="Some Tips",bd=1,relief=RAISED,font=fn+" 12",padx=225,bg=Mcolor)
        L1.pack()
        L2=Label(root,text=" 1 Always check the function for error before pressing get output.",**hoption)
        L2.pack(anchor=W)
        L3=Label(root,text="2 Enter only integer value in Interval and Decimal Point.",**hoption)
        L3.pack(anchor=W)
        L4=Label(root,text="3 See theory for better understanding.",**hoption)
        L4.pack(anchor=W)
        L51=Label(root,text="4 Click steps to see iteration elaborately.",**hoption)
        L51.pack(anchor=W)
        L6=Label(root,text="5 You can see which method is better by comparing.",**hoption)
        L6.pack(anchor=W)
        f1=Frame(root,**Foption)
        f1.pack(anchor=W,pady=2)
        B1=Button(f1,text="Click",**btoption)
        B1.pack(side=LEFT)
        L5=Label(f1,text=" to get more tips.",**hoption)
        L5.pack(side=LEFT)
if __name__=="__main__":
    root1=Tk()
    root1.geometry("470x210")
    Fc="#a7c4bc"
    root1.configure(bg=Fc)
    O=tipstricks(root1)
    root1.mainloop()
