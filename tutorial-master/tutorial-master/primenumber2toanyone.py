try:
    num = int(input("Enter a number"))
    i = 2
    while i < num:
        if i % 2 == 0:
            print(i, " is not a prime number")
        else:
            print(i, " is a prime number")
        i = i + 1
except Exception:
    print("Check input")