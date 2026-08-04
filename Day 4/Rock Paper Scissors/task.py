# ROCK PAPER SCISSORS PROJECT NOTES
#
# Goal:
# Make a game where the user chooses rock, paper, or scissors,
# and the computer randomly chooses one too.
#
# Then we compare both choices and decide:
# - You win
# - You lose
# - It is a draw
#
# This project uses:
# - variables
# - input()
# - int()
# - random.randint()
# - lists
# - indexing
# - if / elif / else statements
# - logical operators
# - ASCII art


# We import the random module so the computer can make a random choice.
# random.randint(0, 2) will let the computer choose 0, 1, or 2.
import random


# These three variables store ASCII art.
# ASCII art is a picture made from text characters.
#
# Triple quotes allow each picture to stretch across multiple lines.
#
# The variable names are:
# rock
# paper
# scissors
#
# These are variables, not strings that we type manually later.
# That means we print rock, not "rock", when we want the picture.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# A list lets us group related values together.
#
# This list stores the three ASCII art choices in order:
# index 0 -> rock
# index 1 -> paper
# index 2 -> scissors
#
# This order matches the prompt we give the user:
# 0 for rock
# 1 for paper
# 2 for scissors
game_images = [rock, paper, scissors]


# input() asks the user to type their choice.
# input() always returns a string, so we wrap it in int().
#
# int(...) converts the user's answer from text into a whole number.
#
# Example:
# input() gives "0"
# int("0") gives 0
#
# We need a number because we will use it as a list index.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


# The computer also needs to choose rock, paper, or scissors.
#
# random.randint(0, 2) gives a random integer from 0 to 2.
# randint includes both end numbers, so possible results are:
# 0, 1, or 2
computer_choice = random.randint(0, 2)


# INVALID INPUT CHECK
#
# The valid choices are only:
# 0, 1, and 2
#
# If the user types a number less than 0 or greater than 2,
# that number cannot be used as an index for game_images.
#
# Example:
# game_images[0] works.
# game_images[1] works.
# game_images[2] works.
# game_images[3] would crash with an IndexError.
#
# So we check for invalid input before printing game_images[user_choice].
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose.")

else:
    # This prints the user's chosen ASCII art.
    # user_choice is used as the index.
    #
    # If user_choice is 0, this prints rock.
    # If user_choice is 1, this prints paper.
    # If user_choice is 2, this prints scissors.
    print("You chose:")
    print(game_images[user_choice])

    # This prints the computer's chosen ASCII art.
    # computer_choice is also 0, 1, or 2,
    # so it can safely be used as an index.
    print("Computer chose:")
    print(game_images[computer_choice])

    # GAME RULES
    #
    # Rock beats scissors.
    # Scissors beats paper.
    # Paper beats rock.
    #
    # Number meanings:
    # 0 = rock
    # 1 = paper
    # 2 = scissors

    # Draw:
    # If both choices are the same, nobody wins.
    #
    # Example:
    # user_choice = 0 and computer_choice = 0
    # Both chose rock, so it is a draw.
    if user_choice == computer_choice:
        print("It's a draw.")

    # Special winning case for the user:
    # User chooses rock, computer chooses scissors.
    #
    # 0 = rock
    # 2 = scissors
    #
    # Rock beats scissors, so the user wins.
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")

    # Special losing case for the user:
    # User chooses scissors, computer chooses rock.
    #
    # 2 = scissors
    # 0 = rock
    #
    # Rock beats scissors, so the user loses.
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")

    # General winning case:
    #
    # For the remaining normal cases,
    # the higher number beats the lower number.
    #
    # 1 beats 0:
    # Paper beats rock.
    #
    # 2 beats 1:
    # Scissors beats paper.
    elif user_choice > computer_choice:
        print("You win!")

    # General losing case:
    #
    # If the computer's number is higher than the user's number,
    # and it was not one of the special cases above,
    # then the user loses.
    elif computer_choice > user_choice:
        print("You lose.")


# QUICK REVIEW
#
# random.randint(0, 2)
# Gives 0, 1, or 2 randomly.
#
# game_images = [rock, paper, scissors]
# Stores the pictures in a list.
#
# game_images[0]
# Gets the rock picture.
#
# game_images[1]
# Gets the paper picture.
#
# game_images[2]
# Gets the scissors picture.
#
# input() gives text.
# int(input(...)) converts that text into a number.
#
# Always check if the user's number is valid before using it as a list index.
# Otherwise, a number like 9 would cause an IndexError.
#
# == checks if two values are equal.
# and lets us check two conditions together.
# elif lets us check another possible condition.
