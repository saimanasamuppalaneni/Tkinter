from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("400x400")
window.configure(bg = 'beige')

def key_pressed(event):
    print(event.char)
window.bind("<Key>",key_pressed)
def mouse_click(event):
    print("the mouse clicked")

button1 = Button(window,text = "click me!",bg = 'grey',fg = 'white',width = 10,height = 1)
button1.place(x=70,y=70)
button1.bind("<Button-1>",mouse_click)

window.mainloop()
