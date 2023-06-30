stock=15
num=int(input("Enter your order"))
count = 0
i=stock
if num<stock:
    while num>=count:
        count = count + 1
        stock = stock - 1
    print(count-1, " Toffies are debited")
    print(i-num," is the value of reminder toffies")
elif num == stock:
    print("All ", stock, " Toffis are debited")
else:
    while stock == 0:
        stock = stock - 1
        count = count + 1
    print(count, " Toffies are debited")





