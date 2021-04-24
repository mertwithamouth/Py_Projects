import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, genre TEXT, rate REAL, isbn INTEGER, img TEXT)")
    conn.commit()
    conn.close()



def insert(title, author, year, genre, rate, isbn, img):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?,?,?,?)", (title, author, year, genre, rate, isbn, img))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",genre="",rate="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR genre=? OR rate=? OR isbn=?", (title,author,year,genre,rate,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title, author, year, genre, rate, isbn, img):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE bookstore SET title=?, author=?,year=?, genre=?,rate=?,isbn=?,img=? WHERE id=?",(title, author, year, genre, rate, isbn, img,id))
    conn.commit()
    conn.close()


connect()
