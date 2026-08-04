# Python Revision Notes: Docstrings

# ------------------------------------------------------------
# 1. What is a docstring?
# ------------------------------------------------------------

# A docstring is a short piece of documentation inside your code.
# It explains what a function, class, or module does.
#
# Docstrings are useful because editors can show them as help text,
# just like Python shows help for built-in functions such as len().


def format_name(f_name, l_name):
    """Take a first and last name and return them in title case."""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_name = format_name("AnGeLa", "YU")
print(formatted_name)


# Key points:
# - A docstring uses triple quotes: """Like this."""
# - It must be the first indented line inside the function.
# - It should briefly explain what the function does.


# ------------------------------------------------------------
# 2. Docstrings can be multi-line
# ------------------------------------------------------------

# Triple quotes allow the documentation to go across multiple lines.
# This is useful when a function needs a little more explanation.


def calculate_name_length(f_name, l_name):
    """
    Format a first and last name into title case.
    Return the number of characters in the formatted full name.
    """
    full_name = format_name(f_name, l_name)
    return len(full_name)


length = calculate_name_length("john", "smith")
print(length)


# Key points:
# - Multi-line docstrings still use triple quotes.
# - Keep them clear and short.
# - Describe the result the function returns when useful.


# ------------------------------------------------------------
# 3. Viewing a function's docstring
# ------------------------------------------------------------

# Python stores a function's docstring in __doc__.
# This lets us print the documentation for our own functions.

print(format_name.__doc__)
print(calculate_name_length.__doc__)


# Built-in functions also have documentation.
print(len.__doc__)


# Beginner tip:
# In many code editors, docstrings appear when you hover over
# or start typing a function call.


# ------------------------------------------------------------
# 4. Docstrings vs comments
# ------------------------------------------------------------

# Comments are notes for humans reading the code.
# Python ignores comments completely.


def greet(name):
    """Return a greeting for the given name."""
    # This comment explains the next line of code.
    return f"Hello {name}"


print(greet("Aum"))


# Difference:
# - Docstrings document what a function does.
# - Comments explain small details inside the code.
# - Docstrings can be shown by help tools and editors.
# - Comments are only visible in the source code.


# ------------------------------------------------------------
# 5. Triple quotes are not the best multi-line comment style
# ------------------------------------------------------------

# You may see triple quotes used like a multi-line comment:

"""
This text is not assigned to a variable,
so it does not affect the program.
But official Python style prefers normal # comments for comments.
"""

# Better for normal comments:
# Use # on each line.
# In most editors, select the lines and press Ctrl + / on Windows.


# ------------------------------------------------------------
# 6. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Putting the docstring in the wrong place.


def wrong_docstring_example():
    name = "Angela"
    """This is not treated as the function docstring because it is not first."""
    return name


print(wrong_docstring_example.__doc__)

# The result is None because the triple-quoted text was not the first line.


# Mistake 2: Writing a docstring that is too vague.


def add(a, b):
    """Does something."""
    return a + b


print(add(2, 3))

# Better docstring:


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add_numbers(2, 3))


# ------------------------------------------------------------
# 7. Mini summary
# ------------------------------------------------------------

# - Docstrings document functions and other blocks of code.
# - Put a function docstring as the first line inside the function.
# - Use triple quotes for docstrings.
# - Docstrings can be one line or multi-line.
# - Use # comments for normal comments.
# - Good docstrings help your future self understand your code quickly.

