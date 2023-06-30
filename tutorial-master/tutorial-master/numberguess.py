import random
n = random.randint(1, 99)
print(n)
print("You just have 5 chance")
chance=1
guess = int(input("Enter an integer from 1 to 99: "))
while n != guess:
    while chance <= 4:
        #chance = chance + 1
        if guess < n:

            print("guess is low")

            guess = int(input(" Low Wala Enter an integer from 1 to 99: "))
            chance = chance + 1
        elif guess > n:

            print("guess is high")

            guess = int(input("High Wala Enter an integer from 1 to 99: "))
            chance = chance + 1

        else:
            print("You guessed it")
            break

    if chance>5:
        print("Your chance is over")
        break


else:
    print("You guessed it")
    #break


# break




'''else:
    print(guess)'''








