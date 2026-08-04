# FOR LOOPS NOTES
#
# A loop lets us repeat code.
#
# A for loop is useful when we want to go through each item in a list
# and do something with each item one at a time.
#
# Example:
# If we have a list of fruits, a for loop can print each fruit separately.


# This is a list.
# It stores three strings:
# "Apple", "Peach", and "Pear".
fruits = ["Apple", "Peach", "Pear"]


# This is a for loop.
#
# for fruit in fruits:
#
# How to read it in English:
# "For each fruit inside the fruits list, run the indented code below."
#
# for is the keyword that starts the loop.
#
# fruit is a temporary variable name.
# It represents one item from the list at a time.
#
# in tells Python which list we want to loop through.
#
# fruits is the list we are looping through.
#
# The colon : is required.
# It tells Python that the indented block below belongs to the for loop.
for fruit in fruits:
    # This line is indented, so it is inside the for loop.
    #
    # The first time the loop runs:
    # fruit is "Apple"
    #
    # The second time the loop runs:
    # fruit is "Peach"
    #
    # The third time the loop runs:
    # fruit is "Pear"
    #
    # Because there are 3 items in the list,
    # this print() line runs 3 times.
    print(fruit)


# 1. DOING MORE THAN ONE THING INSIDE A LOOP
#
# A for loop can run more than one line of code.
# Every indented line underneath the for loop is part of the loop.

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# Output:
# Apple
# Apple pie
# Peach
# Peach pie
# Pear
# Pear pie
#
# Python finishes all indented lines for "Apple",
# then loops back and does the same thing for "Peach",
# then loops back and does the same thing for "Pear".


# 2. INDENTATION MATTERS
#
# Indentation means spaces at the beginning of a line.
#
# In Python, indentation controls whether code is inside or outside a block.
#
# Code inside the for loop is indented.
# Code outside the for loop is not indented.

for fruit in fruits:
    print(fruit)
    print("This line is inside the loop.")

print("This line is outside the loop.")

# The inside line prints once for every fruit.
# The outside line prints only once after the loop is finished.


# 3. PRINTING THE WHOLE LIST VS PRINTING EACH ITEM
#
# This prints the whole list at once.

print(fruits)

# This prints each item one by one.

for fruit in fruits:
    print(fruit)


# 4. THE LOOP VARIABLE NAME CAN CHANGE
#
# The temporary variable does not have to be called fruit.
# But it should have a clear name.
#
# These both work:
#
# for fruit in fruits:
#     print(fruit)
#
# for item in fruits:
#     print(item)
#
# fruit is better here because each item in the list is a fruit.

for item in fruits:
    print(item)


# 5. WHY LOOPS ARE USEFUL
#
# Without a loop, we would write:
#
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
#
# That works for 3 fruits, but it is not good if there are 100 fruits.
#
# A loop saves time because the same code can run for every item automatically.


# QUICK REVIEW
#
# A loop repeats code.
# A for loop can go through each item in a list.
# The loop variable stores one item at a time.
# The indented code runs once for each item.
# Code not indented under the loop runs after the loop is finished.
# The colon : starts the loop block.
