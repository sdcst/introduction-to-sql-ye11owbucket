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
    petname = input("Enter Pet Name: ")
    petspecies = input("Enter Species ")
    petbreed = input("Enter Breed: ")
    ownername = input("Enter Owner Name: ")
    ownerphonenumber = input("Enter Phone Number: ")
    owneremail = input("Enter Email: ")
    ownerbalance = float(input("Enter Balance: "))
    firstvisit = input("Enter time of first visit")
    list = [petname, petspecies, petbreed, ownername, ownerphonenumber, owneremail, ownerbalance, firstvisit]
    query = f"insert into pet (petname, petspecies, petbreed, ownername, ownerphonenumber, owneremail, ownerbalance, firstvisit) values ('{list[0]}','{list[1]}','{list[2]}','{list[3]}','{list[4]}','{list[5]}','{list[6]}','{list[7]}')"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def readid(x):
    query = f'select * from pet where id={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readname(x):
    query = f'select * from pet where petname={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readspec(x):
    query = f'select * from pet where petspecies={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readbreed(x):
    query = f'select * from pet where petbreed={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readownname(x):
    query = f'select * from pet where ownername={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readphone(x):
    query = f'select * from pet where ownerphonenumber={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)
    
def reademail(x):
    query = f'select * from pet where owneremail={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readbal(x):
    query = f'select * from pet where ownerbalance={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

def readvisit(x):
    query = f'select * from pet where firstvisit={x}'
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)






for __name__ in "__main__":
    while True:
        print("press 1 to add new pet\npress 2 to get pet info\npress anything else to exit")
        y = input("Enter:")
        if y == '1':
            addition()
        if y == '2':
            print("1 for Pet Name\n2 for id\n3 for phone number")
            x = str(input("Enter: "))
            if x == '1':
                i = input("Enter Pet Name: ")
                readname(i)
            if x == '2':
                i = input("Enter Owner Name: ")
                readownname(i)
            if x == '3':
                i = input("Enter Phone #: ")
                readphone(i)

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
