def firstAndLastElement(list):
    return [list[0],list[len(list)-1]]

list= input("Give me a sequence of numbers:").split()

print(firstAndLastElement(list))