from tkinter import *


window= Tk()
window.configure(bg='grey')

def kg_to_convert():
    grams=float(e1_value.get())*1000
    t1.insert(END,grams)
    t1.insert(END,' grams')
    t1.insert(END,'\n')

    pounds=float(e1_value.get())*2.20462
    t2.insert(END,pounds)
    t2.insert(END,' pounds')
    t2.insert(END,'\n')

    ounces=float(e1_value.get())*35.274 
    t3.insert(END,ounces)
    t3.insert(END,' ounces')
    t3.insert(END,'\n')


b1=Button(window, text="Execute",activebackground="blue",activeforeground="blue",command=kg_to_convert)
b1.grid(row=0,column=2)

e2=Label(window,text="Kg")
e2.grid(row=0,column=0)
#input
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)


t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()