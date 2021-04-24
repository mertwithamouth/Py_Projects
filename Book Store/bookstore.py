from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from backend import Database
import requests

database=Database("books.db")


def view():
    for row in database.view():
        list1.insert(END,row)


def search():
    list1.delete(0,END)
    for row in database.search(title.get(),author.get(),year.get(),genre.get(),rate.get(),isbn.get()):
        list1.insert(END,row)

def CurSelect(e):
    if list1.size()!=0:
        global selected_tuple
        global img

        #this one will get the index and to be used for deleting an item
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        value=list1.get(list1.curselection())

        #This part will create the image box on the side and it will display the image that belongs to the book
        img_url1=value[len(value)-1]
        img = Image.open(requests.get(img_url1, stream=True).raw)
        img = img.resize((170,170), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        l8=Label(image=img)
        l8.grid(row=0,column=7,rowspan=5)

        #this part will bring selected item to the entrees
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])

        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])

        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])

        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])

        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])

        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])

        e7.delete(0,END)
        e7.insert(END, selected_tuple[7])

    

def delete():
    database.delete(selected_tuple[0])
    list1.delete(0,END)
    view()

def add():
    database.insert(title.get(),author.get(),year.get(),genre.get(),rate.get(),isbn.get(),img_url.get())

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
        

    list1.delete(0,END)
    view()

def update():
    database.update(selected_tuple[0],title.get(),author.get(),year.get(),genre.get(),rate.get(),isbn.get(),img_url.get())
    list1.delete(0,END)
    view()


window= Tk()
window.title("Bookstore")
window.configure(bg='#856ff8')

#Title input
title=StringVar()
l1=Label(text="Title")
l1.grid(row=0,column=0)
e1=Entry(window,textvariable=title)
e1.grid(row=0,column=1)

#Author input
author=StringVar()
l2=Label(text="Author")
l2.grid(row=0,column=2)
e2=Entry(window,textvariable=author)
e2.grid(row=0,column=3)

#Year input
year=StringVar()
l3=Label(text="Year")
l3.grid(row=1,column=0)
e3=Entry(window,textvariable=year)
e3.grid(row=1,column=1)

#Genre input
genre=StringVar()
l4=Label(text="Genre")
l4.grid(row=1,column=2)
e4=Entry(window,textvariable=genre)
e4.grid(row=1,column=3)

#Rate input
rate=StringVar()
l5=Label(text="Rating")
l5.grid(row=2,column=0)
e5=Entry(window,textvariable=rate)
e5.grid(row=2,column=1)

#ISBN input
isbn=StringVar()
l6=Label(text="ISBN")
l6.grid(row=2,column=2)
e6=Entry(window,textvariable=isbn)
e6.grid(row=2,column=3)

#URL input
img_url=StringVar()
l7=Label(text="Image Url")
l7.grid(row=3,column=1)
e7=Entry(window,textvariable=img_url)
e7.grid(row=3,column=2)

list1=Listbox(window,width=75)
list1.grid(row=0,column=5,rowspan=6)

sb1=Scrollbar(window)
sb1.grid(row=0,column=6,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',CurSelect)

#Search Button
b1=Button(text ="Search Entry", width=15,foreground="red",command=search)
b1.grid(row=4,column=1)

#Add Button
b2=Button(text ="Add Entry", width=15,command=add)
b2.grid(row=4,column=3)

#Update Button
b3=Button(text ="Update Entry", width=15,command=update)
b3.grid(row=5,column=1)

#Delete Button
b4=Button(text ="Delete Entry", width=15,command=delete)
b4.grid(row=5,column=3)

b5=Button(text ="Close", width=15,command=window.destroy)
b5.grid(row=5,column=2)

view()

window.mainloop()