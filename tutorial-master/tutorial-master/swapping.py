try:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    print("The value of a: ", a)
    print("The value of b: ", b)
    a, b = b, a
    s = "After Swapping"
    print(s.center(40, "*"))
    print("The value of a: ", a)
    print("The value of b: ", b)
except Exception:
    print("Check your input")