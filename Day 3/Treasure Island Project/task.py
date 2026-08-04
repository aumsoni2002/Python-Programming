# TREASURE ISLAND PROJECT NOTES
#
# This project is a simple "choose your own adventure" game.
# The player makes choices by typing answers into input().
# Each choice sends the player down a different path.
#
# This project uses:
# - print()
# - input()
# - variables
# - strings
# - if / elif / else statements
# - nested conditionals
# - .lower()
# - triple-quoted strings
# - escape characters like \n


# This print() displays ASCII art.
# ASCII art is a picture made using normal keyboard characters.
#
# The r before the triple quotes makes this a raw string.
# A raw string treats backslashes mostly as normal characters.
# This is useful for ASCII art because ASCII art often contains backslashes.
#
# The three quotes ''' allow the string to stretch across many lines.
# This is called a multi-line string.
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# These two print() statements introduce the game.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# This print() gives the player the first story situation.
#
# The apostrophe in You're works here because the string uses double quotes
# around the outside.
# Python sees the apostrophe as text, not as the end of the string.
print("You're at a crossroad. Where do you want to go?")

# input() asks the player to type a choice.
#
# The prompt uses single quotes on the outside:
# 'Type "left" or "right"\n'
#
# This lets us use double quotes inside the text without confusing Python.
#
# \n means new line.
# It moves the user's typing onto the next line, which makes the game easier to read.
#
# .lower() converts the player's answer to lowercase.
# This means "LEFT", "Left", and "left" all become "left".
# That makes our if statement easier because we only need to check for lowercase.
decision_1 = input('Type "left" or "right"\n').lower()

# This is the first branch of the game.
# == checks whether decision_1 is equal to the string "left".
#
# If the player chose left, the game continues.
# If they chose anything else, the else block runs and the game ends.
if decision_1 == "left":
    # This code is indented, so it only runs if decision_1 == "left" is True.
    print("You have come to a lake. There is an island in the middle of the lake.")

    # This is the second choice.
    # It is nested inside the first if statement.
    #
    # Nested means one decision happens inside another decision.
    # The player only sees this question if they chose left first.
    decision_2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

    # This checks the second choice.
    # If the player chooses wait, the game continues.
    # If they choose swim or anything else, the else block runs.
    if decision_2 == "wait":
        # This code only runs if:
        # decision_1 == "left"
        # and decision_2 == "wait"
        print("You arrive at the island unharmed. There is a house with 3 doors.")

        # This is the third and final choice.
        # Again, .lower() makes the input case-insensitive.
        decision_3 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()

        # if / elif / else is useful when there are several possible answers.
        #
        # if checks the first condition.
        # elif means "else if" and checks another condition.
        # else catches anything that did not match the earlier choices.
        if decision_3 == "red":
            print("Burned by fire. Game Over")
        elif decision_3 == "yellow":
            # Yellow is the winning choice in this game.
            print("You win.")
        elif decision_3 == "blue":
            print("Eaten by beasts. Game Over")
        else:
            # This catches any answer that is not red, yellow, or blue.
            # Example: green, purple, hello, or any unexpected input.
            print("Game Over.")
    else:
        # This else belongs to the second decision.
        # It runs if decision_2 was not "wait".
        print("You have been attacked by trout. Game Over.")
else:
    # This else belongs to the first decision.
    # It runs if decision_1 was not "left".
    print("You fell into a hole. Game Over.")


# IMPORTANT REVIEW NOTES
#
# 1. Why use .lower()?
# Without .lower(), Python treats "left" and "Left" as different strings.
# With .lower(), the player can type LEFT, Left, or left and the code still works.
#
# 2. Why use nested if statements?
# The second question should only happen if the first choice was correct.
# The third question should only happen if the second choice was correct.
# Nesting lets us build that step-by-step story path.
#
# 3. Why use elif for the doors?
# There are more than two possible door choices:
# red, yellow, blue, or something unexpected.
# if / elif / elif / else lets each choice have a different result.
#
# 4. What does \n do?
# \n creates a new line inside a string.
# It is useful in input prompts because it lets the player type on the next line.
#
# 5. What are triple quotes for?
# Triple quotes let you write a string across multiple lines.
# They are useful for ASCII art and long blocks of text.
