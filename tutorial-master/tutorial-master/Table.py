try:
    num = int(input("Enter a number"))
    i = 1
    while i <= 10:
        t = num * i
        i = i + 1
        print(t)
except Exception:
    print("Check your input")
