try:
    year = int(input("Enter a year to find out it's leap or not"))
    if year % 100 == 0:
        if year % 400== 0:
            print("It's a leap year")
        else:
            print("It's not a leap year")
    elif year % 4 == 0:
        print("It's a leap year")
    else:
        print("It's not a leap year")
except ValueError:
    print("PLEASE Enter only Integer Value")
except Exception:
    print("Something went wrong")
