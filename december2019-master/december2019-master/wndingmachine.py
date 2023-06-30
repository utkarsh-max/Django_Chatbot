a=int(input("How many toffe u want"))
stock=10
i=1
while i<=a:
    if i<=stock:
        print(i,"Collect Tofee")
    else:
        print("Out of stock")
        break
    i=i+1
else:
    print("Thank you")
