a=int(input("enter First Number"))
b=int(input("enter Second Number"))
c=int(input("enter Third Number"))

print("a=",a,"b=",b,"c=",c)

if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")