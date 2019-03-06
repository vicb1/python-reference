import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 4, 7]})

import collections

c = collections.Counter()
print ('Initial :', c)

l = [1, 5 ,3,4,1]
c.update(l)
print ('Sequence:', c)
c.update({'a':1, 'd':5})
print ('Dict    :', c)
c.update([5,5,5,5])
print ('Dict    :', dict(c))
c.clear()

print(l.count(1))

print(list('UDDDUDUU'))

print ('12345'[:])

l2 = [44,6,7,8, 5]

print('set: ', list(set(['3', '4']) & set('1234')))
print(len(l2))

# *n is the number of things to choose from, and we choose r of them

# PERMUTATIONS (order matters)
#   Repetition is Allowed: such as the lock above. It could be "333". ### = n^r
#   No Repetition: for example the first three people in a running race. You can't be first and second. ###n!/(n − r)!

# COMBINATIONS (order doesn't matter)
#   Repetition is Allowed: such as coins in your pocket (5,5,5,10,10) ### (r+n-1)!/(r!*(n − 1)!)
#   No Repetition: such as lottery numbers (2,14,15,27,30,33) ### n!/(r!*(n − r)!)

import math
f = math.factorial
def permutation_repetition(n, r): # such as a lock, it could be "333"
    return n^r

def permutation_no_repetition(n, r): # for example the first three people in a running race. You can't be first and second.
    return f(n)/f(n-r)

def combination_repetition(n, r):  # such as coins in your pocket (5,5,5,10,10)
    return f(r+n-1)/(f(r)*f(n-1))

def combination__no_repetition(n, r):  # such as lottery numbers (2,14,15,27,30,33)
    return f(n)/(f(r)*f(n-r))

print('ans = ' + str(permutation_no_repetition(13, 3)))

print('12345'[10%5:]+'12345'[:10%5])

l3 = list('12345')
l3.insert(6, '2')
print(l3)

l4 = l3[:]
l4.sort()
print(l4)

someddict = collections.defaultdict(int)
print('default dict: ', someddict[3]) # print int(), thus 0
