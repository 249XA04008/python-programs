num=int(input("Give the number you want to guess between 0 TO ? : "))
import random
num = random.randint(0, num)
for i in range (num):
    guess =int(input("Guess the number: "))
    if guess==num:
        print("Congratulations! You guessed the number.")
        break
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
