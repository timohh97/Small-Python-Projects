import random
import string 

while True:

    eingabe= input("Do you want a new password? Type y or n:")
    while(eingabe!="y" and eingabe!="n"):
        eingabe= input("Do you want a new password? Type y or n:")
    
    if(eingabe=="n"):
        break
    
    length = random.randint(8,12)
    
    charList= list(string.ascii_letters) + list(range(0,10)) + ['!','?']

    password =""

    for i in range(length):
       password = password + str(random.choice(charList))

    print(password)
    

    
        
          

