import string, re

string1 = "ABC123"
string2 = "Abc123ABC"
string3 = "QWERTYUIOPADFGHJKLZXCVBNM!@#$%^&*()"

def isAlpha(stringIn):
    #alphaRegex = ur"[A-Za-z]*" #for "ABC123" returns ['ABC', '', '', '']
    alphaRegex = ur"[A-Za-z]"
    #a-ha! the way to rule out repeats is by stuffing it all in a set!
    #return "".join(re.findall(alphaRegex, stringIn))
    return "".join(set(re.findall(alphaRegex, stringIn)))


print isAlpha(string1)
print isAlpha(string2)
print isAlpha(string3)
