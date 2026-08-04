# Python Revision Notes: Dictionaries

# ------------------------------------------------------------
# 1. What is a dictionary?
# ------------------------------------------------------------

# A dictionary stores related information as key/value pairs.
#
# Think of a real dictionary:
# - The word is the key.
# - The definition is the value.
#
# Python dictionary syntax:
# {
#     key: value,
# }

# Key points:
# - Dictionaries use curly braces: {}
# - Each item has a key and a value.
# - The key comes first, then a colon, then the value.
# - Separate each key/value pair with a comma.


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)


# ------------------------------------------------------------
# 2. Getting a value from a dictionary
# ------------------------------------------------------------

# To get a value, use the dictionary name and the key in square brackets.

bug_definition = programming_dictionary["Bug"]
print(bug_definition)


# Key points:
# - Dictionaries are not accessed by index like lists.
# - Use the key to get the value.
# - The key must match exactly.


# ------------------------------------------------------------
# 3. Common KeyError mistake
# ------------------------------------------------------------

# If you use a key that does not exist, Python gives a KeyError.

# print(programming_dictionary["Bog"])
# This would cause a KeyError because "Bog" is not a key.


# Beginner tip:
# Spelling and capital letters matter.
# "Bug" and "bug" are different keys.


# ------------------------------------------------------------
# 4. Keys can have different data types
# ------------------------------------------------------------

# Most beginner examples use strings as keys, but keys can also be numbers.

number_dictionary = {
    1: "One",
    2: "Two",
    3: "Three",
}

# Because the key is the number 1, we use 1, not "1".
print(number_dictionary[1])


# Common mistake:
# If your key is a string, use quotes.

# programming_dictionary[Bug]
# This would not work because Python thinks Bug is a variable.

# Correct:
print(programming_dictionary["Bug"])


# ------------------------------------------------------------
# 5. Adding a new item
# ------------------------------------------------------------

# You can add a new key/value pair after the dictionary has been created.

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)


# Key points:
# - Use dictionary_name[new_key] = new_value.
# - If the key does not exist, Python adds a new item.


# ------------------------------------------------------------
# 6. Creating an empty dictionary
# ------------------------------------------------------------

# An empty dictionary is useful when you want to add data later.

student_scores = {}

student_scores["Aum"] = 85
student_scores["Priya"] = 92

print(student_scores)


# Key points:
# - Empty dictionary: {}
# - Empty list: []
# - Do not confuse the two.


# ------------------------------------------------------------
# 7. Editing an item
# ------------------------------------------------------------

# If the key already exists, assigning a new value edits the item.

programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary["Bug"])


# Key points:
# - Existing key = value gets updated.
# - New key = new item gets added.


# ------------------------------------------------------------
# 8. Wiping a dictionary
# ------------------------------------------------------------

# You can wipe a dictionary by setting it equal to an empty dictionary.

game_scores = {
    "Player 1": 10,
    "Player 2": 20,
}

print(game_scores)

# This clears all the scores.
game_scores = {}

print(game_scores)


# Beginner tip:
# Wiping a dictionary removes all its data.
# Only do this when you really want to reset it.


# ------------------------------------------------------------
# 9. Looping through a dictionary
# ------------------------------------------------------------

# When you loop through a dictionary directly, Python gives you the keys.

for key in programming_dictionary:
    print(key)


# To get each value, use the key to look it up.

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Key points:
# - for key in dictionary gives each key.
# - dictionary[key] gives the value for that key.


# ------------------------------------------------------------
# 10. Mini summary
# ------------------------------------------------------------

# - A dictionary stores key/value pairs.
# - Use curly braces to create a dictionary.
# - Use square brackets and a key to get a value.
# - A wrong key causes a KeyError.
# - Use dictionary[key] = value to add or edit items.
# - Use {} to create or wipe a dictionary.
# - Looping through a dictionary gives you the keys first.
