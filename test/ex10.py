import random


list1 = random.sample(range(10),random.randint(0,10))
list2 = random.sample(range(10),random.randint(0,10))

print(list1)
print(list2)

intersection = [x for x in list1 if x in list2]

print("intersection:" + str(intersection))


list3=[1,2,2,3]
list4=[1,2]

print([x for x in set(list3) if x in list4])