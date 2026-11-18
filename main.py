import random

print("🎮 Welcome to Number Guessing Game!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try a bigger number.")

    elif guess > secret_number:
        print("Too High! Try a smaller number.")

    else:
        print("🎉 Congratulations! You Won!")
        print("Your Attempts:", attempts)
        break