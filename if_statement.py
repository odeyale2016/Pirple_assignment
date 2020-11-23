''''
Program to check the equality of two or more numbers
'''
def checkVals(a,b,c):
    if (int(a)==int(b) or int(b)==int(c) or int(a) == int(c)):
       return True
    else:
        return False

val1=checkVals(4,5,"3")
val2=checkVals(3,2,2)
val3=checkVals(7,"7",5)
val4= checkVals(6,6,6)
print(val1)
print(val2)
print(val3)
print(val4)