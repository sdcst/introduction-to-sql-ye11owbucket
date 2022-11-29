#!python

import sqlite3
file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)
cursor = connection.cursor()
query = """
create table if not exists pet (
    id integer primary key autoincrement,
    petname tinytext,
    petspecies tinytext,
    petbreed tinytext,
    ownername tinytext,
    ownerphonenumber tinytext,
    owneremail tinytext,
    ownerbalance tinytext,
    firstvisit tinytext);
"""
cursor.execute(query)

def addition():
    petname = input("Enter pet name ")
    petspecies = input("Enter scecies ")
    petbreed = input("Enter breed")
    ownername = input("Enter ownername")
    ownerphonenumber = input("Enter phone nuber")
    owneremail = input("Enter email")
    ownerbalance = float(input("Enter moner"))
    firstvisit = input("Enter time of first visit")
    list = [petname, petspecies, petbreed, ownername, ownerphonenumber, owneremail, ownerbalance, firstvisit]
    query = f"insert into customers (petname, petspecies, petbreed, ownername, ownerphonenumber, owneremail, ownerbalance, firstvisit) values ('{list[0]}','{list[1]}','{list[2]}','{list[3]}','{list[4]}','{list[5]}','{list[6]}','{list[7]}')"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def readid():
    x = input("Enter Id: ")
    query = f'select * from customers where id={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readname():
    x = input("Enter Pet Name: ")
    query = f'select * from customers where petname={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readspec():
    x = input("Enter Species: ")
    query = f'select * from customers where petspecies={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readbreed():
    x = input("Enter Breed: ")
    query = f'select * from customers where petbreed={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readownname():
    x = input("Enter Owner Name: ")
    query = f'select * from customers where ownername={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readphone():
    x = input("Enter Phone #: ")
    query = f'select * from customers where ownerphonenumber={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)
    
def reademail():
    x = input("Enter Email: ")
    query = f'select * from customers where owneremail={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readbal():
    x = input("Enter Balance: ")
    query = f'select * from customers where ownerbalance={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readvisit():
    x = input("Enter Date of First Visit: ")
    query = f'select * from customers where firstvisit={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)






for __name__ in "__main__":
    while True:
        print("press 1 to add new customer\npress 2 to get customers info\npress anything else to exit")
        y = input("Enter:")
        if y == '1':
            addition()
        if y == '2':
            print("1 for email\n2 for id\n3 for phone number")
            x = input("Enter: ")
        else:
            exit()


    





#petname petspecies petbreed ownername ownerphonenumber owneremail ownerbalance firstvisit 








#def ball()
    """
    Create a program that will store the database for a veterinary
    Each record needs to have the following information:
    id unique integer identifier
    pet name
    pet species (cat, bird, dog, etc)
    pet breed (persian, beagle, canary, etc)
    owner name
    owner phone number
    owner email
    owner balance (amount owing)
    date of first visit
    create a program that will allow the user to:
    insert a new record into the database and save it automatically
    retrieve a record by their id and display all of the information
    retrieve a record by the email and display all of the information
    retrieve a record by phone number and display all of the information
    You will need to create the table yourself. Consider what data types you will
    need to use.
    """
    
#def GRAHHHH():
    """
    x1 = input('petname')
    x2 = input('petspecies')
    x3 = input('petbreed')
    x4 = input('ownername')
    x5 = input('ownerphone number')
    x6 = input('owneremail')
    x7 = input('ownerbalance')
    x8 = input('firstvisit')
    """
#while True:
#   print(press 1 to searcpress 2 to)
#   x = int(input("Enter Option:")) 
