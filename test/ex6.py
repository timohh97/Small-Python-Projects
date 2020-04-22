string = input("Give me a string!")

def isPalindrom(string):
    if(len(string)==0):
      return True

    if(string[0]==string[len(string)-1]):
        return isPalindrom(string[1:len(string)-1])


print(isPalindrom(string))


