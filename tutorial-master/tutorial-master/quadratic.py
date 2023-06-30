try:
    from math import *
    a = int(input("Enter the value of A"))
    b = int(input("Enter the value of B"))
    c = int(input("Enter the value of C"))
    d = b * b - 4 * a * c
    if d == 0:
        print("roots are real and equal")
        x1 = -b / (2 * a)
        x2 = x1
        print("x1=", x1, "x2=", x2)
    elif d > 0:
        print("roots are real and unequal")
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("x1=", x1, "x2=", x2)
    else:
        print("roots are imaginary")
except Exception:
        print("Check your input")
