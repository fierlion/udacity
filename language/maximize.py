# Bonus Practice: Find Max
# Given a list l and a function f, return the element of l that maximizes f.
sentenceIn = "Barbara Kingsolver wrote the Poisonwood bible"
l = sentenceIn.split(" ")
f = len

#first, display the formatted array of words
print '[',
for i in range(len(l)-1):
    print l[i] + ',',
print l[len(l)-1] + ' ]'

#lenths is a list of string lengths in l
lengths = [len(string) for string in l]

# lengthSorted uses list comprehension and zip to sort one list by another,
#here it sorts l by the integer values in lengths, lagest to smallest
lengthSorted = [x for (y,x) in sorted(zip(lengths,l), key=lambda pair: pair[0], reverse=True)]

print "Maximized by length:"
print lengthSorted[0]
#but... we have two strings of the same length.  
#How do we decide which is the MVS (Most Valuable String)

print "------------"

#here's another which uses the ordinal number of each char
#to compare by totalling character values.
bestSoFar = 0
bestWord = ""
for word in l:
    total = 0
    for letter in word:
        total += ord(letter)
    if total >= bestSoFar:
        bestSoFar = total
        bestWord = word

print "Maximized by ordinal value"
print bestWord


