from doctest import master
from lib2to3.pgen2 import token
from cryptography import fernet
from cryptography.fernet import Fernet

#Making an encryption key but then commented out so it doesn't reset everytime
'''
def make_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():

    #Opening file in read mode to get the original encryption key
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


mst_pwd = input("What is the master password? ")

#Converting master password into bytes and then combining it with the encryption key and then initializing it in Fer
key = load_key()
fer = Fernet(key)


def view():
    if mst_pwd == "master":
        #w mode will create/override a file. r mode will read the file. a mode allows you to add something to the end of the file or create one if it doesn't exist
        with open('password.txt', 'r') as f:

            #for every line there is in the txt file, it will print it in the terminal
            for line in f.readlines():
           
                #r.strip gets rid of any new lines and seperates them into a list. Assign the variables to positions on that list and print
                data = line.rstrip()
                user, passwd = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(passwd.encode()).decode())
    else:
        print("There is no information associated with that passowrd or you have entered it incorrectly. Please quit and try again")
        

def add():

    name = input('Account Username: ')
    password = input("Password: ")

    #w mode will create/override a file. r mode will read the file. a mode allows you to add something to the end of the file or create one if it doesn't exist
    with open('password.txt', 'a') as f:
        
        #Takes the username and password and creates a text file. It will add new passwords and users on different line as well
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:

    mode = input("Would you like to add a new password or view your previous ones (view, add)? or Press q to quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Input")
        continue
