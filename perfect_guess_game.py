import random
guess = 0
randomNo = random.randint(1, 100)
# print(randomNo)
userChoice = None

print("Heyy! Welcome to THE PERFECT GUESS GAME")
print("****************************************")

while(True):
   
    print("\nEnter 'q' to quit")

    userChoice = input("Choose any number from 1 to 100 : ")
    guess = guess+1

    if (userChoice.isalpha()):
        if userChoice == 'q':
            print("The game is ended.\n")
            exit()
        else:
            print("You have entered wrong choice. Play again!")
            exit()
    elif (int(userChoice) == randomNo):
        print("\nGreat! You guessed it right.")
        break
    elif (int(userChoice) > randomNo):
        print("You have entered a larger number.")
        print("\n-------------------------------")
    elif (int(userChoice) < randomNo):
        print("You have entered a smaller number.")
        print("\n-------------------------------")
    else:
        print("Sorry ! You guessed it wrong.")
print(f"\nYou required {guess} guess to win a game.")
print(f"Thanks for playing .\n")
