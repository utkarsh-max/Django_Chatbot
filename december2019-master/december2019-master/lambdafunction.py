
'''
function without name
will have only one expression but can have multiple argument


'''

def sum(a,b):
    return a+b

print(sum(4,5))

f=lambda a,b:a+b

res=f(4,6)
print(res)
print(f(55,66))


'''def is_even(n):
    return n%2==0'''

#filter map and reduce
l=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda n:n%2==0,l))
print(even)

#map

square=list(map(lambda x:x*x,even))
print(square)

from functools import reduce
#reduce
sum=reduce(lambda a,b:a+b,square)
print(sum)