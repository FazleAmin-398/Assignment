# Use random.randint(1, 50) to pick a secret number. Keep asking for guesses, saying
# “Too high” or “Too low”, and count the guesses. When correct, print “Got it in 6 guesses!”
# Then ask “Play again? (y/n)”.
import random

while True:
    number = random.randint(1, 50)
    guesses = 6

    while guesses > 0:
        guess = int(input("Guess the number between 1 and 50: "))
        guesses -= 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Got it in {6 - guesses} guesses!")
            break

    if guesses == 0:
        print("Sorry, you've used all your guesses. The number was",number)

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
