def my_max(num_list):
    """
    Function to find the larger value
    
    Attributes:
        num_list (list): A list of numbers to find the largest value from.
    """

    largest_so_far = -1
    for the_num in num_list:
        if the_num > largest_so_far:
            largest_so_far = the_num      
    return largest_so_far


def my_count(num_list):
    """
    Function to count the number of items in a list
    
    Attributes:
        num_list (list): A list of numbers to count.
    """

    count = 0
    for the_num in num_list:
        count = count + 1

    return count

#loop counting
count = 0
print('Before: ', count)
for test_passer in ['John', 'Jane', 'Joe', 'Jill']:
    count = count + 1
    print(count, test_passer)
print('After: ', count)

print('====================================================================================')

#purpose is to count how many times the loop ran and how many items are in the list

#loop sum
count = 0
print('Before: ', count)
for i in [1, 2, 3, 4, 5]:
    count = count + i
    print(count, i)

print('====================================================================================')

#finding the average
count = 0
sum = 0
print('Before: ', count, sum)
for value in [1, 2, 3, 4, 5]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After: ', count, sum, sum / count)

print('====================================================================================')

#filtering 
print('Before')
for value in [1, 2, 3, 4, 5]:
    if value > 2:
        print('Found:', value)
print('After')

print('====================================================================================')

#searching
found = False
print('Before', found)
for value in [1, 2, 3, 4, 5]:
    if value == 3:
        found = True
        print('Found:', value)
print('After', found)