x=10  #global varibale
def test():
    y=15 #local varaible
    x=50
    global z
    z=20
    print(y)
    print(x)
    #to access global variable inside a function
    #which have same name with  local varibale
    s=globals()['x']
    print(s)

test()
print(x)
#print(y)
print(z)
