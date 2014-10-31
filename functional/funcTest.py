#tests modified from: https://thenewcircle.com/static/bookshelf/python_fundamentals_tutorial/functional_programming.html

def iAmObject(argIn):
    return argIn

print iAmObject("Object")

iAmOtherObject = iAmObject

print iAmOtherObject("Other Object")

#Objects are the same
print "Object Locations:"
print "Object@" + str(iAmObject)
print "Other Object@" + str(iAmOtherObject)
print("........")

#pass function in as first-class object
print iAmObject(iAmOtherObject)
print("........")

#a function as argument
comps = [('Bach','Goldberg Variations'), ('Prokofyev', 'Romeo and Juliet'),
         ('Brahms', 'German Requiem'), ('Beethoven', 'Diabelli Variations')]

def secondEl(tupleIn):
    return tupleIn[1]

print "sorted (by default, [0]): ", sorted(comps)
print "sorted (by second,  [1]): ", sorted(comps, key=secondEl)
print("........")

#lambdas
def callFunc(f, *args):
    return f(*args)

print "calling: lambda x, y: x + y, 4, 5"
print callFunc(lambda x, y: x + y, 4, 5)
print("........")

#function scope
def outer():
    def inner(argIn):
        return argIn
    return inner

function1 = outer()
print function1
print function1("Inner")
