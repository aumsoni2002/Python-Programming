# Python Revision Notes: Debugging - Describe the Problem

# ------------------------------------------------------------
# 1. What is debugging?
# ------------------------------------------------------------

# Debugging means finding and fixing bugs in your code.
#
# A bug is a mistake that stops your code from working correctly.
# Bugs can be caused by typos, wrong logic, wrong assumptions, or many other things.


# Key points:
# - Everyone creates bugs.
# - Debugging is a normal part of programming.
# - The first step is to clearly describe the problem.


# ------------------------------------------------------------
# 2. Step 1: Describe the problem
# ------------------------------------------------------------

# Before fixing a bug, explain what is happening.
#
# Ask yourself:
# - What is the code supposed to do?
# - What is it actually doing?
# - Where does the result first become wrong?
# - What assumptions am I making?


# ------------------------------------------------------------
# 3. Example bug: range() stopping too early
# ------------------------------------------------------------

# Broken version from the lesson:

# def broken_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
#
# broken_function()


# Problem description:
# - The for loop is meant to loop through numbers from 1 to 20.
# - The function is meant to print "You got it" when i equals 20.
# - The hidden assumption is that range(1, 20) includes 20.
# - That assumption is wrong.


# ------------------------------------------------------------
# 4. Important range() reminder
# ------------------------------------------------------------

# range(start, stop) includes the start number,
# but it does NOT include the stop number.

print(list(range(1, 5)))

# Output:
# [1, 2, 3, 4]
#
# Notice that 5 is not included.


# Key points:
# - range(1, 20) gives numbers from 1 to 19.
# - range(1, 21) gives numbers from 1 to 20.
# - The stop value is excluded.


# ------------------------------------------------------------
# 5. Fixed version
# ------------------------------------------------------------


def my_function():
    # Use 21 so that 20 is included.
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()


# ------------------------------------------------------------
# 6. Testing your assumption
# ------------------------------------------------------------

# If you are unsure what values a loop is using, print them.


def show_range_values():
    for i in range(1, 21):
        # This helps us see each value of i.
        print(i)


show_range_values()


# Beginner tip:
# Adding temporary print statements is a simple debugging technique.
# It helps you see what your code is actually doing.


# ------------------------------------------------------------
# 7. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Forgetting that range() excludes the stop value.

print(list(range(1, 3)))
# This prints [1, 2], not [1, 2, 3].


# Mistake 2: Fixing code before understanding the problem.
#
# It is better to first describe the bug clearly.
# Otherwise, you may guess randomly and create more bugs.


# Mistake 3: Assuming a condition is reached.

for number in range(1, 5):
    if number == 10:
        print("This will never print.")

# number never becomes 10, so the print statement does not run.


# ------------------------------------------------------------
# 8. Mini summary
# ------------------------------------------------------------

# - Debugging means finding and fixing bugs.
# - First, describe the problem clearly.
# - Check what the code should do vs what it actually does.
# - Look for hidden assumptions.
# - range(start, stop) does not include the stop value.
# - Use print statements to inspect values while debugging.
