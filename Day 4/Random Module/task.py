# RANDOM MODULE NOTES
#
# Randomization means making something unpredictable.
# This is useful in games and simulations.
#
# Examples:
# - A coin toss should randomly be heads or tails.
# - A dice roll should randomly be 1 to 6.
# - A game should not always give the same enemy, block, or reward.
#
# Computers are deterministic.
# That means they normally follow exact instructions and do predictable things.
#
# Python uses a pseudo-random number generator.
# "Pseudo" means it is not truly random like nature,
# but it is random enough for normal programs and games.


# import random gives this file access to Python's random module.
# A module is a separate file or collection of code that contains useful tools.
# The Python team already wrote the random module for us,
# so we do not have to build random number logic ourselves.
import random

# This imports our own module called my_module.py.
# Because my_module.py is in the same folder as this file,
# Python can import it by name.
#
# After importing it, we can access things inside it using dot notation.
# Example:
# my_module.my_favourite_number
import my_module


# DOT NOTATION
#
# Dot notation means using a dot . to get something from inside a module.
#
# random.randint means:
# Go into the random module and use the randint function.
#
# my_module.my_favourite_number means:
# Go into my_module and get the variable called my_favourite_number.


# RANDOM INTEGERS WITH randint()
#
# randint(a, b) gives a random integer between a and b.
# Integer means a whole number.
#
# Important:
# randint includes both end numbers.
#
# random.randint(1, 10) can give:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10
#
# The 1 is included.
# The 10 is included.

# random_integer = random.randint(1, 10)
# print(random_integer)


# USING OUR OWN MODULE
#
# This prints the variable stored inside my_module.py.
# In my_module.py, there is a variable:
# my_favourite_number = 3.1415
#
# This shows that modules can help split code into separate files.
#
# For small beginner programs, one file is fine.
# For bigger programs, modules help keep code organized.

# print(my_module.my_favourite_number)


# RANDOM FLOATS WITH random()
#
# random.random() gives a random float between 0 and 1.
#
# A float is a number with a decimal point.
#
# The possible range is:
# 0.0 up to, but not including, 1.0
#
# This means 0 is possible,
# but 1 is not included.
#
# random.random() does not need any inputs,
# but it still needs parentheses to call the function.

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)


# EXPANDING THE RANGE OF random()
#
# Since random.random() gives a number from 0 to less than 1,
# multiplying it changes the range.
#
# Example:
# random.random() * 10
#
# This gives a random float from 0 to less than 10.
#
# The lower end is still 0.
# The upper end becomes close to 10, but not exactly 10.

# random_number_0_to_10 = random.random() * 10
# print(random_number_0_to_10)


# RANDOM FLOATS WITH uniform()
#
# random.uniform(a, b) gives a random float between a and b.
#
# Example:
# random.uniform(1, 10)
#
# This gives a random decimal number somewhere between 1 and 10.
#
# The exact edge behavior can depend on floating point rounding,
# so for simple beginner work, it is often easier to remember:
# uniform creates a random float in the range you give it.

# random_float = random.uniform(1, 10)
# print(random_float)


# HEADS OR TAILS CHALLENGE
#
# Goal:
# Make a program that randomly prints either "Heads" or "Tails".
#
# We need two possible random values:
# 0 and 1
#
# We can use:
# random.randint(0, 1)
#
# Because randint includes both ends,
# this can return either 0 or 1.

random_integer = random.randint(0, 1)

# This if statement checks which random number was generated.
#
# == means "is equal to".
# It checks whether random_integer is equal to 1.
#
# If random_integer is 1, we print Heads.
# Otherwise, the only other possible value is 0,
# so the else block prints Tails.
if random_integer == 1:
    print("Heads")
else:
    print("Tails")


# QUICK REVIEW
#
# import random
# Lets us use Python's random module.
#
# random.randint(1, 10)
# Gives a random whole number from 1 to 10, including both 1 and 10.
#
# random.random()
# Gives a random decimal number from 0 up to, but not including, 1.
#
# random.random() * 10
# Gives a random decimal number from 0 up to, but not including, 10.
#
# random.uniform(1, 10)
# Gives a random decimal number between 1 and 10.
#
# import my_module
# Lets us use code from our own Python file called my_module.py.
#
# module_name.something_inside_it
# This is dot notation.
