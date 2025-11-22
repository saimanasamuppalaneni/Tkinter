from tkinter import *
root = Tk()
root.title("main window")
root.geometry('500x400')

def top1():
    top1 = Toplevel()
    top1.geometry('200x300')
    top1.title("this is the top window")
    label2 = Label(top1,text = 'top level window')
    label2.pack()

button1 = Button(root,text = "click me!")
label1 = Label(root,text = "main window")
label1.place(x = 130,y = 120)
button1 = Button(root,text = "click me!",command = top1)
button1.place(x = 150,y = 150)

root.mainloop()