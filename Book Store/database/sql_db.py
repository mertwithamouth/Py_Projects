import sqlite3


def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE store (item TEXT,quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()




while True:
    print("What would you like to do?")
    print("1.Insert")
    print("2.View the List")
    print("3.Delete")
    print("4.Delete")
    decision=int(input("Type 1,2,3 or 4: "))
    if decision==1:
        item=input("What would you like to add to the list? ")
        quantity=input("How many? ")
        price=input("What is the price? ")
        insert(item,quantity,price)
        break

    elif decision==2:
        print(view())
        break

    elif decision==3:
        print(view())
        item=input("Which Item do you want to delete?: ")
        delete(item)
        break

    elif decision==4:
        print(view())
        item=input("Which Item do you want to update?: ")
        quantity=int(input("What is the new quantity: "))
        price=float(input("What is the new price: "))
        update(quantity,price,item)
        break

    else:
        print("You put wrong key code. Please try again!")