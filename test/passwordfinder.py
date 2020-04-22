import random
import string 

eingabe = input("Give me a random string:")

while True:
    
    length = random.randint(1,10)
    
    charList= list(string.ascii_letters) + list(range(0,10)) + ['!','?']

    password =""

    for i in range(length):
       password = password + str(random.choice(charList))

    print(password)

    if(password==eingabe):
        break 
        
print("I have found it!")