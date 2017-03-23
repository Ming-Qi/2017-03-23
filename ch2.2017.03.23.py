from functools import partial

# by convention, we give classes PascalCase names
class Set:
 # these are the member functions
 # every one takes a first parameter "self" (another convention)
 # that refers to the particular Set object being used
 def __init__(self, values=None):

    s1 = Set() # empty set
    s2 = Set([1,2,2,3]) # initialize with values"""
    self.dict = {} # each instance of Set has its own dict property
 # which is what we'll use to track memberships
    if values is not None:
        for value in values:
            self.add(value)
def __repr__(self):
    return "Set: " + str(self.dict.keys())
# we'll represent membership by being a key in self.dict with value True
def add(self, value):
    self.dict[value] = True
 # value is in the Set if it's a key in the dictionary
def contains(self, value):
    return value in self.dict
def remove(self, value):
    del self.dict[value]






def exp(base, power):
 return base ** power
def two_to_the(power):
 return exp(2, power)

square_of = partial(exp, power=2)
print square_of(3)


def double(x):
    return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
print twice_xs
twice_xs = map(double, xs) # same as above
print twice_xs

list_doubler = partial(map, double) # *function* that doubles a list
print list_doubler
twice_xs = list_doubler(xs) # again [2, 4, 6, 8]
print twice_xs

def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]

x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24

print x_product

documents = ["aa","bb","cc"]
