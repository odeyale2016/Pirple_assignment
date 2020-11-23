odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)

i = evens.intersection(primes)
d = odds.difference(primes)
s = evens.symmetric_difference(primes)
odds.update(evens)
#odds.difference_update(evens)
# print(odds)
#print(setB)
#print(setC)
# print(i)
# print(u)
# print(d)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)
print(diff)