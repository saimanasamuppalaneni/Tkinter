from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile
def open_file():
    file1 = askopenfile(mode = 'r',filetypes = [("text files","*.txt"),("all files","*.*")])
    if file1 is not None:
        content = file1.read()
        text1.delete("1.0","end")
        text1.insert(END,content)
    file1.close()

def save_file():
    file1 = asksaveasfile(mode = 'w',filetypes = [("text files","*.txt"),("all files","*.*")])
    if file1 is not None:
        mytext = text1.get(1.0,END)
        file1.write(mytext)
    file1.close()

root = Tk()
root.title("text editor")
root.geometry("500x400")
root.configure(bg = 'white')
text1 = Text(root,width = 50 ,height = 20,relief = 'sunken',bd = 3,bg = 'grey')
button1 = Button(root,width = 7,height = 3,command = open_file,text = 'open')
button2 = Button(root,width = 7,height = 3,command = save_file,text = 'save')
text1.grid(row = 0,column = 1,rowspan = 2)
button1.grid(row = 0,column  =0)
button2.grid(row = 1,column  =0)
root.mainloop()