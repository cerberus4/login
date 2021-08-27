
import getpass
def login():
    print('Enter Number to continue:\n--------------------------\n1. Login \n2. Register')
    entry = input
    username = input('Username:')

    password = getpass.getpass()

    print(username)
    print(password)

#Form Tutor Management System
import sys #this allows you to use the sys.exit command to quit/logout of the application
def main():
    login()

    
#the program is initiated, so to speak, here
main()