from tkinter import *
def fabout1(root):
     h1=Toplevel(root,bg="white")
     h1.title("About")
     h1.geometry("350x200")
     Loption={'bg':"white",'fg':"#2f5d62"}
     Label(h1,text="About",font="Gill_Sans 13",**Loption).pack()
     Label(h1,text="                    Version 2021.6                   \n\n"
                                " Copyrights____________________________\n"
                                "         All rights reserved\n\n"
                                "For information about this application contact:\n"
                                " Harinder Singh\n"
                                "       email: harindersingh2107@gmail.com",font="Gill_Sans 11",**Loption).pack()
     h1.resizable(False, False)
     h1.mainloop()

