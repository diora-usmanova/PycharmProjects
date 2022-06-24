# DISPLAY NONDUPLICATE WORDS IN ASCENDING ORDER

f = open('14.8_textFile', 'r')
words = f.read()
print(words)
s = set()
items = words.split()
s = set(str(x) for x in items)
print(sorted(s))

f.close()
