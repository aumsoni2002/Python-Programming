# NESTED IF / ELSE AND ELIF NOTES
#
# In the previous lesson, we checked one condition:
# Is the user's height at least 120 cm?
#
# Now we want to check another condition after that:
# How old is the user?
#
# This means the program has more decisions to make.


# This prints a welcome message before asking any questions.
print("Welcome to the rollercoaster!")

# input() asks the user for their height.
# input() gives back a string, so int() converts it into a whole number.
# We need a number because we are going to compare it with 120.
height = int(input("What is your height in cm? "))


# This is the first condition.
# It checks whether the user is tall enough to ride.
#
# >= means "greater than or equal to".
# So height >= 120 means:
# Is the user's height 120 cm or taller?
#
# If this is False, the program skips everything inside this if block
# and goes straight to the else block at the bottom.
if height >= 120:
    # This line only runs if the user is tall enough.
    print("You can ride the rollercoaster")

    # NESTED IF STATEMENT
    #
    # A nested if statement is an if statement inside another if statement.
    #
    # This age check is nested inside the height check.
    # That means Python only asks for the user's age if they are tall enough.
    #
    # If height >= 120 is False, this age input never happens.
    age = int(input("What is your age? "))

    # ELIF
    #
    # elif means "else if".
    #
    # We use elif when there are more than two possible outcomes.
    #
    # For this rollercoaster ticket:
    # - Under 12 years old pays $5
    # - 12 to 18 years old pays $7
    # - Over 18 years old pays $12

    # This checks the first age condition.
    # If the user is younger than 12, they pay the child price.
    if age < 12:
        print("Please pay $5.")

    # This only gets checked if age < 12 was False.
    #
    # <= means "less than or equal to".
    # age <= 18 catches users who are 12 through 18.
    #
    # Why?
    # If the user was younger than 12, the first if block already handled them.
    # So by the time Python reaches this elif, we already know age is not under 12.
    elif age <= 18:
        print("Please pay $7.")

    # else catches everyone who did not match the earlier conditions.
    #
    # In this case:
    # If age is not under 12,
    # and age is not 18 or under,
    # then the user must be over 18.
    else:
        print("Please pay $12.")
else:
    # This else belongs to the height check.
    # It runs if height >= 120 is False.
    #
    # Important:
    # This else lines up with the first if statement,
    # not with the nested age if statement.
    print("Sorry you have to grow taller before you can ride.")


# HOW PYTHON THINKS THROUGH THIS PROGRAM
#
# 1. Ask for height.
# 2. Check if height >= 120.
# 3. If height is too short:
#    Print the "grow taller" message and stop.
# 4. If height is tall enough:
#    Ask for age.
# 5. Check age:
#    If age < 12, ticket is $5.
#    Elif age <= 18, ticket is $7.
#    Else, ticket is $12.


# IF / ELIF / ELSE STRUCTURE
#
# General pattern:
#
# if condition_1:
#     do_this_if_condition_1_is_true
# elif condition_2:
#     do_this_if_condition_1_is_false_but_condition_2_is_true
# else:
#     do_this_if_all_conditions_above_are_false
#
# You can have as many elif blocks as you need.
# You can only have one final else block.


# IMPORTANT INDENTATION REMINDER
#
# Indentation controls which block code belongs to.
#
# The age if / elif / else is indented inside the height if block.
# That is what makes it nested.
#
# The final else is not indented as far as the age logic.
# It lines up with the original height if.
#
# If indentation is wrong, Python may give an IndentationError
# or the program may make decisions in the wrong place.
