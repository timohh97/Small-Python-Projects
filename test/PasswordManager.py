import sys
import random
import string

def start():
 master = input("Enter the master password (Type exit for exit):")
 while(master!="test" and master!="exit"):
    master = input("Enter the master password (Type exit for exit):")

 if(master=="exit"):
    sys.exit()


 print("Welcome to your password manager!")

 string2 = input("Do you want to create or see a password? Type create or see:")
 while(string2!="create" and string2!="see" and string2!="exit"):
    string2 = input("Do you want to create or see a password? Type create or see:")

 if(string2=="exit"):
    sys.exit()

 if(string2=="create"):
    createPassword()


def createPassword():
    description=input("Type description for password usage:")
    print("The generated password is: "+str(generatePassword()))


    


def generatePassword():
    length = random.randint(8,12)
    charList= list(string.ascii_letters) + list(range(0,10)) + ['!','?']
    password =""
    for i in range(length):
       password = password + str(random.choice(charList))
    return password


start()



