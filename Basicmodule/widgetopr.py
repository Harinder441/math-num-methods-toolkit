from tkinter import *
def clear_Frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
