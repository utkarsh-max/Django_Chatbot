try:
    a = int(input("Enter first angle"))
    b = int(input("Enter second angle"))
    c = int(input("Enter third angle"))
    sum = a + b + c
    print("sum of total angles: ", sum)
    if (sum == 180):
        print("It's a valid triangle")
    else:
        print("It's not a valid triangle")
except Exception:
    print("Enter valid angles")