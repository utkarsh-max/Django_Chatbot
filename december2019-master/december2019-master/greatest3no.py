a=int(input("Enter first no"))
b=int(input("Enter second no"))
c=int(input("Enter third no"))
print("a=",a,"b=",b,"c=",c)

if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b>c:
    print("b is gratest")
else:
    print("c is greatest")