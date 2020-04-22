number=int(input("Give me a number!"))


if(number%4==0):
    print("number is a multiple of 4")
elif(number%2==0):
    print("even number")
elif(number%2==1):
    print("odd number")

num= int(input("Give me a second number!"))
check= int(input("Give me a third number!"))

if(num%check==0):
    print(str(num)+ " is a multiple of " +str(check))
else:
    print(str(num)+ " is not a multiple of " +str(check))