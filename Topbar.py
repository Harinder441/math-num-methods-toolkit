from tkinter import *
from NUMERICAL_METHOD_Calculator.Basicmodule.widgetopr import clear_Frame
from NUMERICAL_METHOD_Calculator.TranscendentalandPolynomial.PolynomialHome import TPE
from NUMERICAL_METHOD_Calculator.Topbar1.dialogs.aboutf import fabout1
import webbrowser
class Topbar:
    def __init__(self,topbar,topics):
        self.tp=topics
        fn="Gill_Sans"
        fn1="Stencil_Std"
        fs=" 12"
        Mcolor="#a7c4bc"
        Mcolor1="#d1d9d9"
        self.Mcolor=Mcolor
        fcolor='black'
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        hoption={'padx':2,'pady':2,'font':fn+" 12",'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Mcolor,'fg':fcolor}
        hoption1={'padx':2,'pady':2,'font':fn+" 6",'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Mcolor,'fg':fcolor}
        btoption={'anchor':"w",'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        btoption2={'relief':RAISED,'anchor':"w",'bd':0,'bg':Mcolor1,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        lboption={'padx':2,'pady':2,'anchor':"w",'bd':0,'bg':Mcolor}
        self.moption={'bg':Mcolor,'font':fn+" 10",'fg':fcolor}
        icx=7
        global aboutp
        aboutp = PhotoImage(file ="./Topbar1/icon/about.png", )
        about=Button(topbar,text="About",image=aboutp,**hoption1,compound=TOP,command=self.fabout)
        about.pack(side=RIGHT,padx=icx)
        global feedbackp
        feedbackp = PhotoImage(file ="./Topbar1/icon/feedback.png", )
        S_icon=Button(topbar,text="Feedback",image=feedbackp,**hoption1,compound=TOP,command=self.feedback)
        S_icon.pack(side=RIGHT,padx=icx)
        global helpp
        helpp = PhotoImage(file ="./Topbar1/icon/help.png", )
        S_icon=Button(topbar,text="Tutorial",image=helpp,**hoption1,compound=TOP)
        S_icon.pack(side=RIGHT,padx=icx)
        global searchp
        searchp = PhotoImage(file ="./Topbar1/icon/search20.png", )
        S_icon=Button(topbar,text="Search",image=searchp,**hoption1,compound=TOP)
        global homep
        homep = PhotoImage(file ="./Topbar1/icon/home20.png")
        home=Button(topbar,text="Home",image = homep,compound=LEFT,**hoption)
        home.pack(side=LEFT,padx=2)
        sp=Label(topbar,padx=20,bd=0,bg=Mcolor)
        sp.pack(side=LEFT)
        #packing method
        topicsf=Frame(topbar,bg=Mcolor)
        topicsf.pack(side=LEFT,fill=Y)
        ppx=0
        pbx=2
        T_P=Button(topicsf,text="Transcendental and Polynomial equation",font=fn+" 10",pady=3,padx=4+pbx,**btoption2,command=self.Tpe)
        T_P.pack(side=LEFT,padx=ppx)
        S_L=Button(topicsf,text="System of Linear equation",font=fn+" 11",pady=2,padx=2+pbx,**btoption2,command=self.syst)
        S_L.pack(side=LEFT,padx=ppx)
        N_I=Button(topicsf,text="Numerical Intigration",font=fn+" 11",pady=2,padx=5+pbx,**btoption2,command=self.Inti)
        N_I.pack(side=LEFT,padx=ppx)
        IP=Button(topicsf,text="Interpolation",font=fn+" 11",pady=2,padx=10+pbx,**btoption2,command=self.inter)
        IP.pack(side=LEFT,padx=ppx)
        self.topbar=topbar
    def Tpe(self):
        clear_Frame(self.tp.center)
        TPE(self.tp.center,None)
    def Inti(self):
        clear_Frame(self.tp.center)
    def inter(self):
        clear_Frame(self.tp.center)
    def syst(self):
        clear_Frame(self.tp.center)
    def fabout(self):
        fabout1(self.topbar)
    def feedback(self):
        webbrowser.open_new(r"https://docs.google.com/forms/d/e/1FAIpQLSdpjfkapKbq0JckbN8ykWBU4GLZ7rdaPTjaUFRr1HW7pjbRvg/viewform?usp=sf_link")

if __name__=="__main__":
    root=Tk()
    root.geometry("1370x35")
    b=Topbar(root,None)
    Fc=b.Mcolor
    root.configure(bg=Fc)
    root.mainloop()
