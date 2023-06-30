from array import array
import numpy

arr=array('i',[])


st=int(input("enter the no of students of class"))

i=0
while i<st:
    marks=int(input("enter the marks of each student"))
    arr.append(marks)
    i=i+1
print(arr)
for j in arr:
    print(j)

flag=0
search= int(input("enter the marks u want to search"))
for j in range(0,len(arr)):
    if arr[j]==search:
        print("item found at location",j)
        flag=1


if flag==0:
    print("item not found")

print(arr.index(search))

