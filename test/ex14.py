def removeDuplicatesSet(eingabe):
    return list(set(eingabe))

def removeDuplicatesLoop(list):
    result=[]
    for x in list:
        if(x not in result):
            result.append(x)
    return result



print(removeDuplicatesSet([1,2,2,3,3,4]))
print(removeDuplicatesLoop([1,2,2,3,3,4]))