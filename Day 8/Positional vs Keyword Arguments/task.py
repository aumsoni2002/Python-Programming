# Python Revision Notes: Positional vs Keyword Arguments

# ------------------------------------------------------------
# 1. Functions with more than one input
# ------------------------------------------------------------

# A function can take more than one input.
# Each input is stored in a parameter.

# Key points:
# - Put parameters inside the parentheses.
# - Separate multiple parameters with commas.
# - Use the parameters inside the function body.


def greet_with(name, location):
    # name and location are parameters.
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Here we give the function two arguments.
greet_with("Jack Bauer", "Nowhere")


# ------------------------------------------------------------
# 2. Positional arguments
# ------------------------------------------------------------

# Positional arguments are matched by their order.
#
# The first argument goes into the first parameter.
# The second argument goes into the second parameter.


def show_numbers(a, b, c):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")


# 1 goes into a, 2 goes into b, and 3 goes into c.
show_numbers(1, 2, 3)


# If we change the order, the values go into different parameters.
show_numbers(3, 1, 2)


# Example with greet_with:
greet_with("Angela", "London")

# This is the wrong order.
# Python does not know that "Nowhere" is a place and "Jack Bauer" is a name.
# It only looks at the position.
greet_with("Nowhere", "Jack Bauer")


# Beginner tip:
# If your function output looks strange, check the order of your arguments.


# ------------------------------------------------------------
# 3. Keyword arguments
# ------------------------------------------------------------

# Keyword arguments say exactly which parameter should get which value.
#
# Format:
# function_name(parameter_name=value)

# Here the order is clear because we name each parameter.
greet_with(name="Angela", location="London")

# With keyword arguments, the order can be changed.
# The result is still correct because the parameter names are included.
greet_with(location="London", name="Angela")


# Key points:
# - Keyword arguments make code clearer.
# - They help avoid mistakes caused by the wrong order.
# - They can make the function call longer to write.


# ------------------------------------------------------------
# 4. Positional vs keyword arguments
# ------------------------------------------------------------

# Positional arguments:
# - Shorter to write.
# - Matched by order.
# - Can cause mistakes if the order is wrong.

# Keyword arguments:
# - Longer to write.
# - Matched by parameter name.
# - Usually clearer when a function has several inputs.


def make_profile(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")


# Positional arguments: order matters.
make_profile("Aum", 25, "Toronto")

# Keyword arguments: order does not matter.
make_profile(city="Toronto", name="Aum", age=25)


# ------------------------------------------------------------
# 5. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Giving too few arguments.

# greet_with("Angela")
# This would cause an error because location is missing.


# Mistake 2: Giving too many arguments.

# greet_with("Angela", "London", "Extra")
# This would cause an error because greet_with only expects 2 inputs.


# Mistake 3: Misspelling a keyword argument.

# greet_with(namme="Angela", location="London")
# This would cause an error because the parameter is called name, not namme.


# Mistake 4: Putting positional arguments after keyword arguments.

# greet_with(name="Angela", "London")
# This would cause an error.

# Correct version:
greet_with(name="Angela", location="London")


# ------------------------------------------------------------
# 6. Mini summary
# ------------------------------------------------------------

# - Functions can have multiple parameters.
# - Positional arguments are matched by order.
# - Keyword arguments are matched by name.
# - Use keyword arguments when you want the code to be extra clear.
# - Check argument order if your function gives unexpected results.
