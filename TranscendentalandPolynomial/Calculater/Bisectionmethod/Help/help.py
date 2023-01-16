from tkinter import *
import webbrowser
class Help:
   def __init__(self,root):
        Mcolor="#a7c4bc"
        MMf=Frame(root)
        MMf.pack(fill=BOTH,expand=1)
        C=Canvas(MMf,bg=Mcolor)
        C.pack(side=LEFT,fill=BOTH,expand=1)
        S1=Scrollbar(MMf,orient=VERTICAL,command=C.yview)
        S1.pack(side=RIGHT,fill=Y)
        C.configure(yscrollcommand=S1.set)
        C.bind("<Configure>",lambda e:C.configure(scrollregion=C.bbox("all")))
        Sf=Frame(C,bg=Mcolor)
        C.create_window((0,0),window=Sf,anchor=NW)
        fn="Gill_Sans"
        fn1="Stencil_Std"
        fs=" 12"
        self.Mcolor=Mcolor
        fcolor='black'
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        hoption={'padx':2,'pady':2,'font':fn+" 12",'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Mcolor,'fg':fcolor}
        btoption={'font':fn+" 13",'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        btoption1={'font':fn+" 17",'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        loption={'font':fn+" 15",'padx':2,'pady':2,'anchor':"w",'bd':0,'bg':Mcolor}

        Post=Button(Sf,text="Post Your Question.",**btoption1,command=self.askweb)
        Post.pack()
        L1=Label(Sf,text="FAQs",**loption)
        L1.pack()
        pdx=20
        self.F1 =Frame(Sf)
        self.F1.pack(padx=pdx)
        B1=Button(self.F1,text="Q1. I entered correct function but \nit is not giving  any Output?",**btoption ,command=lambda:self.Answer("1"))
        B1.pack(anchor=W)
        # self.L1=Label(F1,pady=0)
        # self.L1.pack(pady=0)
        self.b1i=0
        B2=Button(Sf,text="Q2 Why it is giving Name error?",**btoption,command=lambda:self.Answer("2"))
        B2.pack(anchor=W,padx=pdx)
        B3=Button(Sf,text="Q3 Why it is giving syntax error?",**btoption,command=lambda:self.Answer("3"))
        B3.pack(anchor=W,padx=pdx)
        B4=Button(Sf,text="Q4 can I save output?",**btoption,command=lambda:self.Answer("4"))
        B4.pack(anchor=W,padx=pdx)
        B5=Button(Sf,text="Q5 How to minimize the window?",**btoption,command=lambda:self.Answer("5"))
        B5.pack(anchor=W,padx=pdx)
        B6=Button(Sf,text="Q5 How to minimize the window?",**btoption,command=lambda:self.Answer("6"))
        B6.pack(anchor=W,padx=pdx)
        B7=Button(Sf,text="Q5 How to minimize the window?",**btoption,command=lambda:self.Answer("7"))
        B7.pack(anchor=W,padx=pdx)
        B8=Button(Sf,text="Q5 How to minimize the window?",**btoption,command=lambda:self.Answer("8"))
        B8.pack(anchor=W,padx=pdx)
        B9=Button(Sf,text="Q5 How to minimize the window?",**btoption)
        B9.pack(anchor=W,padx=pdx)
   def Answer(self,num):
        if num=="1":
             Loption={'wraplength':340,'justify':'left','font':"Arial"+" 13","bg":"#d1d9d9"}
             if self.b1i==0:
                  self.L1=Label(self.F1,text="Ans. Method does not work for discontin- -ous functions.",**Loption)
                  self.L1.pack(anchor=W)
                  self.b1i=1
             else:
                  self.L1.destroy()
                  self.b1i=0
   def askweb(self):
        webbrowser.open_new(r"https://docs.google.com/forms/d/e/1FAIpQLSdjjvQ4lz9NflMpsuJdX_KlwVLNGcL-r47K7L0FdgwNDzch1g/viewform?usp=sf_link")



if __name__=='__main__':
    root=Tk()
    root.title("Help")
    root.geometry("400x380")
    Fc="white"
    root.configure(bg=Fc)
    b=Help(root)
    root.resizable(False, False)
    root.mainloop()
