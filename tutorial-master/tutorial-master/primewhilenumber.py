try:
    num = int(input("Enter a number"))
    i = 2
    while i < num:
        if num % i == 0:
            print("Number is not prime")
            break
        else:
            print("Number is prime")
            break
        i = i + 1
except Exception:
    print("Check input")