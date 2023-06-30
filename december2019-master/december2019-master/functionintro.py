'''import mymodule
mymodule.a()'''

from mymodule import *

a()
b()

print(__name__)
def greet():
    print("good Morning")


greet()
greet()
greet()

def add(x,y):
    c=x+y
    print("Sum=",c)


add(3,5)
add(44,66)

def add1(x,y):
    c=x+y
    return c

d=add1(55,77)
print(d)

print(add1(44,56))

def calci(r,s):
    sum=r+s
    mul=r*s
    return sum,mul

p,q=calci(3,6)
print(p,q)