# ============================================================
# RAISING YOUR OWN EXCEPTIONS - REVISION NOTES
# ============================================================


# 1. What does raise do?
# ----------------------
# Python automatically raises exceptions for errors such as missing files.
# The raise keyword lets us deliberately create an exception when our own
# program rules are broken.
#
# General pattern:
# raise ExceptionType("Helpful error message")


# 2. A simple raise example
# -------------------------
def check_age(age):
    if age < 0:
        # The value is a valid integer, but it is not a sensible age.
        raise ValueError("Age cannot be negative.")

    return age


print(check_age(25))  # Valid, so the function returns 25.

# Catch the deliberately raised exception so this demo can keep running.
try:
    check_age(-5)
except ValueError as error:
    print(f"Invalid age: {error}")


# 3. Valid Python can still contain invalid data
# ------------------------------------------------
# Python can calculate with a height of 45 metres because 45 is a valid number.
# However, that is not a realistic human height. Validation checks the meaning
# of data, not just whether Python can process it.


# 4. BMI example with validation
# ------------------------------
def calculate_bmi(height, weight):
    """Return BMI after checking that height and weight are sensible."""

    if height <= 0:
        raise ValueError("Height must be greater than 0 metres.")

    if height > 3:
        raise ValueError("Human height should not be over 3 metres.")

    if weight <= 0:
        raise ValueError("Weight must be greater than 0 kilograms.")

    # ** means "raised to a power". BMI = weight / height squared.
    return weight / height ** 2


# A valid calculation continues normally.
bmi = calculate_bmi(height=1.75, weight=67)
print(f"BMI: {bmi:.1f}")

# An unrealistic height raises ValueError before an incorrect BMI is returned.
try:
    calculate_bmi(height=45, weight=67)
except ValueError as error:
    print(f"Could not calculate BMI: {error}")


# 5. Using raise with user input
# ------------------------------
# input() returns text, so convert it before calling the function:
#
# height = float(input("Height in metres: "))
# weight = float(input("Weight in kilograms: "))
#
# try:
#     print(calculate_bmi(height, weight))
# except ValueError as error:
#     print(error)
#
# float() can also raise ValueError if the user enters non-numeric text.


# KEY POINTS TO REMEMBER
# ----------------------
# - raise deliberately stops normal execution and creates an exception.
# - Raise an exception when data breaks an important program rule.
# - Choose a suitable built-in exception class.
# - ValueError is useful when the data type is correct but its value is invalid.
# - Add a clear message that explains what went wrong.
# - A raised exception can be handled with try and except.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Raise an exception object, not a plain string:
#    raise ValueError("Invalid value")  # Correct
#    raise "Invalid value"              # TypeError
#
# 2. If an exception is not caught, it stops the program and shows a traceback.
#
# 3. Do not use raise for normal decisions that an if/else can handle easily.
#    Use it when the function cannot safely produce a valid result.
#
# 4. Put ** 2 on the height: weight / height ** 2.
#    Writing weight / height * height calculates something different because
#    multiplication and division are evaluated from left to right.
