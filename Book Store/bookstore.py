from tkinter import *


window= Tk()

def km_to_miles():
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)
    t1.insert(END,' miles')
    t1.insert(END,'\n')


b1=Button(window, text="Execute",activebackground="blue",activeforeground="blue",command=km_to_miles)
b1.grid(row=0,column=0)


#input
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)


t1=Text(window,height=5,width=20)
t1.grid(row=0,column=2)

window.mainloop()