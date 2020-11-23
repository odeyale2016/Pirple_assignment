
#3 SET
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
setA={1,3,5}
u = odds.union(evens)

i = evens.intersection(primes)
d = odds.difference(primes)
s = evens.symmetric_difference(primes)
odds.update(evens)
# print(setA.issubset(odds))
# print(odds.issuperset(setA))
# print(odds.isdisjoint(evens))
# #odds.difference_update(evens)
# print(odds)
# #print(setB)
# #print(setC)
# # print(i)
# # print(u)
# # print(d)
# # print(s)

# setB=setA
# setB=setA.copy()

# setB.add(7)
# print(setB)
# print(setA)

# FROZEN SET3 
# a = frozenset(odds)

# a.add(9) # This will give errors
# print(a)

#4 STRINGS: Ordered, immutable, text representation
# my_string="Hello World"
# char=my_string[0:5]  #Slicing
# char2=my_string[::-1]
# print(char2)

# STRIP METHOD
my_string='     HELLO WORLD   '
new_string = "Welcome to Python World"
my_string=my_string.strip()
print(my_string.lower())
print(my_string.startswith('H'))
print(my_string.endswith('He'))
my_list=new_string.split()
print(my_list)
my_list1=' '.join(my_list)
print(my_list1)

str1=['a'] * 6
print(str1)
str2=''.join(str1)
print(str2)
