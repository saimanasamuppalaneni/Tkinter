from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Event Handler")
window.geometry("400x400")
window.configure(bg = 'beige')

def msg():
    messagebox.showinfo("Alert","virus detected!!!!!")
    ans = messagebox.askyesno("answer","do you want to continue?")
    if ans:
        print("pressed yes")
    else:
        print("pressed no")
    

button1 = Button(window,text = "click me!",bg = 'grey',fg = 'white',width = 10,height = 1,command = msg)
button1.place(x=70,y=70)

window.mainloop()