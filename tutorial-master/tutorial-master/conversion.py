try:
    km = int(input("Enter distance in kilometer"))
    me = km * 1000
    feet = km * 3280.8399
    centi = km * 100000
    print("Distance in meter= ", me)
    print("Distance in feet= ", feet)
    print("Distance in centimeter= ", centi)
except Exception:
    print("Check your input")
