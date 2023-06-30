from numpy import *

'''
there are 6 ways to create an array using numpy
1. array()
2. linspace()
3. logspace()
4. arange()
5. zeros()
6. ones()


'''

'''arr=array([1,2,3,4.5],float32)
print(arr)

print(arr.dtype)

for i in arr:
    print(i)'''

#linspace
arr2= linspace(0,15)
print(arr2)

arr3= logspace(1,5,5)
print(arr3)

arr4= arange(1,15,2)
print(arr4)

arr5=ones(50)
print(arr5)

arr6=zeros(4,int)
print(arr6)