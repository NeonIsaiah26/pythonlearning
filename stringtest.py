# def first_string():

#     str3 = '123'
#     x = int(str3) + 1
#     print('The value of x is:', x)
#     return x


# # =====================================================================================================================================


# def apple_string():

#     apple_count = int(input("Enter the number of apples you have: "))
#     apple_ate = int(input("Enter the number of apples you ate: "))
#     name = input("Enter your name: ")

#     if apple_ate > 30:
#         print("You eat too much apples,", name,"!!")
#     else:
#         x = apple_count - apple_ate
#         print("You have", x, "apples left after eating", apple_ate, "apples.")
#     return apple_ate


# # ======================================================================================================================================

# def looking_nside():
#     fruit = 'banana'
#     letter = fruit[1]
#     print(letter)
#     x = 3 
#     w = fruit [x - 1]
#     print(w)
#     return w

#====================================================================================================================================

# def string_length():
#     fruit = 'banana'
#     print(len(fruit))

#====================================================================================================================================

# def loop_strng():
#     fruit = 'banana'
#     index = 0
#     while index < len(fruit):
#         letter = fruit[index]
#         print(index, letter)
#         index = index + 1
# loop_strng()

#====================================================================================================================================

#using in as logical operator
def in_op():
    fruit = 'banana'
    if 'a' in fruit:
        print('Found the letter!!')
    else:
        print('Letter not found')
in_op()