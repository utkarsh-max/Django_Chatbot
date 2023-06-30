num=int(input("Enter the number to check it is prime or not"))
if(num<300) and (num>1):
    for i in range(2,num):
        if (num % i == 0):
            print("The number is not a prime number")
            break
    else:
        print("This number is prime")
