
from tkinter import *
def Fnk():
    c=a.delete(1.0,END)
def fgh():
    a.insert(END, '   Asliddin')
    
b = Tk()
a=Text(b,width=40, height=6, font=("verdana",15))
a.pack() 
button=Button(b,text=("yozuvni uchirish"), command=Fnk)
btn=Button(text=("yozuvni chiqar"), command=fgh)
btn.pack()
button.pack()
b.mainloop()
