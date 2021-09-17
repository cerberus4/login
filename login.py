import getpass
import sqlite3
import sys
from os import system, name
import time
from tabulate import tabulate
from prettytable import PrettyTable

class ls:
    usernameinput = ''
    cur = ''
    def heading():
        h = open('banner.txt','r')   
        lines = h.read()
        print(lines)

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def dbconnect():
        db = sqlite3.connect('logindb.db')
        ls.cur = db.cursor()

    def dbCommitClose():
        db = sqlite3.connect('logindb.db')
        db.commit()
        print('commit')
        db.close()
        print('close')
    
    def dbClose():
        db = sqlite3.connect('logindb.db')
        db.close()

    def addRecord(id, regusername, password,):
        try:
            db = sqlite3.connect('logindb.db')
            cursor = db.cursor()

            sqliteInsert = 'INSERT INTO USERS (id, username, password) VALUES (?, ?, ?);'

            dataTuple = (id, regusername, password)
            cursor.execute(sqliteInsert, dataTuple)
            db.commit()

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
            time.sleep(10)
        finally:
            if db:
                db.close()

    def deleteRecord(id):
        try:
            db = sqlite3.connect('logindb.db')
            cursor = db.cursor()

            sqliteDelete = 'DELETE from USERS where id=?'
            cursor.execute(sqliteDelete, (id,))
            db.commit()

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
            time.sleep(10)
        finally:
            if db:
                db.close()

    def deleteMenu():
        ls.clear()
        ls.heading()

        ls.dbconnect()
        ls.cur.execute('SELECT * FROM USERS')
        listusers = ls.cur.fetchall()
        myTable = PrettyTable(['ID', 'Username', 'Password'])
        for line in listusers:
            myTable.add_row(line) 
        print(myTable)

        print('Enter account id you wish to delete, or type \'back\' to return to menu ')
        entry = input('')

        if entry == 'back':
            ls.logged_in_menu()
        else:
            ls.deleteRecord(entry)
            print('Record number ' + entry + ' successfully deleted. Returning you to main menu.')
            time.sleep(3)
            ls.logged_in_menu()
        

    def main_menu():
        ls.clear()
        ls.heading()
        print('Enter Number to continue:\n--------------------------\n1. Login \n2. Register \n3. Quit')
        entry = input('')

        if entry == '1':
            ls.login_menu()
        elif entry == '2':
            ls.register()
        elif entry == '3':
            print('Quitting application')
            time.sleep(2)
            ls.clear()
            sys.exit
        else:
            print('Error, please try again')
            time.sleep(2)
            ls.main_menu()

    def login_menu():
        ls.clear()
        ls.heading()
        print('1. Login\n--------------------------')
        ls.usernameinput = input('Username: '),
        password = getpass.getpass()
        
        db = sqlite3.connect('logindb.db')
        ls.cur = db.cursor()
        ls.cur.execute('SELECT password from USERS WHERE username = ?', ls.usernameinput)
        pwd = ls.cur.fetchone()
        
        if pwd[0] == password:
            ls.dbClose()
            ls.logged_in_menu()          
        else:
            ls.dbClose()
            print('Incorrect password, returning you to the main menu')
            time.sleep(2)
            ls.main_menu()

    def logged_in_menu():
        ls.clear()
        ls.heading()
        
        print('Welcome ' + ls.usernameinput[0] + ', what would you like to do?\n--------------------------\n1. List Accounts \n2. Delete Account \n3. Log Out \n4. Quit')
        entry = input('')
        if entry == '1':
            ls.list_accounts()
        elif entry == '2':
            ls.deleteMenu()
        elif entry == '3':
            ls.main_menu()
            print('Returning you to the main menu')
            time.sleep(2)
        elif entry == '4':
            print('Quitting application')
            time.sleep(2)
            ls.clear()
            sys.exit
        else:
            print('error')
            ls.logged_in_menu()

    def loggedInList():
        print('What would you like to do?\n--------------------------\n1. List Accounts \n2. Delete Account \n3. Log Out \n4. Quit')
        entry = input('')
        if entry == '1':
            ls.list_accounts()
        elif entry == '2':
            ls.deleteMenu()
        elif entry == '3':
            ls.main_menu()
            print('Returning you to the main menu')
            time.sleep(2)
        elif entry == '4':
            print('Quitting application')
            time.sleep(2)
            ls.clear()
            sys.exit
        

    def register(): 
        ls.clear()
        ls.heading()
        print('1. Register New User\n--------------------------')
        regusername = input('Username: '),
        
        #check to see if username exists
        ls.dbconnect()        
        ls.cur.execute('SELECT * from USERS WHERE username = ?', regusername)
        
        if ls.cur.fetchone() == None:
            ls.cur.execute('SELECT COUNT(*) FROM USERS')
            count = ls.cur.fetchone()
            plus1 = int(count[0] + 1)
            regpassword = getpass.getpass()
            pwdcheck = getpass.getpass('Confirm Password: ')
            if regpassword == pwdcheck:
                ls.addRecord(plus1, regusername[0], regpassword)
                print('\n Welcome ' + regusername[0] + ', you can now log in at the main menu')
                time.sleep(2)
                ls.main_menu()
            else:
                print('Passwords do not match, redirecting you to the main menu') 
                time.sleep(2)
                ls.main_menu()
        #username taken
        else:
            print('Username taken please try another one')
            time.sleep(2)
            ls.register()
    
    def list_accounts():
        ls.clear()
        ls.heading()
        ls.dbconnect()
        ls.cur.execute('SELECT * FROM USERS')
        listusers = ls.cur.fetchall()
        myTable = PrettyTable(['ID', 'Username', 'Password'])
        for line in listusers:
            myTable.add_row(line) 
        print(myTable)
        ls.loggedInList()
        
