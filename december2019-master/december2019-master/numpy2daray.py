from numpy import *
'''
a=array([
    [1,2,3],
    [2,3,4]
])
print(a)

print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)

b=a.flatten()
print(b)

print(b.reshape(3,2))
'''
x=array([
    [1,2,3],
    [2,3,4]
])

xbhai=matrix('1 2 1; 2 3 4')
print(xbhai)
y=array([
    [3,31,113],
    [41,224,4],
    [6,7,8]
])


'''c=x+y
print(c)'''

'''
Numpy matrices are strictly 2-dimensional, while numpy arrays (ndarrays) are N-dimensional. Matrix objects are a subclass of ndarray, so they inherit all the attributes and methods of ndarrays.

The main advantage of numpy matrices is that they provide a convenient notation for matrix multiplication: if a and b are matrices, then a*b is their matrix product.
'''
d=matrix(x)*matrix(y)
print(d)

p=matrix(y)
print(p)
print(p.diagonal())
print(p.min())
print(p.max())



