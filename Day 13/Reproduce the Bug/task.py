# Python Revision Notes: Debugging - Reproduce the Bug

from random import randint


# ------------------------------------------------------------
# 1. What does "reproduce the bug" mean?
# ------------------------------------------------------------

# To reproduce a bug means to make the bug happen again on purpose.
#
# This is important because some bugs only happen sometimes.
# If you can make the bug happen consistently, it becomes much easier to fix.


# Key points:
# - Random bugs are hard to debug.
# - Find the exact input or value that causes the error.
# - Once you can repeat the bug, you can test your fix properly.


# ------------------------------------------------------------
# 2. Example bug: dice images and list indexes
# ------------------------------------------------------------

# Imagine these are dice images.
# We use text labels here so the example is easy to read in any editor.

dice_images = ["Dice 1", "Dice 2", "Dice 3", "Dice 4", "Dice 5", "Dice 6"]


# Broken version from the lesson:

# dice_num = randint(1, 6)
# print(dice_images[dice_num])


# Why this sometimes breaks:
# - randint(1, 6) can return 1, 2, 3, 4, 5, or 6.
# - List indexes start at 0.
# - This list has indexes 0, 1, 2, 3, 4, and 5.
# - Index 6 does not exist.


# ------------------------------------------------------------
# 3. Reproducing the bug
# ------------------------------------------------------------

# To reproduce the bug, remove the randomness and test the value
# that you think causes the error.

# dice_num = 6
# print(dice_images[dice_num])

# This would cause:
# IndexError: list index out of range


# The bug happens when dice_num is 6 because there is no index 6.


# ------------------------------------------------------------
# 4. Important randint() reminder
# ------------------------------------------------------------

# randint(a, b) includes both a and b.
#
# This is different from range(start, stop),
# where the stop value is not included.

print(randint(1, 1))

# randint(1, 6) can return 6.
# That is why it can break when used directly as a list index.


# ------------------------------------------------------------
# 5. Fixed version
# ------------------------------------------------------------

# To pick a random item from this list using indexes,
# generate a random number from 0 to 5.

dice_num = randint(0, 5)
print(dice_images[dice_num])


# Key points:
# - First item in a list is index 0.
# - Last item in a 6-item list is index 5.
# - randint(0, 5) matches the valid indexes for this list.


# ------------------------------------------------------------
# 6. Checking all possible indexes
# ------------------------------------------------------------

# This loop proves that indexes 0 to 5 all work.

for index in range(0, 6):
    print(f"Index {index}: {dice_images[index]}")


# Beginner tip:
# If your code sometimes crashes with random values,
# temporarily replace the random value with a fixed value.
# Test the edge cases, especially the smallest and largest values.


# ------------------------------------------------------------
# 7. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Forgetting that lists start at index 0.

# print(dice_images[6])
# This would fail because the last valid index is 5.


# Mistake 2: Forgetting that randint() includes the final number.

possible_number = randint(1, 6)
print(possible_number)

# possible_number could be 6.


# Mistake 3: Only testing once.
#
# Random bugs may not appear every time.
# Run the code many times or force the problem value to appear.


# ------------------------------------------------------------
# 8. Mini summary
# ------------------------------------------------------------

# - Reproducing a bug means making it happen again on purpose.
# - Random bugs are easier to fix once you find the bad value.
# - randint(a, b) includes both a and b.
# - Lists start counting at 0.
# - A 6-item list has indexes 0 to 5.
# - For this dice example, use randint(0, 5), not randint(1, 6).
