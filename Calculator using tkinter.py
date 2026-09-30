#Write a Python script to make calculator using Tkinter.

import tkinter as tk
root=tk.Tk()
def add():
    result.set(float(e1.get())+float(e2.get()))
def sub():
    result.set(float(e1.get())-float(e2.get()))
def mul():
    result.set(float(e1.get())*float(e2.get()))
def div():
    result.set(float(e1.get())/float(e2.get()))
root.title("My First Calc")
root.geometry("230x140")
tk.Label(root,text="First Number").grid(row=0,column=0)
tk.Label(root,text="Second Number").grid(row=1,column=0)
e1=tk.Entry(root)
e2=tk.Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
result=tk.StringVar()
tk.Label(root,text="Result").grid(row=2,column=0)
tk.Entry(root,textvariable=result).grid(row=2,column=1)
tk.Button(root,text="Add",command=add).grid(row=3,column=0)
tk.Button(root,text="Subtract",command=sub).grid(row=3,column=1)
tk.Button(root,text="Multiply",command=mul).grid(row=4,column=0)
tk.Button(root,text="Divide",command=div).grid(row=4,column=1)
root.mainloop()
