def sort_array(source_array):
    if(len(source_array)==0):
       return source_array
       
    oddnumbers = [n for n in source_array if n%2!=0]
    oddnumbers.sort()

    for i in range(len(source_array)):
       if(source_array[i]%2!=0):
          source_array[i]='odd'
    
    for n in oddnumbers:
       for i in range(len(source_array)):
          if(source_array[i]=='odd'):
             source_array[i]=n
             break
     
    return source_array


string = input("Give me a list of odd and even numbers (seperated by comma):")
stringArray = string.split(",")

numbers = [int(x) for x in stringArray]

print(sort_array(numbers))
