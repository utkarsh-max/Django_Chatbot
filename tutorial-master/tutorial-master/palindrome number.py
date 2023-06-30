try:
    num = int(input("Enter a number to check the number is palindrome or not"))
    rev = 0
    n = num
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    print(rev)
    if (num == rev):
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
except Exception:
    print("Check your value")
