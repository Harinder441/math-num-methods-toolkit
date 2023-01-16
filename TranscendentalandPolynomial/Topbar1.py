from tkinter import *
class Topbar:
    def __init__(self,topbar,topics):
        self.tp=topics
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
        global aboutp
        aboutp = PhotoImage(file ="/home/harash/Documents/MY_projects_withpython/NUMERICAL_METHOD_Calculator/Topbar1/icon/about.png", )
        about=Button(topbar,image=aboutp,**hoption)
        about.pack(side=RIGHT,padx=icx)
        global feedbackp
        feedbackp = PhotoImage(file ="/home/harash/Documents/MY_projects_withpython/NUMERICAL_METHOD_Calculator/Topbar1/icon/feedback.png", )
        S_icon=Button(topbar,image=feedbackp,**hoption)
        S_icon.pack(side=RIGHT,padx=icx)
        global helpp
        helpp = PhotoImage(file ="/home/harash/Documents/MY_projects_withpython/NUMERICAL_METHOD_Calculator/Topbar1/icon/help.png", )
        S_icon=Button(topbar,image=helpp,**hoption)
        S_icon.pack(side=RIGHT,padx=icx)
        global searchp
        searchp = PhotoImage(file ="/home/harash/Documents/MY_projects_withpython/NUMERICAL_METHOD_Calculator/Topbar1/icon/search20.png", )
        S_icon=Button(topbar,image=searchp,**hoption)
        S_icon.pack(side=RIGHT,padx=icx)
        global homep
        homep = PhotoImage(file ="/home/harash/Documents/MY_projects_withpython/NUMERICAL_METHOD_Calculator/Topbar1/icon/home20.png")
        home=Button(topbar,text="Home",image = homep,compound=LEFT,**hoption)
        home.pack(side=LEFT,padx=2)
        sp=Label(topbar,padx=20,bd=0,bg=Mcolor)
        sp.pack(side=LEFT)
        T_P=Button(topbar,text="Transcendental and Polynomial equation",font=fn+" 10",pady=4,padx=2,**btoption,command=self.Tpe)
        T_P.pack(side=LEFT)
        S_L=Button(topbar,text="System of Linear equation",font=fn+" 11",pady=3,padx=2,**btoption,command=self.Inti)
        S_L.pack(side=LEFT)
        N_I=Button(topbar,text="Numerical Intigration",font=fn+" 11",pady=3,padx=5,**btoption)
        N_I.pack(side=LEFT)
        IP=Button(topbar,text="Interpolation",font=fn+" 11",pady=3,padx=10,**btoption)
        IP.pack(side=LEFT)
    # def Tpe(self):
    #     clear_Frame(self.tp.center)
    #     TPE(self.tp.center)
    # def Inti(self):
    #     clear_Frame(self.tp.center)

if __name__=="__main__":
    root=Tk()
    b=Topbar(root,None)
    Fc=b.Mcolor
    root.configure(bg=Fc)
    root.mainloop()
