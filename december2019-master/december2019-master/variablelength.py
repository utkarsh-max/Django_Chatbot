def add(x,y,z):
    c=x+y+z
    print("Sum=",c)

add(6,8,7)

#4. variable length argument (*)

def varsum(*b):
    #print(a)
    print(b)
    sum=0
    for i in b:
        sum=sum+i
    print(sum)

varsum(1,2,3,4,5,6,55,33,66,33,66,33,6,33,77,33,77,44)


#5. keyword variable length argumnent

def persondata(name,**data):
    print(name)
    print(data)
    for i ,j in data.items():
        print(i,j)


persondata(name="bcd",age=16,city="gkp",phone=9956477467,roll=5)
