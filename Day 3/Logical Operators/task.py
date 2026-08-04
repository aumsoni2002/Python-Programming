# LOGICAL OPERATORS NOTES
#
# Logical operators let us check multiple conditions together.
#
# The three main logical operators are:
# and
# or
# not
#
# They are useful when one decision depends on more than one condition.
#
# Example idea:
# Is the pizza large AND does the user want pepperoni AND does the user want extra cheese?
#
# Instead of writing many separate nested if statements,
# logical operators let us combine checks on one line.


# 1. THE and OPERATOR
#
# and means both conditions must be True.
#
# True and True becomes True.
# True and False becomes False.
# False and True becomes False.
# False and False becomes False.
#
# Example:
a = 12
print(a > 10 and a < 13)  # True, because 12 is greater than 10 and less than 13
print(a > 15 and a < 13)  # False, because 12 is not greater than 15


# 2. THE or OPERATOR
#
# or means at least one condition must be True.
#
# True or True becomes True.
# True or False becomes True.
# False or True becomes True.
# False or False becomes False.
#
# Example:
print(a > 10 or a < 10)  # True, because a > 10 is True
print(a > 15 or a < 10)  # False, because both conditions are False


# 3. THE not OPERATOR
#
# not reverses a condition.
#
# not True becomes False.
# not False becomes True.
#
# Example:
print(not a < 0)  # True, because a < 0 is False, and not reverses it


# ROLLERCOASTER EXAMPLE USING LOGICAL OPERATORS
#
# This program checks:
# 1. Is the user tall enough to ride?
# 2. What ticket price should they pay based on age?
# 3. Are they between 45 and 55, so they get a free ride?
# 4. Do they want a photo added to the bill?


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# bill starts at 0.
# We will change this value later depending on the user's age
# and whether they want a photo.
bill = 0


# First condition:
# The user must be at least 120 cm tall to ride.
if height >= 120:
    print("You can ride the rollercoaster!")

    # This age question only happens if the user is tall enough.
    # That is because it is indented inside the height if block.
    age = int(input("What is your age? "))

    # If the user is under 12, the child ticket price is $5.
    if age < 12:
        bill = 5
        print("Child tickets are $5.")

    # If the first condition was False, Python checks this elif.
    # age <= 18 catches users from 12 to 18.
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    # This elif uses the and logical operator.
    #
    # age >= 45 and age <= 55 means:
    # Is the age greater than or equal to 45
    # AND is the age less than or equal to 55?
    #
    # Both sides must be True for the whole condition to be True.
    #
    # Examples:
    # age = 50 -> True and True -> True, so the free ride message runs.
    # age = 40 -> False and True -> False, so this block is skipped.
    # age = 60 -> True and False -> False, so this block is skipped.
    #
    # Python may suggest a shorter chained comparison:
    # 45 <= age <= 55
    #
    # That means the same thing.
    # The longer version is easier to understand while learning.
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")

    # If none of the age conditions above were True,
    # the user is an adult outside the free ride age range.
    else:
        bill = 12
        print("Adult tickets are $12.")

    # This asks if the user wants a photo.
    # The answer is stored as a string.
    wants_photo = input("Do you want a photo taken? Y or N. ")

    # == checks whether two values are equal.
    # This condition checks if the user typed exactly "Y".
    if wants_photo == "Y":
        # += adds to the current value of bill.
        # bill += 3 means bill = bill + 3.
        bill += 3

    # This f-string places the bill variable inside the printed sentence.
    print(f"Your final bill is ${bill}")

else:
    # This else belongs to the height check.
    # It runs if height >= 120 is False.
    print("Sorry, you have to grow taller before you can ride.")


# QUICK REVIEW
#
# Use and when every condition must be True.
# Example:
# age >= 45 and age <= 55
#
# Use or when at least one condition must be True.
# Example:
# day == "Saturday" or day == "Sunday"
#
# Use not when you want to reverse a condition.
# Example:
# not is_game_over
#
# Logical operators help make conditions more powerful
# without needing too many nested if statements.
