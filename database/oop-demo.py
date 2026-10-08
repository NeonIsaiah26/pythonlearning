from object_life_cycle2 import Absents

x = Absents()

def myfunc(x):
    y = x + 1
    return x + 2

y = myfunc(5)

print(y)