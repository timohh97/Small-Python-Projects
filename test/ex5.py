import random

eingabe = input("Gib mir eine Ziffernfolge getrennt durch Leerzeichen:")
eingabe2 = input("Gib mir eine Ziffernfolge getrennt durch Leerzeichen:")

list = eingabe.split()
list2 = eingabe2.split()



def listIntersection(list1,list2):
 intersection =[]
 for i in list1:
    if(i in list2):
       intersection.append(i)
 return set(intersection)



print(listIntersection(list,list2))


number1 = random.randrange(0,1000)
number2 = random.randrange(0,1000)

k1 = random.randrange(0,number1)
k2 = random.randrange(0,number2)



randlist1= random.sample(range(0,number1),k1)
randlist2 =random.sample(range(0,number2),k2)

print(listIntersection(randlist1,randlist2))
    

