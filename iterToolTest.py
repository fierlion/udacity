import itertools
import time

houses = [1,2,3]
orderings = list(itertools.permutations(houses))

def nextTo(ob1, ob2):
    "Check if Object ob1 is immediately next to ob2"
    return abs(ob1 - ob2) == 1

for (red, green, blue) in orderings:
    for (hot, hotter, hottest) in orderings:
        #print (red == hottest) #'==' checks for same value
        #print (red is hottest) #'is' checks for same Object
        print nextTo(red, hottest)

def sq(x):
    return x * x

#__________________________________________________

#generator expression tests
for x2 in (sq(x) for x in range(10) if x%2 == 0):
    print x2

gList = list((sq(x) for x in range(10) if x%2 != 0))
print gList

#check function runtime
def timedCall(fn, *args):
    "Call function with args, return time in seconds and result"
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

#_____________________________________________

# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    
def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    for i in ints(0):
        if i == 0: yield i
        else:
            yield i
            yield i * -1

#test generator function
x = all_ints()
for i in range(50):
    print x.next()
