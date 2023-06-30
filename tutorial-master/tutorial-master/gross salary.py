try:
    basic_salary = int(input("Enter basic salary"))
    print("Include dearness allowance 40% and house rent allowance 20%")
    da = (basic_salary * 40) / 100
    ha = (basic_salary * 20) / 100
    total = da + ha+basic_salary
    print("your total gross salary is= ", total)
except Exception:
    print("Check your input again")
