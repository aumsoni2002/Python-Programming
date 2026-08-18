# ============================================================
# UNLIMITED POSITIONAL ARGUMENTS (*args) - REVISION NOTES
# ============================================================


# 1. Why use *args?
# -----------------
# A normal function has a fixed number of parameters.
def add_two_numbers(n1, n2):
    return n1 + n2


print(add_two_numbers(3, 5))  # Exactly two arguments are required.

# Sometimes we do not know how many values the caller will provide.
# *args lets a function accept any number of positional arguments.


# 2. Creating a function with *args
# ---------------------------------
def add(*args):
    # Python collects all positional arguments into a tuple named args.
    total = 0

    # Loop through every number in the tuple.
    for number in args:
        total += number

    return total


print(add(3, 5, 6))           # 14
print(add(3, 5, 6, 2, 1))     # 17
print(add(10))                 # 10
print(add())                   # 0 because there are no numbers to add.


# 3. What is args?
# ----------------
def inspect_arguments(*args):
    print(args)        # Displays all arguments as a tuple.
    print(type(args))  # Displays <class 'tuple'>.


inspect_arguments(3, 5, 6)  # args becomes (3, 5, 6).

# "args" is the usual name, but it is only a convention.
# The asterisk (*) is the part that gives the special behaviour.
def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(2, 3, 4))  # 24


# 4. Accessing *args by index
# ---------------------------
# args is a tuple, so individual values can be accessed using an index.
def show_positions(*args):
    print(f"First argument: {args[0]}")   # Index 0 is the first item.
    print(f"Second argument: {args[1]}")  # Index 1 is the second item.


show_positions(3, 5, 6)

# The order matters because *args stores positional arguments.
# In the call above, args[0] is 3 and args[1] is 5.


# KEY POINTS TO REMEMBER
# ----------------------
# - *args allows zero, one, or many positional arguments.
# - Python packs the supplied arguments into a tuple.
# - A tuple can be looped through and accessed by index.
# - The conventional name is args, but *numbers would also work.
# - The asterisk is essential; the parameter name is your choice.
# - These are called unlimited positional arguments because their order matters.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Do not forget the asterisk in the function definition.
#    Without it, the function expects one argument instead of many.
#
# 2. Avoid using "sum" as a variable name. sum() is already a Python function.
#    Names such as "total" are clearer and do not hide the built-in function.
#
# 3. Check that an index exists before using it. This call would fail because
#    show_positions() expects at least two items:
# show_positions(10)  # IndexError when the function tries to read args[1].
#
# 4. *args itself does not check data types. Passing text to add() may cause a
#    TypeError because numbers and strings cannot always be added together.
