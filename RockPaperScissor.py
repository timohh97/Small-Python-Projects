import os

flag = True

while flag:
 string1 = input("Player 1 rock, paper or scissor?:")
 while(string1!="rock" and string1!="paper" and string1!="scissor"):
    string1 = input("Player 1 rock, paper or scissor?:")

 os.system('cls')

 string2 = input("Player 2 rock, paper or scissor?:")
 while(string2!="rock" and string2!="paper" and string2!="scissor"):
    string2 = input("Player 2 rock, paper or scissor?:")

   
 if(string1==string2):
        print("Draw!")    
 elif(string1=="rock"):
        if(string2=="paper"):
               print("Player 2 wins!")
        else:
               print("Player 1 wins!")
 elif(string1=="paper"):
        if(string2=="scissor"):
               print("Player 2 wins!")
        else:
               print("Player 1 wins!")
 elif(string1=="scissor"):
        if(string2=="rock"):
               print("Player 2 wins!")
        else:
               print("Player 1 wins!")
 
 

        
 eingabe = input("Wanna play again? Type y or n:")
 while(eingabe!="y" and eingabe!="n"):
        eingabe = input("Wanna play again? Type y or n:")
 if(eingabe=="n"):
     print("Game Over")
     flag = False
 else:
        print("Next Round")

    
    




