vowels = set("aeiou")
word = "hello"
u = vowels.union(set(word)) 
print(u)
d = vowels.difference(set(word))
print(d)
i = vowels.intersection(set(word))
print(i)