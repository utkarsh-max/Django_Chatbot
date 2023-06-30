try:
    r = int(input("Enter radius of circle always in integer for find out area: "))
    a = 3.14 * r * r
    print("Area of circle= ",a)
    r1=int(input("Enter radius of circle to find out parameter: "))
    p=2*3.14*r1
    print("Parameter of circle: ",p)
except Exception:
    print("Something went wrong!!!!!!")

