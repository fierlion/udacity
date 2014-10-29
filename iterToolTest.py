import itertools

houses = [1,2,3]
orderings = list(itertools.permutations(houses))

def nextTo(ob1, ob2):
    "Object ob1 is immediately next to ob2"
    return abs(h1 - h2) == 1

for (red, green, blue) in orderings:
    for (hot, hotter, hottest) in orderings:
        #print (red == hottest) #'==' checks for same value
        print (red is hottest) # checks for same Object
