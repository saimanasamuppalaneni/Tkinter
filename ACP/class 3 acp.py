from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Length Converter App")
window.geometry("500x500+600+200")
window .configure(bg = 'turquoise')
def msg():
    inc = entry1.get()
    result = int(inc)*2.54
    messagebox.showinfo("Inches to Centimeter",result)
label1 = Label(window,text = "Inches to Centimeters",bg = 'turquoise',fg = 'white', font = ("Arial",16,'bold'))
label1.place(x = 40,y = 40)
label2 = Label(window,text = "Inches :",bg = 'turquoise',fg = 'white', font = ("Arial",12,'bold'))
label2.place(x = 80,y = 80)
entry1 = Entry()
entry1.place(x = 160,y = 80)
button1 = Button(window,text = "Centimeter",bg = 'darkgrey',fg = 'white',command = msg)
button1.place(x = 130,y = 130)

window.mainloop()