from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = TopLevel()
    top.geometry("toplevel")
    top.title("toplevel")

    l2 = Label = (top, text = "This is a toplevel window")
    l2.pack()

    top.mainloop()

l = label(root, text = "This is a root window")
btn = Button(root, text = "Click here to open another window" , command = topwin)

l.pack()
btn.pack