# Python Revision Notes: Debugging - Use a Debugger

import random
import maths


# ------------------------------------------------------------
# 1. What is a debugger?
# ------------------------------------------------------------

# A debugger is a tool that lets you pause your code while it runs.
#
# It helps you:
# - Stop at a specific line
# - Run code one line at a time
# - See the current value of variables
# - Follow code into functions
# - Understand exactly where the bug happens


# Key points:
# - print() is useful, but a debugger is more powerful.
# - A debugger lets you inspect your program while it is running.
# - PyCharm, Thonny, and many other editors include debuggers.


# ------------------------------------------------------------
# 2. Breakpoints
# ------------------------------------------------------------

# A breakpoint is a line where the debugger pauses your program.
#
# In PyCharm:
# - Click in the gutter beside a line number to add a breakpoint.
# - Run the file in Debug mode.
# - Python pauses when it reaches that line.


# Beginner tip:
# Put breakpoints near the area where you think the bug starts.


# ------------------------------------------------------------
# 3. Step Over, Step Into, and Step Out
# ------------------------------------------------------------

# Common debugger buttons:
#
# Step Over:
# - Run the current line and move to the next line.
# - Useful when you do not need to inspect another function.
#
# Step Into:
# - Go inside the function being called.
# - Useful when you want to inspect how that function works.
#
# Step Into My Code:
# - Like Step Into, but skips Python library code.
# - Useful when your project has multiple files.
#
# Step Out:
# - Leave the current function and go back to where it was called.


# ------------------------------------------------------------
# 4. The original bug
# ------------------------------------------------------------

# Original broken version from the lesson:

# def broken_mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)


# Bug:
# b_list.append(new_item) is outside the for loop.
# That means it only runs once, after the loop is finished.
# So only one item gets added to b_list.


# ------------------------------------------------------------
# 5. Fixed version
# ------------------------------------------------------------


def mutate(a_list):
    b_list = []

    for item in a_list:
        # Multiply the current item by 2.
        new_item = item * 2

        # Add a random number from 1 to 3.
        new_item += random.randint(1, 3)

        # Use our own maths.add() function to add item again.
        new_item = maths.add(new_item, item)

        # This line must be inside the loop.
        # It adds each new_item to b_list as it is created.
        b_list.append(new_item)

    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# Key points:
# - Indentation changes how Python code runs.
# - If append() is outside the loop, it only happens once.
# - If append() is inside the loop, it happens every time the loop runs.


# ------------------------------------------------------------
# 6. How the debugger helps here
# ------------------------------------------------------------

# While stepping through the broken code, you would watch b_list.
#
# In the broken version:
# - b_list stays empty during the loop.
# - Only the final new_item gets appended after the loop.
#
# In the fixed version:
# - b_list grows after each loop.
# - One new value is added for each item in a_list.


# ------------------------------------------------------------
# 7. Small predictable example
# ------------------------------------------------------------

# Random numbers make debugging harder because the result changes each run.
# Here is a predictable version without random numbers.


def predictable_mutate(a_list):
    b_list = []

    for item in a_list:
        new_item = item * 2
        new_item += 1
        new_item = maths.add(new_item, item)
        b_list.append(new_item)

    return b_list


print(predictable_mutate([1, 2, 3]))


# What happens for item 1:
# - 1 * 2 = 2
# - 2 + 1 = 3
# - 3 + 1 = 4
#
# So the first result is 4.


# ------------------------------------------------------------
# 8. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Wrong indentation.
#
# In Python, indentation decides whether code is inside or outside a loop.


# Mistake 2: Stepping into library code when you do not need to.
#
# random.randint() is built-in library code.
# Most of the time, the bug is in your code, not Python's library code.


# Mistake 3: Forgetting to watch variable values.
#
# In a debugger, watch important variables like:
# - item
# - new_item
# - b_list


# ------------------------------------------------------------
# 9. Mini summary
# ------------------------------------------------------------

# - A debugger lets you pause and inspect running code.
# - A breakpoint tells the debugger where to stop.
# - Step Over runs the current line.
# - Step Into goes inside a function.
# - Step Out leaves the current function.
# - The variables panel shows values as they change.
# - Debuggers are especially helpful for loops and indentation bugs.
