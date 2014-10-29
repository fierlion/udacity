import itertools

houses = [1,2,3]
orderings = list(itertools.permutations(houses))

for (red, green, blue) in orderings:
    for (hot, hotter, hottest) in orderings:
        print (red == hottest)
