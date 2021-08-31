import getpass
import sqlite3
import sys
import subprocess
import time

#main menu prompt
def main_menu():
    subprocess.run(['clear'], shell=True)

    #print heading from text file
    h = open('banner.txt','r')   
    lines = h.read()
    print(lines)
    print('Enter Number to continue:\n--------------------------\n1. Login \n2. Register \n3. Quit')
    entry = input('')
    if entry == '1':
        login()
    elif entry == '2':
        register()
    elif entry == '3':
        print('Quitting application')
        time.sleep(2)
        subprocess.run(['clear'], shell=True)
        sys.exit
    else:
        print('error')
        main_menu()
#login menu
def login():
    #clear screen
    subprocess.run(['clear'], shell=True)

    #print heading from text file
    h = open('banner.txt','r')   
    lines = h.read()
    print(lines)
    print('1. Login\n--------------------------')
    usernameinput = input('Username: '),
    password = getpass.getpass()
    
    db = sqlite3.connect('logindb.db')
    cur = db.cursor()
    cur.execute('SELECT password from USERS WHERE username = ?', usernameinput)
    pwd = cur.fetchone()
    if pwd[0] == password:
        print('welcome')
        db.close
    else:
        db.close
        print('Incorrect password, returning you to the main menu')
        time.sleep(2)
        subprocess.run(['clear'], shell=True)
        main_menu()

#registration menu
def register(): 
    #clear screen
    subprocess.run(['clear'], shell=True)

    #print heading from text file
    h = open('banner.txt','r')   
    lines = h.read()
    print(lines)
    print('1. Register New User\n--------------------------')

    #enter desired username
    regusername = input('Username: '),
    #connect to database
    db = sqlite3.connect('logindb.db')
    cur = db.cursor()
    #check to see if username exists
    cur.execute('SELECT * from USERS WHERE username = ?', regusername)
    #username free
    if cur.fetchone() == None:
        cur.execute('SELECT COUNT(*) FROM USERS')
        count = cur.fetchone()
        plus1 = int(count[0] + 1)
        regpassword = getpass.getpass()
        pwdcheck = getpass.getpass('Confirm Password: ')
        if regpassword == pwdcheck:
            data_tuple = plus1, regusername[0], regpassword
            cur.execute('INSERT INTO USERS (id, username, password) VALUES (?, ?, ?)', data_tuple)
            db.commit()
            db.close()
            print('\n Welcome ' + regusername[0] + ', you can now log in at the main menu')
            time.sleep(2)
            main_menu()
        else:
            print('Passwords do not match, redirecting you to the main menu') 
            time.sleep(2)
            main_menu()
    #username taken
    else:
        print('Username taken please try another one')
        time.sleep(2)
        register()
    #cur.execute("INSERT INTO USERS VALUES (1, 'John >> Doe' , ' john.doe@xyz.com' , 'A')")
    #enter username
    #check if free
    #regpassword = input('Enter dsired password')
    #pwdcheck = input('Re enter password')
    #enter password

    #count total names in user table
    #add 1 to the total and use as primary key





main_menu()

'''
CREATE TABLE USERS(
	id INT PRIMARY KEY NOT NULL,
	username TEXT NOT NULL,
	password TEXT NOT NULL
);
'''