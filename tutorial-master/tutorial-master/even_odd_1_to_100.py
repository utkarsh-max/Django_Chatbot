try:
    start=int(input("Enter starting number"))
    end=int(input("Enter Ending number"))
    if start<end:
        i=start
        while i<=end:
            if i % 2 == 0:
                print("Even number=",i)
            else:
                print("Odd number=",i)
            i=i+1
    else:
        i=start
        while i>=end:
            if i%2==0:
                print("Even number= ",i)
            else:
                print("Odd number= ",i)
            i=i-1
except Exception:
    print("Check your input")