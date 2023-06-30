n = int(input("Enter a number to find it's Sum"))
digit = n
sum = 0
while(digit > 0):
    n1 = digit % 10
    sum = sum+n1
    digit = digit//10
print(sum)
