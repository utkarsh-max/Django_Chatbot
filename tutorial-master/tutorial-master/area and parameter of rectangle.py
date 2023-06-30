try:
    length = int(input("Enter length of rectangle"))
    breadth = int(input("Enter breadth of rectangle"))
    area = length * breadth
    parameter = 2 * (length + breadth)
    print("Area of rectangle: ", area)
    print("Parameter of rectangle: ", parameter)
except Exception:
    print("Check your input")
