try:
    base = int(input("Enter a number for base of triangle"))
    height = int(input("Enter a number for height of triangle"))
    area = (1 / 2) * base * height
    print("area of triange= ", area)
except Exception:
    print("Something went wrong!!!!!!")