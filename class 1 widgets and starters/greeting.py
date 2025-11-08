from tkinter import *
from datetime import date

root = Tk()
root.title("my first window")
root.geometry("400x400")
root.configure(bg = "aqua")
def greet():
    name = entry1.get()
    dt = date.today()
    g = "Welcome"+ name + "\n Today's date is \n" +str(dt)
    text1.delete("1.0","end")
    text1.insert("1.0",g)

label1 = Label(root,text = "Name",bg = 'aqua',fg = 'navy')
label1.pack(pady = 10)
entry1 = Entry()
entry1.pack(pady = 10)
button1 = Button(root,text = "start",bg = 'navy',fg = 'aqua',width = 10 ,height = 1,command = greet)
button1.pack(pady = 10)
text1 = Text(root,bg = 'white',width = 40,height = 10)
text1.pack(pady = 10)



root.mainloop()