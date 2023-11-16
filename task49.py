import random

secret_number = random.randint(1,100)
for i in range(10):
    guess = int(input("Guess a number between 1 to 100 inclusive:"))
    if guess> secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Congratulations! You guessed the correct number ")
        break