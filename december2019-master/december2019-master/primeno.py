a=int(input("enter any no"))

i=2
while i<=a-1:
    if a%i==0:
        print("Not Prime")
        break

    i=i+1

else:  #this else will run when the loop not properly runs
    print("Prime no")