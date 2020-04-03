word = input("Please provide the string :")
vowel = {'a', 'e', 'i', 'o', 'u'}
d = {}
for w in word:
    if w in vowel:
        d[w] = d.get(w, 0) + 1

for k, v in d.items():
    print(k, " occured ", v, " times.")
