import random
from art import logo

print(logo)

guessed_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = (input("Choose a difficulty. Type 'easy' or 'hard'")).lower()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

guess = 0

while attempts > 0:
    print(f"Guessed number is {guessed_number}")
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == guessed_number:
        print("You guessed it right")
        break
    elif guess > guessed_number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")

    attempts = attempts - 1

if attempts == 0 and guess != guessed_number:
    print("You have run out of guesses.")