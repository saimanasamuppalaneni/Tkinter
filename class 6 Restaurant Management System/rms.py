from tkinter import *
import random
root = Tk()
root.title("Restauraunt Management System")
root.geometry('800x400')
root.configure(bg = 'beige')
frame1 = Frame(root,width = 500,height = 300,relief = SUNKEN,bg = 'beige')
frame1.pack()
label1 = Label(frame1,font=("arial",18,'bold'),text = "Restauraunt Management System",bg = 'beige',fg = 'firebrick')
label1.grid(row = 0,column = 0,columnspan = 4,padx = 10,pady = 10)

drink = StringVar()
Pizza = StringVar()
Burger = StringVar()
LargeBurger = StringVar()
Fries = StringVar()

labeldrink = Label(frame1,font=("arial",12,'bold'),text = "Drinks",bg = 'beige',fg = 'firebrick')
labeldrink.grid(row = 3,column = 0,padx = 10,pady = 10)
entrydrink = Entry(frame1,textvariable=drink,justify = RIGHT)
entrydrink.grid(row = 3,column = 1)
entrydrink.insert(END,0)

labelpizza = Label(frame1,font=("arial",12,'bold'),text = "Pizza",bg = 'beige',fg = 'firebrick')
labelpizza.grid(row = 4,column = 0,padx = 10,pady = 10)
entrypizza = Entry(frame1,textvariable=drink,justify = RIGHT)
entrypizza.grid(row = 4,column = 1)
entrypizza.insert(END,0)

labelburger = Label(frame1,font=("arial",12,'bold'),text = "Burger",bg = 'beige',fg = 'firebrick')
labelburger.grid(row = 5,column = 0,padx = 10,pady = 10)
entryburger = Entry(frame1,textvariable=drink,justify = RIGHT)
entryburger.grid(row = 5,column = 1)
entryburger.insert(END,0)

labellargeburger = Label(frame1,font=("arial",12,'bold'),text = "Large Burger",bg = 'beige',fg = 'firebrick')
labellargeburger.grid(row = 6,column = 0,padx = 10,pady = 10)
entrylargeburger = Entry(frame1,textvariable=drink,justify = RIGHT)
entrylargeburger.grid(row = 6,column = 1)
entrylargeburger.insert(END,0)

labelfries = Label(frame1,font=("arial",12,'bold'),text = "Fries",bg = 'beige',fg = 'firebrick')
labelfries.grid(row = 7,column = 0,padx = 10,pady = 10)
entryfries = Entry(frame1,textvariable=drink,justify = RIGHT)
entryfries.grid(row = 7,column = 1)
entryfries.insert(END,0)

labelorderno = Label(frame1,font=("arial",12,'bold'),text = "OrderNo",bg = 'beige',fg = 'firebrick')
labelorderno.grid(row = 3,column = 3,padx = 10,pady = 10)
entryorderno = Entry(frame1)
entryorderno.grid(row = 3,column = 4)

labelcost = Label(frame1,font=("arial",12,'bold'),text = "Cost",bg = 'beige',fg = 'firebrick')
labelcost.grid(row = 4,column = 3,padx = 10,pady = 10)
entrycost = Entry(frame1)
entrycost.grid(row = 4,column = 4)

labelservice = Label(frame1,font=("arial",12,'bold'),text = "Service Charge",bg = 'beige',fg = 'firebrick')
labelservice.grid(row = 5,column = 3,padx = 10,pady = 10)
entryservice = Entry(frame1)
entryservice.grid(row = 5,column = 4)

labeltax = Label(frame1,font=("arial",12,'bold'),text = "Tax",bg = 'beige',fg = 'firebrick')
labeltax.grid(row = 6,column = 3,padx = 10,pady = 10)
entrytax = Entry(frame1)
entrytax.grid(row = 6,column = 4)

labeltoatl = Label(frame1,font=("arial",12,'bold'),text = "Total Cost",bg = 'beige',fg = 'firebrick')
labeltoatl.grid(row = 7,column = 3,padx = 10,pady = 10)
entrytotal = Entry(frame1)
entrytotal.grid(row = 7,column = 4)

def ex():
    root.destroy()
def reset():
    entrydrink.delete(0,END)
    entrydrink.insert(END,0)
    entryburger.delete(0,END)
    entryburger.insert(END,0)
    entryfries.delete(0,END)
    entryfries.insert(END,0)
    entrylargeburger.delete(0,END)
    entrylargeburger.insert(END,0)
    entrypizza.delete(0,END)
    entrypizza.insert(END,0)
    entrycost.delete(0,END)
    entrycost.insert(END,0)
    entryorderno.delete(0,END)
    entryorderno.insert(END,0)
    entryservice.delete(0,END)
    entryservice.insert(END,0)
    entrytax.delete(0,END)
    entrytax.insert(END,0)
    entrytotal.delete(0,END)
    entrytotal.insert(END,0)

def total():
    global drink
    global Burger
    global LargeBurger
    global Pizza
    global Fries

drink = float(drink.get())
burger = float(Burger.get())
LargeBurger = float(LargeBurger.get())
Pizza = float(Pizza.get())
Fries = float(Fries.get())

cost = 20 * drink + Pizza * 250 + burger * 150 + Fries * 75 + LargeBurger * 200
entrycost.insert(0,str(cost))
service = cost * 0.02
entryservice.insert(0,str('Rs %2f'%service))
tax = cost * 0.1
entrytax.insert(0,str('Rs %2f'%tax))
totalcost = cost+service+tax
entrytotal.insert('Rs %2f'%totalcost)
rand = random.randint(1,10000)
entryorderno.insert(0,str(rand))

def price():
    top = Toplevel()
    top.geometry("300x200")
    top.title("Top Level")
    l2 = Label(top,text = "Price",font = ('Times',22,'bold'))
    l3 = Label(top,text = "Drinks Rs. 20",font = ('Times',12,'bold'))
    l4 = Label(top,text = "Burger Rs.150",font = ('Times',12,'bold'))
    l5 = Label(top,text = "Pizza Rs .250",font = ('Times',12,'bold'))
    l6 = Label(top,text = "Largeburger Rs.200",font = ('Times',12,'bold'))
    l7 = Label(top,text = "Fries Rs.75",font = ('Times',12,'bold'))
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
    l6.pack()
    l7.pack()



button1 = Button(frame1,font=("arial",12,'bold'),text = "Price",bg = 'firebrick',fg = 'beige',command = price)
button1.grid(row = 10,column = 0,padx = 10,pady = 10)   
button2 = Button(frame1,font=("arial",12,'bold'),text = "Total",bg = 'firebrick',fg = 'beige',command = total)
button2.grid(row = 10,column = 1,padx = 10,pady = 10)
button3 = Button(frame1,font=("arial",12,'bold'),text = "Reset",bg = 'firebrick',fg = 'beige',command = reset)
button3.grid(row = 10,column = 2,padx = 10,pady = 10)
button4 = Button(frame1,font=("arial",12,'bold'),text = "Exit",bg = 'firebrick',fg = 'beige',command = ex)
button4.grid(row = 10,column = 3,padx = 10,pady = 10)

root.mainloop()
