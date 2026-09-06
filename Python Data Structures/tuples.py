# short tuple examples
def tuple_example():
    x = ("apple", "banana", "grapes","orange")
    x = (x[2])
    print(x)

# tuple basics
def tuple_basics(my_string, my_string2):
    (x, y) = (my_string, my_string2)
    print(y)

# tuples and dictionaries
def tuple_dict():
    d = dict()
    d['neon'] = 2
    d['erd'] = 4
    for (k, v) in d.items():
        print(k, v)
    tuples = d.items()
    print(tuples)

#tuples are comparable (<, >, =)

# Sorting list of tuples (Can put the value more than once but cant put the same key more than once)
# Key order not value order 
def tuple_sort():
    d = {'a':10, 'c':22, 'b':1 }
    d.items()
    d = sorted(d.items())
    print(d)

# Sorting by value 
def value_sort():
    c = {'a':10, 'c':22, 'b':1 }
    tmp = list()
    for k, v in c.items():
        tmp.append((v, k))
    print(tmp)
    tmp = sorted(tmp, reverse=True)
    print(tmp)

# SHORT version
def short_tuple():
    c = {'a':10, 'c':22, 'b':1 }
    print(sorted([(v,k) for k,v in c.items()]))

short_tuple()

