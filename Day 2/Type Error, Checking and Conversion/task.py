# TYPE ERRORS, TYPE CHECKING, AND TYPE CONVERSION NOTES
#
# This lesson is about how Python functions expect certain data types,
# how to check the data type of a value, and how to convert one type into another.


# 1. FUNCTIONS EXPECT CERTAIN DATA TYPES
#
# A function is like a small machine.
# You give it an input, it does some work, and then it gives back an output.
#
# Example:
# len("Hello") works because len() can count the characters in a string.

print(len("Hello"))  # Output: 5


# TYPE ERROR
#
# A TypeError happens when Python gets the wrong type of data for an operation.
#
# This would crash:
# print(len(123))
#
# Why?
# 123 is an integer.
# len() does not know how to count the "length" of an integer.
# len() works with things that have items inside them, like strings.
#
# "Hello" is a string with characters inside it.
# 123 is a number, not a collection of characters.


# 2. TYPE CHECKING WITH type()
#
# type() tells us what data type a value has.
# This is called type checking.
#
# To see the result in the console, we put type() inside print().

print(type("Hello"))  # Output: <class 'str'>
print(type(123))      # Output: <class 'int'>
print(type(3.14))     # Output: <class 'float'>
print(type(True))     # Output: <class 'bool'>


# WHAT THE OUTPUT MEANS
#
# <class 'str'> means string.
# <class 'int'> means integer.
# <class 'float'> means floating point number.
# <class 'bool'> means Boolean.


# 3. REVIEW OF THE FOUR BASIC DATA TYPES
#
# String:
# Text inside quotation marks.

example_string = "Hello"

# Integer:
# A whole number with no decimal point.

example_integer = 123

# Float:
# A number with a decimal point.

example_float = 3.14

# Boolean:
# A value that is either True or False.
# True and False must start with capital letters.
# They do not use quotation marks.

example_boolean = True

print(type(example_string))
print(type(example_integer))
print(type(example_float))
print(type(example_boolean))


# 4. SAME SYMBOL, DIFFERENT BEHAVIOR
#
# The + symbol behaves differently depending on the data type.

# With strings, + joins text together.
# This is called concatenation.

print("123" + "456")  # Output: 123456

# With integers, + does math addition.

print(123 + 456)  # Output: 579


# 5. TYPE CONVERSION / TYPE CASTING
#
# Type conversion means changing a value from one data type into another.
# It is also called type casting.
#
# Common conversion functions:
# int()   converts to an integer
# float() converts to a float
# str()   converts to a string
# bool()  converts to a Boolean


# CONVERTING STRINGS TO INTEGERS
#
# "123" is a string because it has quotation marks.
# int("123") converts it into the integer 123.

number_as_text = "123"
number_as_integer = int(number_as_text)

print(type(number_as_text))     # Output: <class 'str'>
print(type(number_as_integer))  # Output: <class 'int'>


# Before conversion, Python joins the strings:

print("123" + "456")  # Output: 123456

# After conversion, Python adds the numbers:

print(int("123") + int("456"))  # Output: 579


# VALUE ERROR
#
# Not every string can be converted into an integer.
#
# This would crash:
# print(int("ABC"))
#
# Why?
# "ABC" does not represent a number.
# Python cannot guess what number ABC should become.
#
# This causes a ValueError.
# A ValueError means the data type might be acceptable,
# but the actual value does not make sense for the conversion.


# 6. CONVERTING NUMBERS TO STRINGS
#
# Sometimes we need to convert a number into a string.
# This is common when using concatenation.

length_of_name = 3

# This would crash:
# print("Number of letters in your name: " + length_of_name)
#
# Why?
# The first part is a string.
# length_of_name is an integer.
# Python cannot concatenate a string and an integer directly.

# Fix:
# Convert the integer to a string using str().

print("Number of letters in your name: " + str(length_of_name))


# 7. BREAKING A PROBLEM INTO VARIABLES
#
# This is easier to understand than putting everything into one long line.
#
# Imagine the user typed the name "Angela".

name_of_the_user = "Angela"
length_of_name = len(name_of_the_user)

# name_of_the_user is a string.
# length_of_name is an integer because len() returns a whole number.

print(type(name_of_the_user))  # Output: <class 'str'>
print(type(length_of_name))    # Output: <class 'int'>

# To join the message with the number, convert the number to a string.

print("Number of letters in your name: " + str(length_of_name))


# 8. INTERACTIVE VERSION
#
# This is the version you would use if you wanted the program to ask the user.
# It is commented out so this notes file can run without waiting for input.
#
# name_of_the_user = input("Enter your name: ")
# length_of_name = len(name_of_the_user)
# print("Number of letters in your name: " + str(length_of_name))


# QUICK REVIEW
#
# len("Hello") works because "Hello" is a string.
# len(123) gives a TypeError because 123 is an integer.
#
# type(value) checks the data type.
# int(value) converts to an integer.
# float(value) converts to a float.
# str(value) converts to a string.
# bool(value) converts to a Boolean.
#
# "123" + "456" gives "123456" because both values are strings.
# int("123") + int("456") gives 579 because both values become integers.
#
# Use str() when you need to join a number into a sentence.
