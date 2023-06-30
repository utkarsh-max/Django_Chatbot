try:
    num = int(input("Enter a number to check even or odd"))
    if (num % 2 == 0):
        print("number is even")
    else:
        print("number is odd ")
except ValueError:
    print("PLEASE Enter only Integer")
except Exception:
    print("Something went wrong please check your input")

