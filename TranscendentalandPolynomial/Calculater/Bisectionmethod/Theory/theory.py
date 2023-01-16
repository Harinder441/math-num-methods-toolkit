from tkinter import *
class theory:
    def __init__(self,root):
         MMf=Frame(root)
         MMf.pack(fill=BOTH,expand=1)
         C=Canvas(MMf)
         C.pack(side=LEFT,fill=BOTH,expand=1)
         S1=Scrollbar(MMf,orient=VERTICAL,command=C.yview)
         S1.pack(side=RIGHT,fill=Y)
         C.configure(yscrollcommand=S1.set)
         C.bind("<Configure>",lambda e:C.configure(scrollregion=C.bbox("all")))
         Sf=Frame(C)
         C.create_window((0,0),window=Sf,anchor=NW)
         global bs1
         bs1=PhotoImage(file="./Images/bisec1.png")
         L1=Label(Sf,image=bs1)
         L1.pack(pady=0)
         global bs2
         bs2=PhotoImage(file="./Images/bisec2.png")
         L2=Label(Sf,image=bs2)
         L2.pack(pady=0)
         global bs3
         bs3=PhotoImage(file="./Images/bisec.png")
         L3=Label(Sf,image=bs3)
         L3.pack(pady=0)

if __name__=='__main__':
    root=Tk()
    root.title("Bisection Method Theory")
    root.geometry("800x700")
    Fc="white"
    root.configure(bg=Fc)
    b=theory(root)
    root.resizable(False, False)
    root.mainloop()
