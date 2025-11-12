from tkinter import *

root = Tk()
root.title("Number Pad")
root.geometry("300x400")
root.configure(bg = "aqua")
t = [[7,8,9],[4,5,6],[1,2,3],['#',0,'*']]
for i in range(4):
    root.rowconfigure(i,weight = 1,minsize=80)
    for j in range(3):
        root.columnconfigure(j,weight = 1,minsize = 80)
        label1 = Label(root,text = t[i][j],bg = 'grey',fg = 'black',bd = 2,relief='sunken',width = 2)
        label1.grid(row = i,column = j)
        

root.mainloop()