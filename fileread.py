 # Reading a file and printing the contents of the file

def fileread(file_name):
    handle = open(file_name)
    for items in handle:
        print(items.strip())
    handle.close()

 # Counting lines in a file

def countlines(file_name):
    handle = open(file_name)
    count = 0
    for lines in handle:
        count += 1
    print("Number of lines in the file: ", count)
    handle.close()
 
 # Reading the "whole" file and printing the length of the file and the first 20 characters of the file

def read_whole(file_name, print_specific):
    handle = open(file_name)
    inp = handle.read()
    print(len(inp))
    print(inp[:print_specific])
    handle.close()

# Searching through a file for a specific string and printing the lines that contain the string

def search_string(file_name, search):
    handle = open(file_name)
    countlines(file_name)
    for lines in handle:
        if lines.startswith(search):
            print(lines.strip())

# Excluding lines that start with a specific string and printing the rest of the lines
def exclude_string(file_name, exclude):
    handle = open(file_name)
    for lines in handle:
        if not lines.startswith(exclude):
            print(lines.strip())

# Using in to select lines that contain a specific string and printing those lines
def host_finder(file_name, search):
    handle = open(file_name)
    for lines in handle:
        if search in lines:
            print(lines.strip())
    handle.close()


