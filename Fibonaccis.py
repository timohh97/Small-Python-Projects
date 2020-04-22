def getFibonacciAt(index):
    if(index==1):
        return 1
    if(index==2):
        return 1 
    return getFibonacciAt(index-1)+getFibonacciAt(index-2)

def generateFibonaccis(number):
    return [getFibonacciAt(x) for x in range(1,number+1)]
    
number = int(input("How many Fibonaccis do you want to print?:"))

print(generateFibonaccis(number))