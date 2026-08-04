# Python Revision Notes: Debugging - Fix the Errors

# ------------------------------------------------------------
# 1. Fix visible errors first
# ------------------------------------------------------------

# Sometimes your editor shows an error before you even run the code.
# Fix these first because Python may not be able to run the file at all.


# Broken version from the lesson:

# age = int(input("How old are you? "))
# if age > 18:
# print("You can drive at age {age}.")


# Problem:
# The print line is not indented.
# Code inside an if statement must be indented.


age = 20

if age > 18:
    # This line is indented, so it belongs to the if statement.
    print("You can drive.")


# Key points:
# - Code inside if, for, while, and functions must be indented.
# - Indentation tells Python which lines belong to the block.
# - Fix editor warnings and syntax errors before debugging logic.


# ------------------------------------------------------------
# 2. Console errors
# ------------------------------------------------------------

# Some errors only appear when the program runs.
# These errors show up in the console.


# Example:

# age = int("twelve")

# This would cause:
# ValueError: invalid literal for int() with base 10: 'twelve'


# Why?
# int() can convert "12" into 12.
# But int() cannot convert "twelve" into 12.

print(int("12"))


# Beginner tip:
# When you get a console error, read the error type and message.
# Search the error message with the word Python if you do not understand it.


# ------------------------------------------------------------
# 3. Catching errors with try/except
# ------------------------------------------------------------

# A try/except block lets us handle an error without crashing the program.
#
# Put risky code inside try.
# Put the backup plan inside except.


def convert_age(age_text):
    try:
        # This line might fail if age_text is not a number.
        age_number = int(age_text)
    except ValueError:
        # This runs if int(age_text) causes a ValueError.
        return "Invalid number. Please type digits, such as 15."
    else:
        # This runs only if there was no error.
        return age_number


print(convert_age("12"))
print(convert_age("twelve"))


# Key points:
# - ValueError happens when a value has the wrong format.
# - try/except can stop the program from crashing.
# - Handle only the error you expect when possible.


# ------------------------------------------------------------
# 4. Interactive version
# ------------------------------------------------------------

# This version is commented out so the file can run without waiting for input.

# age_text = input("How old are you? ")
#
# try:
#     age = int(age_text)
# except ValueError:
#     print("You typed an invalid number. Please try a numerical response such as 15.")
# else:
#     if age > 18:
#         print(f"You can drive at age {age}.")


# ------------------------------------------------------------
# 5. Errors vs bugs
# ------------------------------------------------------------

# Not all bugs create error messages.
# Sometimes the code runs, but the output is wrong.


age = 21

# Buggy version:
print("You can drive at age {age}.")

# Fixed version:
print(f"You can drive at age {age}.")


# Why?
# Without the f before the string, Python treats {age} as normal text.
# With an f-string, Python inserts the value of the variable.


# ------------------------------------------------------------
# 6. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Missing indentation.

# if age > 18:
# print("Can drive")

# Correct:
if age > 18:
    print("Can drive")


# Mistake 2: Forgetting the f in an f-string.

name = "Aum"
print("Hello {name}")
print(f"Hello {name}")


# Mistake 3: Assuming user input is always valid.

bad_input = "abc"
result = convert_age(bad_input)
print(result)


# Beginner tip:
# Users may type unexpected things.
# If your program converts input, think about what happens with invalid input.


# ------------------------------------------------------------
# 7. Mini summary
# ------------------------------------------------------------

# - Fix editor errors before continuing.
# - Read console errors carefully.
# - Search the error type and message when needed.
# - int("12") works, but int("twelve") causes a ValueError.
# - Use try/except to handle expected errors.
# - Some bugs do not show errors, so check whether the output is correct.
# - Use f-strings when you want to insert variables into strings.
