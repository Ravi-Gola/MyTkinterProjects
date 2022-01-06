from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Digital clock")
def time():
    str=strftime('%H:%M:%S %p')
    label.configure(text=str)
    label.after(1000,time)

label=Label(root,font=("ds-digital",80),background="black",foreground="cyan")
label.pack(anchor=CENTER)
time()
root.mainloop()