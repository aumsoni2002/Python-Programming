# PYTHON LISTS NOTES
#
# A list is a data structure.
# A data structure is a way to organize and store data.
#
# A normal variable stores one value:
# name = "Aum"
# age = 12
#
# A list can store many values together in one variable.
# Lists are useful when the values are related.
#
# Examples:
# - names of students
# - items in a shopping cart
# - people waiting in a queue
# - states in a country
# - scores in a game


# 1. CREATING A LIST
#
# Lists use square brackets: []
# Each item in the list is separated by a comma.

fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

# In this list:
# "Cherry" is the first item.
# "Apple" is the second item.
# "Pear" is the third item.
#
# Lists can store strings, numbers, Booleans, or even mixed data types.

mixed_list = ["Aum", 12, 3.14, True]
print(mixed_list)


# 2. WHY LISTS ARE USEFUL
#
# Without a list, related data would need many separate variables:
#
# state1 = "Delaware"
# state2 = "Pennsylvania"
# state3 = "New Jersey"
#
# That works, but it becomes messy with lots of items.
#
# A list lets us keep related values together.

states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]


# 3. LISTS KEEP ORDER
#
# Lists remember the order of their items.
# In states_of_america, the states are listed in the order they joined the union.
#
# This matters when order is important.
#
# Example:
# In a queue, the first person should stay first.
# In a list of states, the first state should stay first.


# 4. GETTING AN ITEM FROM A LIST
#
# To get one item from a list, use square brackets after the list name.
# Inside the square brackets, write the index number.
#
# The index is the item's position in the list.
#
# Important:
# Python starts counting from 0, not 1.
#
# Indexes for fruits:
# fruits[0] is "Cherry"
# fruits[1] is "Apple"
# fruits[2] is "Pear"

print(fruits[0])  # Output: Cherry
print(fruits[1])  # Output: Apple
print(fruits[2])  # Output: Pear


# 5. WHY THE FIRST ITEM IS INDEX 0
#
# At first, index 0 feels strange because humans usually count from 1.
#
# A helpful way to think about it:
# The index is like an offset from the start of the list.
#
# The first item has moved 0 steps from the start.
# The second item has moved 1 step from the start.
# The third item has moved 2 steps from the start.

print(states_of_america[0])  # Output: Delaware
print(states_of_america[1])  # Output: Pennsylvania
print(states_of_america[2])  # Output: New Jersey


# 6. NEGATIVE INDEXES
#
# Negative indexes count from the end of the list.
#
# -1 means the last item.
# -2 means the second last item.
# -3 means the third last item.

print(states_of_america[-1])  # Output: Hawaii
print(states_of_america[-2])  # Output: Alaska
print(states_of_america[-3])  # Output: Arizona


# 7. CHANGING AN ITEM IN A LIST
#
# Lists are changeable.
# The programming word for changeable is mutable.
#
# To change an item:
# 1. Choose the item using its index.
# 2. Assign a new value with =.

print(states_of_america[1])  # Pennsylvania before the change

states_of_america[1] = "Pencilvania"

print(states_of_america[1])  # Pencilvania after the change

# This changed the item at index 1.
# It did not create a new list.
# It changed the existing list.


# 8. ADDING ONE ITEM WITH append()
#
# append() adds one item to the end of a list.
#
# Dot notation is used here:
# states_of_america.append(...)
#
# This means:
# Use the append() method that belongs to this list.

states_of_america.append("Angelaland")
print(states_of_america[-1])  # Output: Angelaland

# append() is useful when you want to add one new item.
# Example:
# Add one new person to the end of a queue.


# 9. ADDING MULTIPLE ITEMS WITH extend()
#
# extend() adds several items to the end of a list.
#
# The value passed into extend() should also be a list.

states_of_america.extend(["Aumland", "Pythonland"])

print(states_of_america[-2])  # Output: Aumland
print(states_of_america[-1])  # Output: Pythonland

# append() adds one item.
# extend() adds multiple items from another list.


# 10. SQUARE BRACKETS REVIEW
#
# Square brackets are used in two common list situations:
#
# Creating a list:
# fruits = ["Cherry", "Apple", "Pear"]
#
# Getting an item from a list:
# fruits[0]
#
# So when you see square brackets in Python,
# think: this might be related to a list or getting an item by index.


# 11. YOU DO NOT NEED TO MEMORIZE EVERY LIST METHOD
#
# Python lists have many useful methods.
# Examples include:
# append()
# extend()
# remove()
# pop()
# sort()
#
# You do not need to memorize all of them right now.
# The important thing is to understand what lists are
# and know that list methods exist.
#
# Programming is like an open-book exam.
# It is normal to check documentation or search when you need a method.


# QUICK REVIEW
#
# A list stores multiple values in one variable.
# Lists use square brackets [].
# Items are separated by commas.
# Lists keep their order.
# Python list indexes start at 0.
# list[0] gives the first item.
# list[-1] gives the last item.
# list[index] = new_value changes an item.
# append() adds one item to the end.
# extend() adds multiple items to the end.
