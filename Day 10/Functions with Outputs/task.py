# Python Revision Notes: Functions with Outputs

# ------------------------------------------------------------
# 1. Function types so far
# ------------------------------------------------------------

# We have seen:
# - Simple functions: run the same code every time.
# - Functions with inputs: use arguments to change what the function does.
# - Functions with outputs: return a result after the function finishes.


def greet():
    # This function has no input and no output.
    print("Hello")


greet()


def greet_with_name(name):
    # This function has an input, but it only prints.
    print(f"Hello {name}")


greet_with_name("Angela")


# ------------------------------------------------------------
# 2. The return keyword
# ------------------------------------------------------------

# return sends a value back out of a function.
# The returned value replaces the function call.


def calculate():
    result = 3 * 2
    return result  # This sends result back to where the function was called.


# The function call is replaced by the returned value.
output = calculate()
print(output)


# Key points:
# - print() shows something in the console.
# - return gives a value back to the rest of your code.
# - You can save a returned value in a variable.


# ------------------------------------------------------------
# 3. Formatting names with return
# ------------------------------------------------------------

# This function takes a first name and last name.
# It returns them in title case.


def format_name(f_name, l_name):
    # .title() returns a new string with the first letter of each word capitalized.
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # Return the final formatted full name.
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("aNgElA", "YU")
print(formatted_string)


# You can also put the function call directly inside print().
print(format_name("jAcK", "BAUER"))


# Key points:
# - f_name and l_name are parameters.
# - "aNgElA" and "YU" are arguments.
# - .title() does not change the original string directly.
# - .title() returns a new formatted string.


# ------------------------------------------------------------
# 4. Built-in functions can also return outputs
# ------------------------------------------------------------

# Python's built-in len() function takes an input and returns an output.

name_length = len("Angela")
print(name_length)


# What happens:
# - "Angela" is the input.
# - len() counts the characters.
# - The result 6 is returned.
# - 6 is stored in name_length.


# ------------------------------------------------------------
# 5. print() vs return
# ------------------------------------------------------------

# print() displays a value.
# return gives a value back so it can be reused later.


def add_numbers(a, b):
    return a + b


total = add_numbers(5, 7)
print(total)


# Because add_numbers returns a value, we can use it in another calculation.
double_total = total * 2
print(double_total)


# Beginner tip:
# If a function only prints, you can see the result,
# but you cannot easily reuse it in another part of your code.


# ------------------------------------------------------------
# 6. Chaining function outputs
# ------------------------------------------------------------

# A returned output can become the input for another function.


def function_1(text):
    # Return the text twice.
    return text + text


def function_2(text):
    # Return the text in title case.
    return text.title()


first_output = function_1("hello")
print(first_output)

# The output from function_1 becomes the input for function_2.
final_output = function_2(first_output)
print(final_output)


# This can also be written in one line.
print(function_2(function_1("python")))


# Key points:
# - function_1("hello") returns "hellohello".
# - function_2("hellohello") returns "Hellohello".
# - Outputs can be passed into other functions as inputs.


# ------------------------------------------------------------
# 7. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Thinking print() and return are the same.


def only_prints():
    print("I am printed, but not returned.")


result = only_prints()
print(result)

# The output is None because only_prints() does not return anything.


# Mistake 2: Forgetting to store or use the returned value.

format_name("john", "smith")
# This runs, but the returned value is not shown or saved.

# Better:
formatted_name = format_name("john", "smith")
print(formatted_name)


# Mistake 3: Forgetting the parentheses when calling the function.

# print(format_name)
# This prints information about the function itself.

# Correct:
print(format_name("mary", "jones"))


# ------------------------------------------------------------
# 8. Mini summary
# ------------------------------------------------------------

# - return creates an output from a function.
# - The returned value replaces the function call.
# - Returned values can be saved, printed, or used in other functions.
# - print() displays a value but does not return it.
# - Built-in functions like len() and string methods like .title() also return values.
