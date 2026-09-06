# List and definite loops 

from email.mime import text


def list_test(friend1, friend2, friend3):
    friends = [friend1, friend2, friend3]
    for friend in friends:
        print("Hello " + friend)


# Looking inside the list

def look_inside(Friend1, Friend2, Friend3):
    friends = [Friend1, Friend2, Friend3]
    print(friends[1])

#  How long is the list 

def list_length(*args):
    friends = list(args)
    print(len(friends))


# Using the range function to count the list

def range_list(*args):
    friend = [args]
    print(list(range(len(args))))


# # MANIPULATING LISTS

# List can be sliced using this

def list_slice(*args, cut_start, cut_end):
    return list(args)[cut_start:cut_end]



# Building a list from scratch

def build_list():
    stuff = list()
    stuff.append('book')
    stuff.append(99)
    stuff.append('cookie')
    print(stuff)

# is something in that list
# Just input in or not in 

# List in order 

def list_order(*args):
    friends = list(args)
    friends.sort()
    list(friends)
    print(friends)

# Built in functions and lists

def list_built_in(*args):
    friends = list(args)
    print(len(friends))
    print(max(friends))
    print(min(friends))
    print(sum(friends))
    print(sum(friends)/len(friends))

# Average finder 

def average_finder():
 
        total = 0
        count = 0
        while True:
            inp = input("Enter a number or type 'done' to finish: ")
            if inp == 'done':
                break
            try:
                total += float(inp)
                count += 1
            except ValueError:
                print("Please enter a valid number.")
        if count > 0:
            print("Average:", total / count)
        else:
            print("No numbers entered.")





# LIST AND STRINGS

# Splitting strings

def string_split(split_this):
    abc = (split_this)
    splita = abc.split()
    print(splita)
    print(len(splita))
    print(splita[2])


# another example. Email finder

def email_finder(file, email, findhost):
    handle = open(file)
    for lines in handle:
        if email in lines:
            lines = findhost
            print(lines.strip())
    words = findhost.split()
    atpos = findhost.find('@')
    dotpos = findhost.rfind('.')
    print("Username: ", findhost[:atpos])
    print("Domain: ", findhost[atpos + 1:dotpos])
    print("Suffix: ", findhost[dotpos + 1:])

email_finder('text.txt', 'neonisaiah@gmail.com', 'neonisaiah@gmail.com')





