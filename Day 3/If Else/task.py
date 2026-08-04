# IF / ELSE STATEMENTS NOTES
#
# An if / else statement lets a program make a decision.
# The program checks a condition.
# If the condition is True, it runs the if block.
# If the condition is False, it runs the else block.
#
# Real-life idea:
# If the bath water is higher than a safe level, drain the water.
# Else, keep filling the bath.
#
# In code, that decision pattern looks like this:
#
# if condition:
#     do_this_if_condition_is_true
# else:
#     do_this_if_condition_is_false


# This print() line welcomes the user.
# It runs before the height check happens.
print("Welcome to the rollercoaster!")

# input() asks the user to type their height.
# input() always gives back a string, even if the user types a number.
#
# Example:
# If the user types 130, input() gives us "130" as text.
#
# int() converts that text into an integer.
# We need an integer because we want to compare the height with the number 120.
#
# The final integer value is stored in the variable called height.
height = int(input("What is your height in cm? "))


# This is an if statement.
# The keyword if tells Python that we are about to check a condition.
#
# height > 120 is the condition.
# The > symbol means "greater than".
#
# This condition asks:
# Is the user's height greater than 120?
#
# A condition must evaluate to either True or False.
#
# The colon : is required after the condition.
# It tells Python that the indented block below belongs to this if statement.
if height > 120:
    # This line is indented, so it is inside the if block.
    # It only runs if height > 120 is True.
    print("You can ride the rollercoaster")
else:
    # else catches the opposite situation.
    # It runs when the if condition is False.
    #
    # Important:
    # else must line up with if.
    # It should not be indented under the if block.
    print("Sorry, you have to grow taller before you can ride.")


# INDENTATION
#
# Indentation means the spaces at the beginning of a line.
# In Python, indentation is part of the code's meaning.
#
# Code indented under if belongs to the if block.
# Code indented under else belongs to the else block.
#
# If the indentation is wrong, Python can give an IndentationError.


# COMPARISON OPERATORS
#
# Comparison operators compare two values.
# The result is always True or False.
#
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# ==  equal to
# !=  not equal to
#
# Examples:
# 130 > 120   is True
# 90 > 120    is False
# 120 > 120   is False
# 120 >= 120  is True
# 120 == 120  is True
# 121 != 120  is True


# IMPORTANT: = VS ==
#
# One equals sign = is for assignment.
# It stores a value in a variable.
#
# Example:
# height = 120
#
# Two equals signs == are for comparison.
# They check whether two values are equal.
#
# Example:
# height == 120
#
# These are not the same thing.
# Use = when storing a value.
# Use == when asking a True/False question.


# ABOUT THIS PROGRAM
#
# The current condition is:
# height > 120
#
# That means a person who is exactly 120 cm is not allowed to ride.
# If you want to include people who are exactly 120 cm,
# change the condition to:
#
# if height >= 120:
#
# Then 120 cm, 121 cm, 130 cm, and higher would be allowed.
