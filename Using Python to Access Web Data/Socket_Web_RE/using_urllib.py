# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())



import urllib.request
import ssl

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
counts = dict()

# for line in fhand:
#     decoded_line = line.decode().strip()
#     print(decoded_line)  # 
    
#     words = decoded_line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# print("\n--- Word Counts ---")
# print(counts)

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


