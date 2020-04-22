eingabe = input("Give me a sentence:")

stringList= eingabe.split()

stringList=reversed(stringList)

print(" ".join(stringList))