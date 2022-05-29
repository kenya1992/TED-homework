with open('hw.txt') as f:

    data = f.read()


words = {}

for word in data.split():


    words[word] = words.get(word, 0) + 1 


d = [(v, k) for k, v in words.items()]
d.sort()
d.reverse()
for count, word in d[:]:
    print(count, word)
