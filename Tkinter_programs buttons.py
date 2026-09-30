import tkinter as tk
def show_text():
    text=entry.get()
    print("You typed: ",text)
root=tk.Tk()
root.title("Input App")
root.geometry("300x300")
entry=tk.Entry(root)
entry.pack()
btn=tk.Button(root,text="Show text", command=show_text)
btn.pack()
root.mainloop()
