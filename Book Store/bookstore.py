from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from backend import Database
import requests

database=Database("books.db")

class Window(object):

    def __init__(self,window):
        self.window=window
        self.window.title("Bookstore")
        self.window.configure(bg='#856ff8')

        #Title input
        self.title=StringVar()
        self.l1=Label(text="Title")
        self.l1.grid(row=0,column=0)
        self.e1=Entry(window,textvariable=self.title)
        self.e1.grid(row=0,column=1)

        #Author input
        self.author=StringVar()
        self.l2=Label(text="Author")
        self.l2.grid(row=0,column=2)
        self.e2=Entry(window,textvariable=self.author)
        self.e2.grid(row=0,column=3)

        #Year input
        self.year=StringVar()
        self.l3=Label(text="Year")
        self.l3.grid(row=1,column=0)
        self.e3=Entry(window,textvariable=self.year)
        self.e3.grid(row=1,column=1)

        #Genre input
        self.genre=StringVar()
        self.l4=Label(text="Genre")
        self.l4.grid(row=1,column=2)
        self.e4=Entry(window,textvariable=self.genre)
        self.e4.grid(row=1,column=3)

        #Rate input
        self.rate=StringVar()
        self.l5=Label(text="Rating")
        self.l5.grid(row=2,column=0)
        self.e5=Entry(window,textvariable=self.rate)
        self.e5.grid(row=2,column=1)

        #ISBN input
        self.isbn=StringVar()
        self.l6=Label(text="ISBN")
        self.l6.grid(row=2,column=2)
        self.e6=Entry(window,textvariable=self.isbn)
        self.e6.grid(row=2,column=3)

        #URL input
        self.img_url=StringVar()
        self.l7=Label(text="Image Url")
        self.l7.grid(row=3,column=1)
        self.e7=Entry(window,textvariable=self.img_url)
        self.e7.grid(row=3,column=2)

        self.list1=Listbox(window,width=75)
        self.list1.grid(row=0,column=5,rowspan=6)

        sb1=Scrollbar(window)
        sb1.grid(row=0,column=6,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)
        self.list1.bind('<<ListboxSelect>>',self.CurSelect)

        #Search Button
        b1=Button(text ="Search Entry", width=15,foreground="red",command=self.search)
        b1.grid(row=4,column=1)

        #Add Button
        b2=Button(text ="Add Entry", width=15,command=self.add)
        b2.grid(row=4,column=3)

        #Update Button
        b3=Button(text ="Update Entry", width=15,command=self.update)
        b3.grid(row=5,column=1)

        #Delete Button
        b4=Button(text ="Delete Entry", width=15,command=self.delete)
        b4.grid(row=5,column=3)

        b5=Button(text ="Close", width=15,command=window.destroy)
        b5.grid(row=5,column=2)

    def view(self):
        for row in database.view():
            self.list1.insert(END,row)


    def search(self):
        self.list1.delete(0,END)
        for row in database.search(title.get(),author.get(),year.get(),genre.get(),rate.get(),isbn.get()):
            self.list1.insert(END,row)

    def CurSelect(self,e):
        if self.list1.size()!=0:
            global selected_tuple
            global img

            #this one will get the index and to be used for deleting an item
            index=list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            value=self.list1.get(self.list1.curselection())

            #This part will create the image box on the side and it will display the image that belongs to the book
            self.img_url1=value[len(value)-1]
            self.img = Image.open(requests.get(img_url1, stream=True).raw)
            self.img = img.resize((170,170), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(img)
            self.l8=Label(image=img)
            self.l8.grid(row=0,column=7,rowspan=5)

            #this part will bring selected item to the entrees
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])

            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])

            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])

            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])

            self.e5.delete(0,END)
            self.e5.insert(END,self.selected_tuple[5])

            self.e6.delete(0,END)
            self.e6.insert(END,self.selected_tuple[6])

            self.e7.delete(0,END)
            self.e7.insert(END, self.selected_tuple[7])

        

    def delete(self):
        database.delete(self.selected_tuple[0])
        self.list1.delete(0,END)
        view()

    def add(self):
        database.insert(self.title.get(),self.author.get(),self.year.get(),self.genre.get(),self.rate.get(),self.isbn.get(),self.img_url.get())

        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
            

        self.list1.delete(0,END)
        self.view()

    def update(self):
        database.update(self.selected_tuple[0],self.title.get(),self.author.get(),self.year.get(),self.genre.get(),self.rate.get(),self.isbn.get(),self.img_url.get())
        self.list1.delete(0,END)
        view()



window= Tk()
win=Window(window)
win.view()
window.mainloop()