'''
#main menu prompt
def main_menu():
    clear()
    #print heading from text file
    heading()
    print('Enter Number to continue:\n--------------------------\n1. Login \n2. Register \n3. Quit')
    entry = input('')
    if entry == '1':
        login.login_menu()
    elif entry == '2':
        register()
    elif entry == '3':
        print('Quitting application')
        time.sleep(2)
        clear()
        sys.exit
    else:
        print('error')
        main_menu()
#login menu
class login:
    usernameinput = ''

    def login_menu():
        #cls screen
        clear()
        #print heading from text file
        heading()
        print('1. Login\n--------------------------')
        login.usernameinput = input('Username: '),
        password = getpass.getpass()
        
        db = sqlite3.connect('logindb.db')
        cur = db.cursor()
        cur.execute('SELECT password from USERS WHERE username = ?', login.usernameinput)
        pwd = cur.fetchone()
        if pwd[0] == password:
            db.close  
            login.logged_in_menu()          
        else:
            db.close
            print('Incorrect password, returning you to the main menu')
            time.sleep(2)
            main_menu()

    def logged_in_menu():
        clear()
        #print heading from text file
        heading()
        print('Welcome ' + login.usernameinput[0] + ', what would you like to do?\n--------------------------\n1. List Accounts \n2. Delete Account \n3. Quit')
        entry = input('')
        if entry == '1':
            list_accounts()
        elif entry == '2':
            register()
        elif entry == '3':
            print('Quitting application')
            time.sleep(2)
            clear()
            sys.exit
        else:
            print('error')
            main_menu()

def list_accounts():
    clear()
    #print heading from text file
    heading()
    print(usernameinput[0] ' , what would you like to do?\n--------------------------\n1. List Accounts \n2. Delete Account \n3. Quit')
    db = sqlite3.connect('logindb.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM USERS')
    listusers = cur.fetchall()
    myTable = PrettyTable(['ID', 'Username', 'Password'])
    for line in listusers:
        myTable.add_row(line) 
    print(myTable)
    print(usernameinput[0] ' , what would you like to do?\n--------------------------\n1. List Accounts \n2. Delete Account \n3. Quit')
    ###################
    entername = input('enter name')
    del_accounts()

def del_accounts(list_accounts):
    db = sqlite3.connect('logindb.db')
    cur = db.cursor()
    sql = 'DELETE FROM USERS WHERE id=?'
    cur.execute('SELECT * from USERS WHERE username = ?', regusername)
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    print(list_accounts.entername)
#registration menu
def register(): 
    #cls screen
    clear()

    #print heading from text file
    heading()
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

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
'''


ls.main_menu()
#ls.deleteRecord(2)

'''
CREATE TABLE USERS(
	id INT PRIMARY KEY NOT NULL,
	username TEXT NOT NULL,
	password TEXT NOT NULL
);
'''