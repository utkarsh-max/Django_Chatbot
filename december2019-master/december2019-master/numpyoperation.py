from numpy import *

arr=array([1,20,3,24,5,6])
arr8=array([32,54,76,32,89,343])
print(arr)

a=[222.55,66]
b=tuple(a)
print(b)
'''arr2=arr+5
print(arr2)

arr3=arr+arr2
print(arr3)

arr4=sin(arr) #sqrt
print(arr4)

a=min(arr) #max, sum,
print(a)

arr5=sort(arr)
print(arr5)

print(arr[4])

print(len(arr))

print(arr[-1])
'''
# copy of one array into another
rra=arr
print(rra)
print(id(arr))
print(id(rra))

# what if u want diffrent reference
#shallow copy because if we change the value of one array it affects another
arrview=arr.view() #this is aliasing
print(arrview)
print(id(arr))
print(id(arrview))

arrview[1]=6222
print(arrview)
print(arr)


#deep copy

arrcopy=arr8.copy()
print(arrcopy)
print(arr8)
print(id(arr8))
print(id(arrcopy))
arrcopy[1]=888888
print(arrcopy)
print(arr8)