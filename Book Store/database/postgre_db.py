import psycopg2


def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='xwh7895@@' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='xwh7895@@' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='xwh7895@@' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='xwh7895@@' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='xwh7895@@' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()



create_table()
while True:
    print("What would you like to do?")
    print("1.Insert")
    print("2.View the List")
    print("3.Delete")
    print("4.Update")
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