# Python Revision Notes: Multiple Return Statements

# ------------------------------------------------------------
# 1. What does return do?
# ------------------------------------------------------------

# return sends a value back from a function.
# It also ends the function immediately.


def add_numbers(a, b):
    result = a + b
    return result  # The function stops here.
    print("This line will never run.")  # Code after return is skipped.


total = add_numbers(3, 4)
print(total)


# Key points:
# - return gives an output.
# - return exits the function.
# - Any code after return in the same block will not run.


# ------------------------------------------------------------
# 2. Multiple return statements
# ------------------------------------------------------------

# A function can have more than one return statement.
# This is useful when different situations need different outputs.


def check_age(age):
    if age >= 18:
        return "You are an adult."
    else:
        return "You are not an adult yet."


print(check_age(20))
print(check_age(15))


# Key points:
# - Only one return statement runs each time the function is called.
# - The return that runs depends on the condition.
# - Once a return runs, the function ends.


# ------------------------------------------------------------
# 3. Early return
# ------------------------------------------------------------

# An early return stops the function before the rest of the code runs.
# This is useful when the input is missing or invalid.


def format_name(f_name, l_name):
    # If either input is empty, stop the function early.
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."

    # These lines only run if both inputs are not empty.
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("AnGEla", "YU"))
print(format_name("", "Smith"))
print(format_name("John", ""))


# Key points:
# - Early return avoids doing unnecessary work.
# - It can prevent errors or bad results.
# - Returning a helpful message is clearer than returning nothing.


# ------------------------------------------------------------
# 4. Empty return
# ------------------------------------------------------------

# A return statement can be used without a value.
# In that case, Python returns None.


def stop_if_empty(text):
    if text == "":
        return  # This returns None.

    return text.title()


print(stop_if_empty("hello"))
print(stop_if_empty(""))


# Beginner tip:
# None means "no value".
# If you print the result of an empty return, you will see None.


# ------------------------------------------------------------
# 5. Using input with a function
# ------------------------------------------------------------

# The course example used input() to collect names from the user.
# This version is commented out so the file can run without waiting for typing.

# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# print(format_name(first_name, last_name))


# Instead, here is a runnable example with stored values:

first_name = "aUm"
last_name = "sHaH"

formatted_name = format_name(first_name, last_name)
print(formatted_name)


# ------------------------------------------------------------
# 6. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Expecting code after return to run.


def example():
    return "Finished"
    # This code is unreachable because return already ended the function.


print(example())


# Mistake 2: Returning nothing by accident.


def maybe_returns_text(text):
    if text == "":
        return
    return text


result = maybe_returns_text("")
print(result)

# This prints None because the function returned without a value.


# Mistake 3: Not handling empty input.


def format_name_without_check(f_name, l_name):
    # This works, but empty input gives an empty-looking result.
    return f"{f_name.title()} {l_name.title()}"


print(format_name_without_check("", ""))

# Better: check for empty input and return a clear message.
print(format_name("", ""))


# ------------------------------------------------------------
# 7. Mini summary
# ------------------------------------------------------------

# - return gives a function an output.
# - return also ends the function immediately.
# - A function can have multiple return statements.
# - Early return is useful for stopping when input is invalid.
# - An empty return gives back None.
# - Return a useful message when it helps explain what went wrong.
