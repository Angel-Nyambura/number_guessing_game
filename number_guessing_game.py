import random

number_guessed = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess a number between 1 to 100"))
        if guess < number_guessed:
            print("Too low!")

        elif guess > number_guessed:
            print("Too high!")

        else:
            print("Congratultions!You guessed correctly")
            break

    except ValueError:
        print("Please enter a valid number")
