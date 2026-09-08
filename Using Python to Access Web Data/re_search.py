# file = open('text.txt')
# for line in file:
#     line = line.rstrip()
#     if line.find('From: ') >= 0:
#         print(line)


import re
# def re_search(my_file):
#     with open(my_file) as file:
#       for line in file:
#           line = line.rstrip()
#           if re.search('Ken to ', line):
#             print(line)

# re_search('text.txt')

def find_all(my_file):
    with open(my_file) as file:  # Using 'with' safely handles closing the file
        for line in file:
            line = line.rstrip()
            # 2. Passed 'line' as the target string to search
            y = re.findall(r"^123+\S+", line)

            # 3. Print the results if any emails were found
            if len(y) > 0:
                print(y)




def double_split(my_file):
    with open(my_file) as file:
        for line in file:
            line = line.rstrip()
            words = line.split()
            if len(words) < 2:
                continue
            email = words[1]
            if "@" in email:
                pieces = email.split("@")
                print(pieces[1])

double_split('text.txt')





