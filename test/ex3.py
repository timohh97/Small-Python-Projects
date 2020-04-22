string =input("Gebe eine Folge von Zahlen ein, getrennt durch ein Leerzeichen!")

list = string.split()

result_list= []

for i in list:
    if(int(i)<5):
      result_list.append(i)


print(result_list)



number= int(input("Bitte gib mir eine Zahl!"))

result_list= []

for i in list:
    if(int(i)<number):
      result_list.append(i)


print(result_list)