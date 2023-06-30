try:
    print("Enter the number of following Five subjects")
    a = int(input("Enter the number of English out of 50"))
    b = int(input("Enter the number of Hindi out of 50"))
    c = int(input("Enter the number of Maths out of 50"))
    d = int(input("Enter the number of Computer out of 50"))
    e = int(input("Enter the number of Science out of 50"))
    if (a <= 50) and (b <= 50) and (c <= 50) and (d <= 50) and (e <= 50):
        total = a + b + c + d + e
        print("Total Marks= ", total)
        per = (total * 100) / 250
        print("Total percentage= ", per)
        if (per >= 60):
            print("Grade is 'A'")
        elif (per >= 45):
            print("Grade is 'B'")
        elif (per >= 33):
            print("Grade is 'C'")
        else:
            print("You are Fail!!!!!")
    else:
        print("PLEASE Enter the marks between 0 to 50")
except Exception:
    print("PLEASE Enter correct value")