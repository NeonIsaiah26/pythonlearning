# new lesson
def dict_test3():
    counts = dict()
    inp = input("Enter a line of text: ")
    words = inp.split()
    print("Words: \n" + str(words) + "\n")
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print("Counts: \n" + str(counts) + "\n")


# Looking up values in a dictionary 
def dict_lookup():
    counts = dict()
    counts['Ken'] = 1
    counts['Erd'] = 1
    counts['Thelma'] = 1
    counts['Neon'] = 1
    names = ['Ken', 'Erd', 'Thelma', 'Neon', 'Gerald']
    for name in names:
        if name in counts:
            print(name, "is already in the dictionary.")
        else:
            print(name, "is not in the dictionary.")

# Retrieving keys and values from a dictionary
def dict_retrieve():
    jjj = {'Ken': 1, 'Erd': 2, 'Thelma': 3, 'Neon': 4}
    print(jjj)
    print("Keys: \n" + str(jjj.keys()) + "\n")
    print("Values: \n" + str(jjj.values()) + "\n")
    print("Items: \n" + str(list(jjj.items())) + "\n")

# Two iteration variables in a dictionary (it just becomes an idiom)
def dict_iterate():
    jjj = {'Ken': 1, 'Erd': 2, 'Thelma': 3, 'Neon': 4}
    for key, value in jjj.items():
        print(key, value)

# Refresher 
def refresher():
    name = input("Enter a file name: ")
    handle = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    bigcount = None
    bigword = None 
    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
            print(bigword, bigcount)


refresher()

