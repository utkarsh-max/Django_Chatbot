try:
    cost = int(input("Enter cost price"))
    selling = int(input("Enter selling price"))
    if (cost > selling):
        print("It's a lose")
        lose = cost - selling
        print("Your lose is: ", lose)
    elif (cost == selling):
        print("There is a balance")
    else:
        print("It's a profit")
        profit = selling - cost
        print("Your profit is: ", profit)
except Exception:
    print("Something Error")
