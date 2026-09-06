def convert_case(my_string, con):
    if con == "lower":
        x = my_string.lower()
    elif con == "upper":
        x = my_string.upper()
    return x

# for uppercase just type upper instead of lower
# ====================================================================================================================================
# searching a string

def searching_string(my_string, word, start, end):
  pos = my_string.find(word, start, end)
  if pos == -1:
     print("Cannot find the word you are looking")
  else:
     print(pos)
# ====================================================================================================================================
# Search and replace

def replace_txt(my_string,old_word, new_word):
  nstr = my_string.replace(old_word, new_word)
  return(nstr)

# ====================================================================================================================================
# parsing and extracting 

def parse_extract(data):
    atpos = data.find('@')
    sppos = data.find(' ', atpos)
    host = data [atpos + 1 : sppos]
    print(f'The host is: {host}')


# ====================================================================================================================================
# data = 'From neon.isaiah@yahoo.com Sat Jan 5 09:14:16 2008'
# parse_extract(data)