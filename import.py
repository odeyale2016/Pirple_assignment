#import random

# randInt = random.randint(1,20)
# randFloat =random.random()
# randonUniform =random.uniform(1,10)
# print(randInt)
# print(randFloat)
# print(randonUniform)

# simpleList =[1,2,5,6,3,10,11,12,15]
# pickElement = random.choice(simpleList)
# print(pickElement)
# print(simpleList)
# random.shuffle(simpleList)
# print(simpleList)

# # TIME Library
# import time
# print("Hello World")
# print("just wait for 2s...")
# time.sleep(2)
# print("Oh! Welcome")

# sum=0
# for i in range(1,8):
#     sum+=1
#     print(sum)
#     time.sleep(2)

# MATH Library
# import math
# val = 5
# newVal = 3.455
# fact=math.factorial(val)
# newFloor=math.floor(newVal)
# print(fact)
# print(newFloor)

# from random import randint

# randVal = randint(1,100)

# while(True):
#     guess = int(input("Enter your guess: "))
#     if guess == randVal:
#         break
#     elif guess < randVal:
#         print("Your guess is too low")
#     else:
#         print("Your guess is too high")
# print("You guess right, Good Job!")

from random import random
 
randVal = random()
 
upper = 1.0
lower = 0.0
while(True):
    guess = (upper + lower)/2
    if guess == randVal:
        break
    elif guess < randVal:
        lower = guess
    else:
        upper = guess
 
print(guess)


