myUniqueList=[]
myLeftovers=[]
def addNewElement(e):
    if (e not in myUniqueList):
        myUniqueList.append(e)
        return True
    else:
        myLeftovers.append(e)
        return False

val1=addNewElement(5)
val2= addNewElement(3)
val3= addNewElement(4)
val4= addNewElement(2)
val5= addNewElement(3)

print(val1)
print(val2)
print(val3)
print(val4)
print(val5)
print(myUniqueList)
print(myLeftovers)

