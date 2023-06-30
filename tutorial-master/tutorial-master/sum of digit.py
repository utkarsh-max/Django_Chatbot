try:
    num = int(input("Enter a number"))
    add = 0
    while num > 0:
        mod = num % 10
        num = num // 10
        add = add + mod
    print("sum of digit: ", add)
except Exception:
    print("Something went wrong!!!!!")



