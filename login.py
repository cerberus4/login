import getpass
import sqlite3
import sys

def menu():
    print('Enter Number to continue:\n--------------------------\n1. Login \n2. Register \n3. Quit')
    entry = input('')
    if entry == '1':
        login()
    elif entry == '2':
        print('register')
    elif entry == '3':
        print('quitting application')
        sys.exit
    else:
        print('error')
        menu()

def login():
    
    usernameinput = input('Username:')
    username = usernameinput,
    password = getpass.getpass()
    
    con = sqlite3.connect('logindb.db')
    cur = con.cursor()
    cur.execute('SELECT password from USERS WHERE username = ?', username)
    pwd = cur.fetchone()
    if pwd[0] == password:
        print('welcome')
    else:
        print('Returning you to menu')
        menu()

def register():
    print('Enter desired username')
    #enter username
    #check if free
    #enter password
    #count total names in user table
    #add 1 to the total and use as primary key
    


#test change
#the program is initiated, so to speak, here
menu()

'''
CREATE TABLE IF NOT EXISTS Login(
    Username TEXT,
    Password TEXT
);
'''