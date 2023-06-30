num=float(input("Enter boxer's weight in Pounds"))
print("Boxer's weight is in Pounds =",num)
if num<115:
    print("Boxer class is Flyweight")
elif (num>=115) and (num<=121):
    print("Boxer class is Bantamweight")
elif (num>=122) and (num<=153):
    print("Boxer class is Featherweight")
elif (num>=154) and (num<=189):
    print("Boxer class is Middleweight")
else:
    print("Boxer class is Heavyweight")