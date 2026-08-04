# FOR LOOPS WITH range() NOTES
#
# So far, for loops have been used with lists.
#
# Example:
# for fruit in fruits:
#     print(fruit)
#
# But sometimes we do not need a list.
# Sometimes we just need to repeat code using numbers.
#
# That is when range() is useful.


# 1. WHAT range() DOES
#
# range() creates a sequence of numbers that a for loop can use.
#
# Important:
# range() does not print numbers by itself.
#
# This would not show the numbers 1 to 10 clearly:
# print(range(1, 10))
#
# range() is usually used with a for loop.


# 2. BASIC range(start, stop)
#
# range(1, 10) starts at 1 and stops before 10.
#
# This means it includes:
# 1, 2, 3, 4, 5, 6, 7, 8, 9
#
# It does not include 10.

for number in range(1, 10):
    print(number)


# 3. INCLUDING THE FINAL NUMBER
#
# If we want to print 1 to 10,
# we need to stop at 11.
#
# range(1, 11) includes 1 through 10.

for number in range(1, 11):
    print(number)


# 4. THE LOOP VARIABLE
#
# In this line:
#
# for number in range(1, 11):
#
# number is a temporary variable.
# Each time the loop runs, number becomes the next value in the range.
#
# First loop:
# number = 1
#
# Second loop:
# number = 2
#
# Third loop:
# number = 3
#
# This continues until number reaches 10.


# 5. range(start, stop, step)
#
# range() can also take a third value called step.
#
# The step controls how much the number increases each time.
#
# range(1, 11, 3) means:
# Start at 1.
# Stop before 11.
# Increase by 3 each time.

for number in range(1, 11, 3):
    print(number)

# Output:
# 1
# 4
# 7
# 10


# 6. THE GAUSS CHALLENGE
#
# Goal:
# Add every number from 1 to 100.
#
# 1 + 2 + 3 + 4 + ... + 100
#
# The answer should be 5050.
#
# We can do this with:
# - a variable to hold the total
# - a for loop
# - range()
# - += or normal addition


# total_sum starts at 0 because we have not added anything yet.
total_sum = 0


# range(1, 101) gives us the numbers 1 through 100.
#
# Why 101?
# Because the stop number is not included.
#
# range(1, 100) would only go up to 99.
# range(1, 101) goes up to 100.
for number in range(1, 101):
    # Each time the loop runs, number is added to total_sum.
    #
    # This line:
    # total_sum = total_sum + number
    #
    # means:
    # Take the old total_sum,
    # add the current number,
    # then store the result back into total_sum.
    total_sum = total_sum + number


# This print is outside the loop because it is not indented.
# That means it only prints once after all numbers have been added.
print(total_sum)


# 7. SAME SOLUTION USING +=
#
# += is a shorter way to add to an existing variable.
#
# total += number
#
# means the same thing as:
#
# total = total + number

total = 0

for number in range(1, 101):
    total += number

print(total)


# 8. STEP-BY-STEP MINI EXAMPLE
#
# Imagine we only add numbers from 1 to 3.

mini_total = 0

for number in range(1, 4):
    mini_total += number

print(mini_total)

# Step-by-step:
#
# Start:
# mini_total = 0
#
# First loop:
# number = 1
# mini_total = 0 + 1
# mini_total is now 1
#
# Second loop:
# number = 2
# mini_total = 1 + 2
# mini_total is now 3
#
# Third loop:
# number = 3
# mini_total = 3 + 3
# mini_total is now 6
#
# Final answer:
# 6


# QUICK REVIEW
#
# range(1, 10)
# Gives numbers from 1 to 9.
#
# range(1, 11)
# Gives numbers from 1 to 10.
#
# range(1, 11, 3)
# Gives 1, 4, 7, 10.
#
# The stop number is not included.
# The third value is the step size.
# A for loop can use range() even when there is no list.
# An accumulator variable stores a growing total.
