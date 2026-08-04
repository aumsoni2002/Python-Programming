# Python Revision Notes: Debugging - Use print()

# ------------------------------------------------------------
# 1. Why use print() for debugging?
# ------------------------------------------------------------

# print() is a simple way to check what your code is doing.
#
# You can print:
# - Variable values
# - Which lines are running
# - Results before and after a calculation


# Key points:
# - print() helps you see inside your program.
# - It is useful when the code runs but gives the wrong answer.
# - Debug print statements are usually temporary.


# ------------------------------------------------------------
# 2. The original bug
# ------------------------------------------------------------

# Original interactive code from the lesson:

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# Bug:
# If pages is 45 and words per page is 250,
# the answer should be 11250.
# But the program prints 0.


# ------------------------------------------------------------
# 3. Use print() to inspect variables
# ------------------------------------------------------------

# Runnable version with fixed inputs:

word_per_page = 0
pages = 45

# This is the bug from the lesson.
# == checks whether two values are equal.
# It does NOT assign a new value.
word_per_page == 250

# Debug prints help us inspect the variables.
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")

total_words = pages * word_per_page
print(f"total_words = {total_words}")


# What print() shows:
# - pages is 45, so that variable is correct.
# - word_per_page is still 0, so the problem is near that line.


# ------------------------------------------------------------
# 4. The actual problem: = vs ==
# ------------------------------------------------------------

# = means assignment.
# It stores a value in a variable.

correct_word_per_page = 250

# == means comparison.
# It checks whether two values are equal and returns True or False.

comparison_result = correct_word_per_page == 250
print(comparison_result)


# Key points:
# - Use = when you want to save a value.
# - Use == when you want to compare two values.
# - Accidentally using == instead of = can leave a variable unchanged.


# ------------------------------------------------------------
# 5. Fixed version
# ------------------------------------------------------------

pages = 45
word_per_page = 250

total_words = pages * word_per_page
print(f"Fixed total_words = {total_words}")


# Interactive fixed version:
# This is commented out so the file can run without waiting for input.

# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# ------------------------------------------------------------
# 6. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Using == when you meant =.

score = 0
score == 10  # This compares, but does not change score.
print(score)

score = 10  # This assigns a new value.
print(score)


# Mistake 2: Not checking variable values.
#
# If the final result is wrong, print the values used to calculate it.

price = 5
quantity = 3

print(f"price = {price}")
print(f"quantity = {quantity}")
print(f"total = {price * quantity}")


# Mistake 3: Leaving too many debug prints in final code.
#
# Debug prints are helpful while fixing a bug.
# After the bug is fixed, remove prints you no longer need.


# ------------------------------------------------------------
# 7. Mini summary
# ------------------------------------------------------------

# - print() is a simple debugging tool.
# - Use print() to check variable values.
# - Debug prints help narrow down where the bug is.
# - = assigns a value.
# - == compares two values.
# - Remove temporary debug prints when they are no longer needed.
