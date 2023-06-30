try:
    r_age = int(input("Enter age of Ram"))
    s_age = int(input("Enter age of Shyam"))
    a_age = int(input("Enter age of Ajay"))
    if (r_age < s_age) and (r_age < a_age):
        print("Ram is youngest")
    elif (s_age < r_age) and (s_age < a_age):
        print("Shyam is youngest")
    else:
        print("Ajay is youngest")
except Exception:
    print("Enter the correct age")
