import tkinter as tk
root=tk.Tk()
root.title("My First App")
root.geometry("300x300")
label=tk.Label(root,text="Hello, Tkinter!",font=("Arial",16))
label.pack()
root.mainloop()
