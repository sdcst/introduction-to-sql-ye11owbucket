#!python

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
import sqlite3
file = 'dbz.db'
connection = sqlite3.connect(file)
print(connection)
cursor = connection.cursor()
query = """
CREATE TABLE if not exists dbz.db.pet (
    id integer primary key,
    petname text,
    petspecies text,
    petbreed text,
    ownername text,
    ownerphonenumber text,
    owneremail text,
    ownerbalance text,
    firstvisit text,
    cnum int);
"""
cursor.execute(query)


def GRAHHHH():
    x1 = input('petname')
    x2 = input('petspecies')
    x3 = input('petbreed')
    x4 = input('ownername')
    x5 = input('ownerphone number')
    x6 = input('owneremail')
    x7 = input('ownerbalance')
    x8 = input('firstvisit')


#while True:
#   print("press 1 to search\npress 2 to ")
#   x = int(input("Enter Option:")) 