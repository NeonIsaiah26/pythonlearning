def first_string(my_str):

    x = int(my_str) + 1
    return x


# =====================================================================================================================================


def apple_string():

    apple_count = int(input("Enter the number of apples you have: "))
    apple_ate = int(input("Enter the number of apples you ate: "))
    name = input("Enter your name: ")

    if apple_ate >= 30:
        print("You eat too much apples,", name,"!!")
    else:
        x = apple_count - apple_ate
        print(f"You have {x}, apples left after eating, {apple_ate}, apples.")
    return apple_ate


# ======================================================================================================================================

def looking_inside(my_string):
    
    letter = my_string[1]
    print(letter)
    x = 3 
    w = my_string [x - 1]
    print(w)
    

# ====================================================================================================================================

def string_length(my_string):
    print(len(my_string))
    

# ====================================================================================================================================

def loop_strng(my_string):
    index = 0
    while index < len(my_string):
        letter = my_string[index]
        print(index, letter)
        index = index + 1
    
       

# ====================================================================================================================================

#using in as logical operator
def in_op(my_string):
    if 'a' in my_string:
        print('Found the letter!!')
    else:
        print('Letter not found')

def str_finder(my_string, a):
    if a in my_string:
            print('Found the letter!!')
    else:
        print('Letter not found')