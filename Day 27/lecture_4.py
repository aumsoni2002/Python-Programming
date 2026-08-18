# ============================================================
# DEFAULT ARGUMENTS AND KEYWORD ARGUMENTS - REVISION NOTES
# ============================================================


# 1. Parameters and arguments
# ---------------------------
# A parameter is a variable listed when a function is defined.
# An argument is the actual value passed in when the function is called.
def show_total(a, b, c):  # a, b, and c are parameters.
    print(a + b + c)


show_total(1, 2, 3)  # 1, 2, and 3 are arguments. Prints 6.


# 2. Keyword arguments
# --------------------
# A keyword argument includes the parameter's name when calling a function.
# This makes the call clearer and allows the arguments to be given in a
# different order.
show_total(c=3, a=1, b=2)  # Still prints 6.

# Key points:
#   - Positional arguments are matched by their position.
#   - Keyword arguments are matched by their parameter name.
#   - Write keyword arguments as name=value.


# 3. Default argument values
# --------------------------
# A default value is used when the caller does not provide that argument.
def calculate(a=1, b=2, c=3):
    print(f"a={a}, b={b}, c={c}, total={a + b + c}")


calculate()       # Uses all defaults: a=1, b=2, c=3.
calculate(b=5)    # Changes only b; a and c keep their defaults.
calculate(10, 20, 30)  # Replaces all three defaults by position.

# Default values are useful when the same settings are used most of the time.
# The caller only needs to supply values that should be different.


# 4. Required and optional arguments
# ----------------------------------
# A parameter without a default value is required.
# A parameter with a default value is optional.
def write_message(message, uppercase=False):
    # "message" is required; "uppercase" is optional.
    if uppercase:
        message = message.upper()
    print(message)


write_message("Hello")                  # Uses uppercase=False.
write_message("Hello", uppercase=True)  # Overrides the default.

# This would cause a TypeError because the required argument is missing:
# write_message()


# 5. Connection to Tkinter and Turtle
# -----------------------------------
# Library functions often have required inputs plus many optional settings.
# For example, a Turtle write method needs text, but settings such as its font
# can have defaults. Tkinter's pack() can also accept optional settings:
#
# my_label.pack()             # Use pack's default layout settings.
# my_label.pack(side="left") # Override only the side setting.
#
# If a function signature shows **kw or **kwargs, it can accept extra keyword
# arguments. This is why some options may be valid even when they are not all
# listed separately in the function hint.


# KEY POINTS TO REMEMBER
# ----------------------
# - Required parameters must be given a value.
# - Optional parameters already have a default value.
# - Use a keyword argument to override one specific default.
# - Keyword arguments improve readability and can be supplied in any order.
# - In a function definition, required parameters must normally come before
#   parameters with defaults.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Use one equals sign for keyword/default arguments: b=5, not b==5.
# 2. Spell parameter names exactly when using keyword arguments.
# 3. Do not omit a required argument, or Python raises TypeError.
# 4. A non-default parameter cannot follow a default parameter:
#
# def broken(a=1, b):  # SyntaxError: required parameter follows a default.
#     pass
#
# Correct version:
def correct_order(b, a=1):
    print(a + b)


correct_order(5)  # b is required; a uses its default. Prints 6.
