from tkinter import *
class Btbar:
    def __init__(self,btbar):
        fn="Gill_Sans"
        fn1="Stencil_Std"
        fs=" 12"
        Mcolor="#a7c4bc"
        self.Mcolor=Mcolor
        fcolor='black'
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        hoption={'padx':2,'pady':2,'font':fn+" 12",'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Mcolor,'fg':fcolor}
        btoption={'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        lboption={'padx':2,'pady':2,'anchor':"w",'bd':0,'bg':Mcolor}
        icx=5
        home=Button(btbar,text="Bot",**hoption)
        home.pack(side=LEFT,padx=2)
        sp=Label(btbar,padx=665,bd=0,bg=Mcolor)
        sp.pack(side=LEFT)


if __name__=="__main__":
    root=Tk()
    root.geometry("1373x30")
    b=Btbar(root)
    Fc=b.Mcolor
    root.configure(bg=Fc)
    root.mainloop()
