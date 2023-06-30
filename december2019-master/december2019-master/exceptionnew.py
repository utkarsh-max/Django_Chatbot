
try:
    #risky code
    print("freeze is open")
    age = int(input("Enter your age"))
    # age=int(age)+10
    age = age + 22
    age1 = int(input("Enter your bhai age"))
    age=age/age1
    print(age)


except ValueError:
    print("you have enterd a character")

except ZeroDivisionError:
    print("bhaiya bhai ki age zero nahi ho sakti")

except Exception:
    print("somthing went wrong")

finally:
    #always runs weather exception comes or not
    print("freeze is closed")