# Python Revision Notes: Functions with Inputs

# ------------------------------------------------------------
# 1. What is a function?
# ------------------------------------------------------------

# A function is a named block of code.
# It lets us group instructions together and reuse them later.

# Key points:
# - Use the def keyword to create a function.
# - The function name should describe what the function does.
# - The code inside the function must be indented.
# - A function does not run until you call it.
# - To call a function, write its name followed by parentheses.


def greet():
    # These lines belong to the function because they are indented.
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


# Calling the function runs all the code inside it.
greet()


# Beginner tip:
# If you define a function but never call it, nothing will happen.


# ------------------------------------------------------------
# 2. Functions can be reused
# ------------------------------------------------------------

# Every time we call greet(), Python runs the same three print statements.

greet()

# This is useful because we do not need to rewrite the same code again and again.


# ------------------------------------------------------------
# 3. Functions with inputs
# ------------------------------------------------------------

# Sometimes we want a function to do almost the same thing,
# but with a small change each time.
#
# Example:
# - "Hello Angela"
# - "Hello Jack"
# - "Hello Maria"
#
# To do this, we put a variable name inside the function's parentheses.
# This variable is called a parameter.


def greet_with_name(name):
    # name stores the value given when the function is called.
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# "Angela" is passed into the function.
# Inside the function, name becomes "Angela".
greet_with_name("Angela")

# We can call the same function with a different value.
greet_with_name("Jack")


# Key points:
# - Inputs make functions more flexible.
# - The value you pass in can change what the function does.
# - Use f-strings to place variables inside strings.


# ------------------------------------------------------------
# 4. Parameter vs Argument
# ------------------------------------------------------------

# These two words are important:
#
# Parameter:
# - The variable name inside the function definition.
# - Example: name in def greet_with_name(name)
#
# Argument:
# - The actual value passed into the function when it is called.
# - Example: "Angela" in greet_with_name("Angela")


def my_function(something):
    # something is the parameter.
    print(f"The input was: {something}")


# 123 is the argument.
my_function(123)


# Quick memory trick:
# - Parameter = placeholder name used by the function.
# - Argument = actual value given to the function.


# ------------------------------------------------------------
# 5. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Forgetting the parentheses when calling a function.

# greet        # This only refers to the function.
# greet()      # This actually runs the function.


# Mistake 2: Forgetting to pass an argument.

# greet_with_name()
# This would cause an error because Python expects a value for name.


# Mistake 3: Forgetting the colon after the function definition.

# def bad_function()
#     print("This will not work")

# Correct version:


def good_function():
    print("This works because the colon is included.")


good_function()


# Mistake 4: Wrong indentation.

# Python uses indentation to know what belongs inside the function.


def correctly_indented():
    print("This line is inside the function.")


print("This line is outside the function.")


# ------------------------------------------------------------
# 6. Mini summary
# ------------------------------------------------------------

# - Functions help us reuse code.
# - Use def to define a function.
# - Call a function with its name and parentheses.
# - Parameters are variable names used inside the function.
# - Arguments are the real values passed into the function.
# - Functions with inputs are more flexible than functions that always do the same thing.
