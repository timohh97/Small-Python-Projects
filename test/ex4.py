number = int(input("Give me a number!"))

result =[]

for i in range(1,number+1):
   if(number%i==0):
     result.append(i)


print(result)