# NUMBER MANIPULATION NOTES
#
# This lesson is about controlling number output and making code shorter.
# The main topics are:
# 1. Flooring numbers with int()
# 2. Rounding numbers with round()
# 3. Assignment operators like +=
# 4. f-strings for mixing text with variables


# 1. WHY NUMBER MANIPULATION MATTERS
#
# Some calculations create long decimal numbers.
# For example, BMI calculations often produce many digits after the decimal.
# That can be hard for users to read.

bmi = 84 / 1.65 ** 2
print(bmi)

# The output is a long float:
# 30.85399449035813
#
# A float is a number with a decimal point.


# 2. FLOORING WITH int()
#
# int() converts a number into an integer.
# An integer is a whole number with no decimal point.
#
# When int() receives a float, it removes everything after the decimal point.
# This is called flooring.
#
# Important:
# Flooring does not round the number.
# It simply cuts off the decimal part.

print(int(bmi))  # Output: 30

# Example:
# int(3.9) gives 3
# It does not give 4, because int() does not round up.

print(int(3.9))  # Output: 3


# 3. ROUNDING WITH round()
#
# round() rounds a number in the normal mathematical way.
# If the decimal part is close enough to the next whole number,
# round() moves it up.
#
# If the decimal part is lower,
# round() moves it down.

print(round(bmi))  # Output: 31

# Example:

print(round(3.9))  # Output: 4
print(round(3.3))  # Output: 3


# 4. ROUNDING TO A CERTAIN NUMBER OF DECIMAL PLACES
#
# round() can take two inputs:
# 1. The number you want to round
# 2. How many decimal places you want
#
# Format:
# round(number, decimal_places)

print(round(bmi, 2))  # Output: 30.85

# This is useful for values like:
# money
# measurements
# percentages
# BMI
#
# Example:
# round(3.14159, 2) gives 3.14

print(round(3.14159, 2))  # Output: 3.14


# 5. ASSIGNMENT OPERATORS
#
# Sometimes you want to update a variable based on its old value.
#
# Example:
# A game score starts at 0.
# When the player earns a point, the score should go up by 1.

score = 0

# Longer way:
# score = score + 1
#
# This means:
# Take the old value of score, add 1, and store the result back in score.

score = score + 1
print(score)  # Output: 1


# Shorter way:
# += means "add this amount to the existing value".

score += 1
print(score)  # Output: 2

# score += 1 is the same idea as:
# score = score + 1


# Other assignment operators:

score -= 1  # Same as score = score - 1
print(score)  # Output: 1

score *= 5  # Same as score = score * 5
print(score)  # Output: 5

score /= 2  # Same as score = score / 2
print(score)  # Output: 2.5

# Important:
# score /= 2 uses normal division,
# so the result becomes a float.


# 6. WHY CONCATENATION CAN BE ANNOYING
#
# If we want to join text with a number, normal string concatenation can fail.

score = 0

# This would crash:
# print("Your score is " + score)
#
# Why?
# "Your score is " is a string.
# score is an integer.
# Python cannot join a string and an integer with + directly.

# One fix is to convert the number to a string:

print("Your score is " + str(score))

# This works, but it can become messy when there are many variables.


# 7. F-STRINGS
#
# An f-string makes it easy to put variables inside a string.
#
# To create an f-string:
# Put the letter f directly before the opening quotation mark.
#
# Then put variable names inside curly braces: {}

score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}")

# Python automatically converts the variable to text inside the f-string.
# We do not need to use str(score).


# 8. MIXING DIFFERENT DATA TYPES IN AN F-STRING
#
# f-strings are useful because they can include many data types:
# integers
# floats
# Booleans
# strings

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")

# In the line above:
# score is an integer.
# height is a float.
# is_winning is a Boolean.
#
# The f-string converts them into text for printing.


# 9. F-STRING EXAMPLES

name = "Aum"
age = 12
favorite_number = 7

print(f"Hello {name}, you are {age} years old.")
print(f"Your favorite number is {favorite_number}.")
print(f"Next year, you will be {age + 1} years old.")

# You can even put simple calculations inside curly braces.
# In this example:
# {age + 1} calculates the age for next year.


# QUICK REVIEW
#
# int(3.9) gives 3 because it cuts off the decimal part.
# round(3.9) gives 4 because it rounds normally.
# round(3.14159, 2) gives 3.14 because it rounds to 2 decimal places.
#
# score += 1 means score = score + 1.
# score -= 1 means score = score - 1.
# score *= 2 means score = score * 2.
# score /= 2 means score = score / 2.
#
# f"Your score is {score}" lets you place variables inside strings.
# f-strings are cleaner than using lots of + signs and str() conversions.

6 + 4 / 2 - (1 * 2)
6 + 4 / 2 - 2
6 + 2 - 2
