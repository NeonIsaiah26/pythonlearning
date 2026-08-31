# def lowercase():
#     greet = 'Hello Bob'
#     zap = greet.lower()
#     print(zap)
# lowercase()

# # for uppercase just type upper instead of lower
# # ====================================================================================================================================
# # searching a string

# def searching_string():
#   fruit = 'banana'
#   pos = fruit.find('na')
#   print(pos)

# aa = fruit.find('z')
# print(aa)

# # ====================================================================================================================================
# # Search and replace

# def replace_txt():
#   greet = 'hello bob'
#   nstr = greet.replace('bob', 'jane')
#   print(nstr)

# # ====================================================================================================================================
# # parsing and extracting 

def parse_extract():
    data = 'From neon.isaiah@gmail.com Sat Jan 5 09:14:16 2008'
    atpos = data.find('@')
    sppos = data.find(' ', atpos)
    host = data [atpos + 1 : sppos]
    print(host)
    
parse_extract()