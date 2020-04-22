import random

counter =0

while True:
 number = random.randint(1,9)
 
 guess = input("Guess a number between 1 and 9:")
 
 if(guess=="exit"):
     print("Guesses: "+str(counter))
     break
 
 counter += 1
 guess = int(guess)
 if(guess==number):
    print("Right!")
 elif(guess<number):
    print("Too low!")
 else:
    print("Too high!")
 
 