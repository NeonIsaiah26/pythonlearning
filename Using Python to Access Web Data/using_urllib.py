# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())



import urllib.request
import ssl

# Create an unverified SSL context to bypass local certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Pass the context into urlopen
fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
for line in fhand:
   decoded_line = (line.decode().strip())
   print(decoded_line)
counts = dict()
word = decoded_line.rsplit()
for words in word:
    word = line.decode().split()
    for word in words:
        counts[words] = counts.get(words, 0) + 1
print(counts)


# for line in fhand:
#     print(line.decode().strip())
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


