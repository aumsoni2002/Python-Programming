# INDEXERROR AND NESTED LISTS NOTES
#
# This lesson is about two important list topics:
# 1. IndexError / list index out of range
# 2. Nested lists, which means lists inside another list


# This is a list of the 50 states of America.
#
# A list stores multiple values in one variable.
# Lists use square brackets [].
# Each item is separated by a comma.
#
# This list is ordered by the date each state joined the union.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]


# Printing the whole list shows every item inside it.
print(states_of_america)


# 1. USING len() WITH A LIST
#
# len() counts how many items are inside a list.
# There are 50 states, so this prints 50.

number_of_states = len(states_of_america)
print(number_of_states)


# 2. LIST INDEXES START AT 0
#
# This is very important:
# If a list has 50 items, the indexes are not 1 to 50.
# The indexes are 0 to 49.
#
# First item:
# index 0
#
# Last item:
# index 49
#
# Why?
# Python starts counting from 0.

print(states_of_america[0])   # Output: Delaware
print(states_of_america[49])  # Output: Hawaii


# 3. INDEXERROR: LIST INDEX OUT OF RANGE
#
# An IndexError happens when you ask for an item that does not exist.
#
# This would crash:
# print(states_of_america[50])
#
# Why?
# There are 50 items in the list,
# but the last valid index is 49.
#
# Index 50 is one step beyond the end of the list.
# There is no item there.


# 4. OFF-BY-ONE ERROR
#
# An off-by-one error happens when your number is close,
# but it is one too high or one too low.
#
# This is common with lists because len() gives the total number of items,
# but indexes start at 0.
#
# number_of_states is 50.
# But states_of_america[50] is invalid.
#
# To get the last item using len(), subtract 1.

last_state_index = number_of_states - 1
print(states_of_america[last_state_index])  # Output: Hawaii

# This works because:
# number_of_states is 50
# number_of_states - 1 is 49
# states_of_america[49] is Hawaii


# 5. EASIER WAY TO GET THE LAST ITEM
#
# Python also lets us use negative indexes.
#
# -1 means the last item.
# -2 means the second last item.

print(states_of_america[-1])  # Output: Hawaii
print(states_of_america[-2])  # Output: Alaska


# 6. NESTED LISTS
#
# A nested list is a list inside another list.
#
# This is useful when you have related groups of data,
# but still want to separate them into smaller categories.
#
# Example:
# The Dirty Dozen is a list of foods with high pesticide levels.
# Some are fruits.
# Some are vegetables.
#
# We can keep fruits and vegetables separate,
# then store both lists inside one larger list.

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen is a nested list.
# It contains two lists:
# 1. fruits
# 2. vegetables

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# The printed structure has extra square brackets because there are lists inside a list.
#
# It looks like:
# [
#   [fruit list],
#   [vegetable list]
# ]


# 7. GETTING ITEMS FROM A NESTED LIST
#
# Since dirty_dozen contains two lists:
#
# dirty_dozen[0] gives the fruits list.
# dirty_dozen[1] gives the vegetables list.

print(dirty_dozen[0])  # Prints the fruits list
print(dirty_dozen[1])  # Prints the vegetables list

# To get one item inside one of the inner lists,
# use two sets of square brackets.

print(dirty_dozen[0][0])  # Output: Strawberries
print(dirty_dozen[1][0])  # Output: Spinach

# How to read dirty_dozen[0][0]:
# dirty_dozen[0] gets the first inner list, which is fruits.
# [0] after that gets the first item from the fruits list.
#
# How to read dirty_dozen[1][2]:
# dirty_dozen[1] gets the second inner list, which is vegetables.
# [2] after that gets the third item from the vegetables list.

print(dirty_dozen[1][2])  # Output: Tomatoes


# QUICK REVIEW
#
# len(list_name) gives the number of items in a list.
# A list with 50 items has indexes 0 to 49.
# The last valid index is len(list_name) - 1.
# list_name[-1] gets the last item.
# IndexError means you tried to access an index that does not exist.
# An off-by-one error often happens when using len() as an index directly.
# A nested list is a list inside another list.
# nested_list[0] gets the first inner list.
# nested_list[0][0] gets the first item inside the first inner list.
