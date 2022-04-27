from tkinter import *
def karra():
    n=int(a.get())
    m=int(b.get())
    c.delete(0.,END)
    for i in range(m+1):
        son=str(i*n)+'\n'
        c.insert(END,son)   
window =Tk()
window.title('karrali son')
window.geometry('250x350')
window.configure(background='orange')
k=Label(window,text='son',bg='orange')
k.grid(row=0, column=0)
d=Label(window , text='natija', bg='red')
d.grid(row=2,column=4)
a=Entry(window, width=5)
a.grid(row=1,column=0)
karra_soni=Label(window,text='karra_soni',bg='yellow')
karra_soni.grid(row=0,column=4)
b=Entry(window, width=5)
b.grid(row=1, column=4)
c= Text(window, height=15,width=6)
c.grid(row=3, column=4)
t=Button(window,text='karali sonlar', command=karra)
t.grid(row=1, column=5)
window.mainloop()

