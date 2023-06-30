s={1,2,2}
print(s)

s.add('apple')
print(s)
s.remove(1)
print(s)
list_f_animal=frozenset({'lion','tiger'})
print(list_f_animal)
#list_f_animal.add('elephant')

emptyset=set()
print(type(emptyset))

emptyset=set(s)
print(emptyset)

#set operation
a={1,2,3,4,6}
b={3,4,7}

print(4 in a)

#union
print(a|b)

#intersection
print(a&b)

#difference

print(a-b)

#symmetric differenc
print(a^b)

c=a.copy()
print(c)

print(a.clear())