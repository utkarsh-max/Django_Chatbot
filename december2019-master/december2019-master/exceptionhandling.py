try:
    print("Freeze is open")
    # risky code which may contain run time error
    a = int(input("enter First Number"))
    print(a)

    b = int(input("enter Second Number"))
    print(b)

    d = a/b
    print("div=", d)
    print("thank you")


except ValueError:
    print("You have entered a character")

except ZeroDivisionError:
    print("Second no can not be zero")

except Exception:
    print("Something went wrong")

# always executes
finally:
    print("Freeze is closed")