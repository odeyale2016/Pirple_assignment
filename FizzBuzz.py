numbers=range(1,100)

for number in numbers:
    if ((number % 3 == 0) and (number % 5== 0)):
        print(number)
        print("FizzBuzz")
        
    elif(number % 5 == 0):
        print(number)
        print("Buzz")
         
    elif(number % 3 == 0 ):
        print(number)
        print("Fizz")
         
    elif((number % number) == 0 and (number % 1 == 0)):
        print(number)
        print("prime")
        
