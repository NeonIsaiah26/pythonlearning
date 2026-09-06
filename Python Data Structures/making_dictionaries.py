def dict_sample():
    cabinet = dict()
    cabinet['A'] = 'Apple'
    cabinet['B'] = 'Banana'
    cabinet['C'] = 'Cherry'

    lst = list()
    lst.append('Apple')
    lst.append('Banana')
    lst.append('Cherry')


# many counters with a dictionary
def dict_counter(word1, word2, word3):
    counts = dict()
    counts[word1] = 1
    counts[word2] = 1
    counts[word3] = 1
    counts[word1] = counts[word1] + 1
    return counts


# When we see a new name

def dict_counter2():
    counts = dict()
    counts['Ken'] = 1
    counts['Erd'] = 1
    counts['Thelma'] = 1
    counts['Neon'] = 1
    names = ['Ken', 'Erd', 'Thelma', 'Neon', 'Gerald']
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    print(counts)


# Simplified counting with get() method
def using_get():
    counts = dict()
    counts['Ken'] = 1
    counts['Erd'] = 1
    counts['Thelma'] = 1
    counts['Neon'] = 1
    names = ['Ken', 'Erd', 'Thelma', 'Neon', 'Gerald']
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    print(counts)

dict_counter2()
using_get()
    
