# BASIC DATA TYPES NOTES
#
# A data type tells Python what kind of value it is working with.
# Different data types behave differently.
#
# In this lesson, the main beginner data types are:
# 1. String  -> text
# 2. Integer -> whole number
# 3. Float   -> decimal number
# 4. Boolean -> True or False


# 1. STRINGS
#
# A string is text.
# Strings are created by putting characters inside quotation marks.
# The quotation marks tell Python, "treat this as text."
#
# Examples of strings:
# "Hello"
# "Aum"
# "123"
#
# Important:
# Even if a string contains numbers, Python still treats it as text
# if the value is inside quotation marks.

print("Hello")


# len() WITH STRINGS
#
# len() counts how many characters are inside a string.
# Characters include letters, numbers, spaces, and symbols.
#
# "hello" has 5 characters:
# h e l l o

print(len("hello"))  # Output: 5


# TYPE ERROR EXAMPLE
#
# len() works on strings because strings are made of characters.
# But len() does not work directly on an integer.
#
# This would crash:
# print(len(123))
#
# Python would give a TypeError because 123 is an integer,
# and integers do not have "characters" the same way strings do.


# SUBSCRIPTING STRINGS
#
# Subscript means getting one specific character from a string.
# We use square brackets [] for subscripting.
#
# The number inside the square brackets is called the index.
# The index tells Python which character position we want.
#
# Important:
# Programmers start counting from 0, not 1.
#
# For the string "Hello":
# H is at index 0
# e is at index 1
# l is at index 2
# l is at index 3
# o is at index 4

print("Hello"[0])  # Output: H
print("Hello"[4])  # Output: o


# NEGATIVE INDEXES
#
# Python also lets us count backwards from the end of a string.
# -1 means the last character.
# -2 means the second last character.
# -3 means the third last character.

print("Hello"[-1])  # Output: o
print("Hello"[-2])  # Output: l


# STRINGS WITH NUMBERS INSIDE
#
# "123" looks like a number to humans,
# but Python sees it as text because it is inside quotation marks.
#
# When we use + between strings, Python joins them together.
# This is called string concatenation.

print("123" + "345")  # Output: 123345

# Python does not calculate the above as math.
# It joins the text "123" and the text "345".


# 2. INTEGERS
#
# An integer is a whole number.
# Whole numbers do not have decimal points.
#
# Examples of integers:
# 5
# 123
# -10
# 0
#
# Integers are written without quotation marks.

print(123 + 345)  # Output: 468

# Because 123 and 345 are integers,
# Python performs real mathematical addition.


# LARGE INTEGERS WITH UNDERSCORES
#
# Humans often write large numbers with commas:
# 123,456,789
#
# In Python, do not use commas for this.
# Instead, you can use underscores to make large numbers easier to read.
#
# Python ignores the underscores when running the code.
# They are only there to help humans read the number.

large_number = 123_456_789
print(large_number)  # Output: 123456789


# 3. FLOATS
#
# A float is a number with a decimal point.
# Float is short for floating point number.
#
# Examples of floats:
# 3.14
# 0.5
# -7.25
#
# If a number has a decimal point, Python treats it as a float.

pi = 3.14159
print(pi)


# 4. BOOLEANS
#
# A Boolean can only have one of two values:
# True
# False
#
# Booleans are useful when a program needs to make decisions.
#
# Important:
# True and False must start with capital letters.
# They do not use quotation marks.
#
# These are Booleans:
# True
# False
#
# These are strings, not Booleans:
# "True"
# "False"

is_learning_python = True
print(is_learning_python)


# QUICK REVIEW
#
# "Hello" is a string because it is text in quotation marks.
# 123 is an integer because it is a whole number.
# 3.14 is a float because it has a decimal point.
# True is a Boolean because it is one of the two Boolean values.
#
# The same symbol can behave differently depending on the data type.
#
# With strings:
# "123" + "345" becomes "123345"
#
# With integers:
# 123 + 345 becomes 468
