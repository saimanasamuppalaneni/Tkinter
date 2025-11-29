from tkinter import *
window = Tk()
window.title("getting started with widgets")
window.geometry("400x400")
window.configure(bg = "aqua")

def product():
    label1 = int(entry1.get())
    label3 = int(entry3.get())
    pro = label1*label3
    product = "the product is "
    text1.delete("1.0","end")
    text1.insert("1.0",product,pro)

label1 = Label(window,text = "Number a",bg = 'aqua',fg = 'navy',font = ("Arial",16,'bold'))
label1.pack(pady = 10)
entry1 = Entry()
entry1.pack(pady = 10)

label2 = Label(window,text = "x",bg = 'aqua',fg = 'navy',font = ("Arial",24,'bold'))
label2.pack(pady = 10)

label3 = Label(window,text = "Number b",bg = 'aqua',fg = 'navy',font = ("Arial",16,'bold'))
label3.pack(pady = 10)
entry3 = Entry()
entry3.pack(pady = 10)


button1 = Button(window,text = "click me!",bg = 'navy',fg = 'aqua',width = 10 ,height = 1,command = product)
button1.pack(pady = 10)
text1 = Text(window,bg = 'white',width = 40,height = 10)
text1.pack(pady = 10)



window.mainloop()

