import random

secret = random.randint(0, 10)
chances = 5

while chances > 0:
    guess = int(input("Enter your guess (0-10): "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("You win 🎉")
        break

    chances -= 1
    print("Remaining chances:", chances)

if chances == 0:
    print("Game over! Number was:", secret)
