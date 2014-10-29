import string

table = string.maketrans('ABC', '123')
f = 'A + B == C'

translated = f.translate(table)
#translated is now magically '1 + 2 == 3'
#print translated
#print eval(translated)

f2 = '1 + 5 == 5'
f3 = '01 + 05'
f4 = '5 / 0 == 1'

def valid (formulaIn):
    """Formula formulaIn is vaid iff it has no numbers
    with leading zeros and evals true"""
    try:
        fixedForm = zeroCheck(formulaIn)
        print fixedForm
        return eval(fixedForm)
    except ZeroDivisionError:
        return False

def zeroCheck(formulaIn):
    zeroArr = formulaIn.split(" ")
    for i in range(len(zeroArr)):
        if zeroArr[i] != '0' and zeroArr[i][0] == '0':
            zeroArr[i] = zeroArr[i][1:]
    return "".join(zeroArr)

print valid(translated)
print valid(f2)
print valid(f3)
print valid(f4)
