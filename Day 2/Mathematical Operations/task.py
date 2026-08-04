# MATHEMATICAL OPERATIONS NOTES
#
# Python can do normal math operations.
# The symbols we use in Python are called operators.
#
# Some operators behave differently depending on the data type.
# Example:
# "123" + "456" joins strings together.
# 123 + 456 adds numbers together.


# 1. ADDITION
#
# The plus sign + adds numbers together.

print(7 + 3)  # Output: 10


# 2. SUBTRACTION
#
# The minus sign - subtracts the second number from the first number.

print(7 - 3)  # Output: 4


# 3. MULTIPLICATION
#
# In Python, multiplication uses the asterisk symbol *.
# We do not use x for multiplication in Python code.

print(3 * 2)  # Output: 6


# 4. DIVISION
#
# Division uses the forward slash /.
#
# Important:
# Normal division always gives a float in Python.
# A float is a number with a decimal point.

print(6 / 3)        # Output: 2.0
print(type(6 / 3))  # Output: <class 'float'>

# Even though 6 divided by 3 is exactly 2,
# Python still gives 2.0 because / always returns a float.
#
# This is called implicit type casting.
# "Implicit" means Python does it automatically.


# 5. FLOOR DIVISION
#
# Floor division uses two forward slashes //.
# It gives a whole number result by removing the decimal part.

print(6 // 3)        # Output: 2
print(type(6 // 3))  # Output: <class 'int'>

# Be careful:
# Floor division does not round normally.
# It removes the decimal part.

print(5 / 3)   # Output: 1.6666666666666667
print(5 // 3)  # Output: 1

# 5 / 3 is about 1.66.
# 5 // 3 removes the decimal part and gives 1.
# This can be useful, but it can also lose important information.


# 6. EXPONENTS
#
# Exponents use two asterisks **.
# This means "to the power of".

print(2 ** 2)  # Output: 4
print(2 ** 3)  # Output: 8

# 2 ** 2 means 2 to the power of 2.
# That is the same as 2 * 2.
#
# 2 ** 3 means 2 to the power of 3.
# That is the same as 2 * 2 * 2.


# 7. ORDER OF OPERATIONS
#
# When there is more than one operation on the same line,
# Python follows a priority order.
#
# The common memory trick is PEMDAS:
#
# P = Parentheses        ()
# E = Exponents          **
# M = Multiplication     *
# D = Division           /
# A = Addition           +
# S = Subtraction        -
#
# Multiplication and division have the same priority.
# When operators have the same priority, Python goes from left to right.
#
# Addition and subtraction also have the same priority.
# They also go from left to right.


# Example:

print(3 * 3 + 3 / 3 - 3)  # Output: 7.0

# Step-by-step:
# 3 * 3 happens first because multiplication has high priority.
# That becomes 9.
#
# 3 / 3 happens next because division also has high priority.
# That becomes 1.0.
#
# Now the expression is:
# 9 + 1.0 - 3
#
# Then Python works left to right:
# 9 + 1.0 = 10.0
# 10.0 - 3 = 7.0


# 8. USING PARENTHESES TO CHANGE PRIORITY
#
# Parentheses happen first.
# Use parentheses when you want a certain part of the calculation
# to happen before everything else.

print(3 * (3 + 3) / 3 - 3)  # Output: 3.0

# Step-by-step:
# (3 + 3) happens first because it is inside parentheses.
# That becomes 6.
#
# Then:
# 3 * 6 / 3 - 3
#
# Multiplication and division go left to right:
# 3 * 6 = 18
# 18 / 3 = 6.0
#
# Then subtraction:
# 6.0 - 3 = 3.0


# 9. QUICK REVIEW
#
# +  addition
# -  subtraction
# *  multiplication
# /  division, always returns a float
# // floor division, removes the decimal part
# ** exponent, raises a number to a power
#
# Use parentheses () when you want to control which calculation happens first.
