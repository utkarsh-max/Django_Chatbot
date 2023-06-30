'''def add(x,y):
    c=x+y
    print("Sum=",c)

add(6,8)'''

#1. positional argument
def person(name,age):
    print("Name=",name)
    age=age+10
    print("Age=",age)

person("Ram",44)

#person(33,"sohan")

'''
pass an agument to function
1. positional argument
2. keyword argument
3. default argument
4. variable length argument (*)
5. keword variable length argumnent
'''

#2. keyword argument
person(name="ram",age=55)
person(age=55,name="ram")

#3. default argument
def person1(name,age=18):
    print("Name=",name)
    age=age+10
    print("Age=",age)

person1("mohan")
person1("sohan",88)