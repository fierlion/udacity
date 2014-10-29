import string

table = string.maketrans('ABC', '123')
f = 'A + B == C'
print f.translate(table)
