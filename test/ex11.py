def isPrime(number):
    if(number==0 or number==1):
        return False

    for i in range(2,number):
        if(number%i==0):
            return False
    return True
 

primeNumbers=[x for x in range(0,1000) if isPrime(x)]

print(primeNumbers)