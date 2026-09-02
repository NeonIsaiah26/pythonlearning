#Reading a file and printing the contents of the file

def fileread(file_name):
    handle = open(file_name)
    for items in handle:
        print(items.strip())
    handle.close()

#Counting lines in a file

def countlines(file_name):
    handle = open(file_name)
    count = 0
    for lines in handle:
        count += 1
    print("Number of lines in the file: ", count)
    handle.close()
