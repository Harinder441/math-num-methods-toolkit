from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename
class ShowIteration:
    def __init__(self,root):
        self.file=None
        #fn="Gill_Sans"
        Mcolor="#d1d9d9"
        self.Mcolor=Mcolor
        fcolor='black'
        ABcolor="#a7c4bc"
        AFcolor="white"
        Bdry="#a7c4bc"
        Foption={'bg':Bdry}
        Eoption={}
        hoption={'bg':Bdry}
        Soption={"relief":FLAT,"activerelief":'flat',"elementborderwidth":0,"jump":0,"troughcolor":'white','bg':Mcolor,'activebackground':ABcolor,'highlightbackground':Mcolor,"highlightcolor":'white'}
        btoption={'bd':0,'bg':Mcolor,'activebackground':ABcolor,'activeforeground':AFcolor,'highlightbackground':Bdry,'fg':fcolor}
        Bottom=Frame(root,pady=3,**Foption)
        Bottom.pack(side=BOTTOM,fill=X)
        Topbar=Frame(root,pady=3,**Foption)
        Topbar.pack(side=TOP,fill=X)
        Iteration=Frame(root)
        Iteration.pack(side=TOP,fill=BOTH,expand=TRUE)

        steps=Button(Topbar,text="Steps",**btoption,command=lambda :self.insertiteration('s'))
        steps.pack(side=LEFT)
        Table=Button(Topbar,text="Table Format",**btoption,command=self.insertiteration)
        Table.pack(side=LEFT)
        space2=Label(Topbar,padx=230,bg=Bdry)
        space2.pack(side=LEFT)
        #pop=Button(Topbar,text="pop",**btoption)
        #pop.pack(side=LEFT)
        Textarea=Text(Iteration,font="Optima 10",fg="#2f5d62")
        Textarea.pack(expand=TRUE,fill=BOTH)
        space1=Label(Bottom,padx=90,bg=Bdry)
        space1.pack(side=LEFT)
        clear=Button(Bottom,text="Clear",command=self.clear,**btoption)
        clear.pack(side=LEFT,padx=50)
        Save=Button(Bottom,text="Save",command=self.savefile,**btoption)
        Save.pack(side=LEFT,padx=50)
        Textarea.insert(1.0,"Press show iteration")
        #Commands
        #adding scrol bar
        S1=Scrollbar(Textarea,**Soption)
        S1.pack(side=RIGHT,fill=Y)
        S1.config(command=Textarea.yview)
        Textarea.config(yscrollcommand=S1.set)

        #Textarea.configure(state='disabled')
        self.Text=Textarea
    def savefile(self):
        file=self.file
        Textarea=self.Text
        if file == None:
            file =asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),(
            "textdocument","*.txt"
            )])
            if file=="":
                file=None
                showinfo("Verify","File not  sucsessfuly saved")
            else:
                f=open(file,"w")
                f.write(Textarea.get(1.0,END))
                f.close()
                showinfo("Verify","File sucsessfuly saved")
        else:
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            showinfo("Verify","File sucsessfuly saved")
    def clear(self):
        Textarea=self.Text
        Textarea.delete(1.0,END)

    def insertiteration(self,mode='tb'):
        Textarea=self.Text
        Textarea.configure(state='normal')
        Textarea.delete(1.0,END)
        if mode=='tb':
            file1=open("../TranscendentalandPolynomial/showiterationtb", 'r')
        else:
            file1=open("../TranscendentalandPolynomial/showiteration", 'r')
        Textarea.insert(1.0,file1.read())
        file1.close()
        Textarea.configure(state='disabled')
if __name__=="__main__":
    root1 = Tk()
    root1.geometry("650x600")
    O1=ShowIteration(root1)
    O1.insertiteration()
    root1.mainloop()
