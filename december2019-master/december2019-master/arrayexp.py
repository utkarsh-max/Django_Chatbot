from array import *
arr1=array('i',[1,2,3,4,65])
print(arr1)
for a in arr1:
    print(a)

arr2=array('d',[1,2,3,4,65.77])
print(arr2)
for a in arr2:
    print(a)

for j in range(0,len(arr2)):
    print(j,arr2[j])


print(arr2.typecode)
print(arr1.buffer_info())
print(id(arr1))


a,b=2,5
print(id(a),id(b))

h=2
print(id(h))


