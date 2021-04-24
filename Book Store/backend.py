import sqlite3


class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, genre TEXT, rate REAL, isbn INTEGER, img TEXT)")
        self.conn.commit()




    def insert(self,title, author, year, genre, rate, isbn, img):
        self.cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?,?,?,?)", (title, author, year, genre, rate, isbn, img))
        self.conn.commit()
        self.conn.close()


    def view(self):
        self.cur.execute("SELECT * FROM bookstore")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",genre="",rate="",isbn=""):
        self.cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR genre=? OR rate=? OR isbn=?", (title,author,year,genre,rate,isbn))
        rows=self.cur.fetchall()
        return rows


    def delete(self,id):
        self.cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
        self.conn.commit()


    def update(self,id,title, author, year, genre, rate, isbn, img):
        self.cur.execute("UPDATE bookstore SET title=?, author=?,year=?, genre=?,rate=?,isbn=?,img=? WHERE id=?",(title, author, year, genre, rate, isbn, img,id))
        self.conn.commit()
    
    def __del(self):
        self.conn.close()



