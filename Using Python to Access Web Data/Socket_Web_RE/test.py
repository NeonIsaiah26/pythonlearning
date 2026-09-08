from using_urllib import web_connect


web_connect('https://www.coursera.org/my-learning?myLearningTab=IN_PROGRESS')
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)