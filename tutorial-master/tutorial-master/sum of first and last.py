try:
    num = int(input("Enter a number"))
    last = num % 10
    first = num // 10
    dim = str(first)
    fir = int(dim[0])
    addition = last + fir
    print(addition)
except Exception:
    print("Check the given input coz it's always in integer")