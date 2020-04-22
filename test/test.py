import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def serialize(node):
     if(node.left==None and node.right==None):
        return node.val+'(none,none)'
     elif (node.left==None):
      return node.val+'(none,'+serialize(node.right)+')'
     elif (node.right==None):
      return node.val+'('+serialize(node.left)+',none)'
     else:
      return node.val+'('+serialize(node.left)+','+serialize(node.right)+')'

def deserialize(string):   

    if(string=='none'):
       return None
    
    rightBracketIndex=len(string)-1
    leftBracketIndex=string.find('(')
    
    endBracketCounter=0

    for i in range(len(string)-1,0)
      if(string[i]==')'):
        endBracketCounter++
      else:
        break
    
    
    


    return Node(string[0:leftBracketIndex],Node(deserialize(string[leftBracketIndex+1,commaIndex])),Node(deserialize(string[commaIndex+1,rightBracketIndex])))



node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
#assert deserialize(serialize(node)).left.left.val == 'left.left'


