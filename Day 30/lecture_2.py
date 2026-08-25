# ============================================================
# ERRORS AND EXCEPTIONS - REVISION NOTES
# ============================================================

from pathlib import Path


# 1. What is an exception?
# ------------------------
# An exception is an error that happens while a program is running.
# If it is not handled, Python stops the program and prints a traceback.

# Common exceptions:
#
# FileNotFoundError - trying to read a file that does not exist
# open("missing.txt", mode="r")
#
# KeyError - using a dictionary key that does not exist
# scores = {"Alice": 10}
# print(scores["Bob"])
#
# IndexError - using a list index that does not exist
# colours = ["red", "blue", "green"]
# print(colours[3])  # Valid indexes are 0, 1, and 2.
#
# TypeError - using an operation with incompatible data types
# print("Age: " + 25)  # A string and an integer cannot be joined directly.

# The error examples are commented out so this entire file remains runnable.


# 2. Handling an exception with try and except
# ---------------------------------------------
# Put code that may fail inside try.
# Put the recovery code inside except.
scores = {"Alice": 10}

try:
    print(scores["Bob"])
except KeyError:
    print("That name is not in the scores dictionary.")

# The program continues because the KeyError was handled.
print("The program is still running.")


# 3. Catch specific exceptions
# -----------------------------
# Avoid a bare "except:" because it catches almost every error and can hide
# unrelated bugs. Catch only the exception that the code can sensibly handle.
try:
    number = int("not a number")
except ValueError:
    print("The text could not be converted to an integer.")

# One try statement can have several specific except blocks:
def get_item(items, index):
    try:
        return items[index]
    except IndexError:
        return "That index is outside the list."
    except TypeError:
        return "The index must be an integer."


print(get_item(["apple", "banana"], 5))
print(get_item(["apple", "banana"], "one"))


# 4. Accessing the error message with "as"
# ------------------------------------------
# "as error" stores the exception object, including useful details.
try:
    print(scores["Charlie"])
except KeyError as error:
    print(f"The key {error} does not exist.")


# 5. try, except, else, and finally
# ---------------------------------
# try:    Run code that might fail.
# except: Run only if the matching exception occurs.
# else:   Run only if the try block succeeds without an exception.
# finally: Run no matter whether the try block succeeds or fails.

# Store the demonstration file beside this Python file.
file_path = Path(__file__).with_name("a_file.txt")
file = None

try:
    # Reading a missing file raises FileNotFoundError.
    file = open(file_path, mode="r", encoding="utf-8")

except FileNotFoundError:
    print("The file was missing, so a new one will be created.")

    # Write mode creates the file if it does not exist.
    # "with" automatically closes the new file afterward.
    with open(file_path, mode="w", encoding="utf-8") as new_file:
        new_file.write("Something")

else:
    # This runs only when the file opened successfully in the try block.
    contents = file.read()
    print(f"File contents: {contents}")

finally:
    # This block always runs. Close the file only if it was opened.
    if file is not None:
        file.close()
        print("The file was closed.")
    else:
        print("No open file needed to be closed.")

# First run:  the file is missing, so except creates it.
# Later runs: the file exists, so else reads it.
# Every run:  finally performs the appropriate cleanup.


# KEY POINTS TO REMEMBER
# ----------------------
# - Exceptions interrupt the normal flow of a program.
# - Handling expected exceptions lets a program fail gracefully or recover.
# - Keep the try block focused on the code that may fail.
# - Catch specific exceptions such as FileNotFoundError or KeyError.
# - Use "except ErrorType as error" to inspect the error details.
# - else runs after a successful try; finally always runs.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Do not use exceptions to hide programming mistakes. Fix unexpected bugs.
# 2. Avoid bare except clauses because they can hide the real problem.
# 3. Make sure a variable exists before using it in finally. Here, file starts
#    as None so the cleanup check is safe even when open() fails.
# 4. Opening a file with "w" creates it, but it also erases existing contents.
# 5. Prefer "with open(...)" for normal file work because it closes the file
#    automatically, even when an exception occurs.
