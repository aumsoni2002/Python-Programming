# Python Revision Notes: Nested Lists and Dictionaries

# ------------------------------------------------------------
# 1. What does nesting mean?
# ------------------------------------------------------------

# Nesting means putting one collection inside another collection.
#
# Examples:
# - A list inside a list
# - A list inside a dictionary
# - A dictionary inside a dictionary
#
# This is useful when simple data is not enough.


# ------------------------------------------------------------
# 2. Simple dictionary
# ------------------------------------------------------------

# This dictionary stores countries as keys and capitals as values.

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

print(capitals["France"])


# Key points:
# - Use the key to get a dictionary value.
# - capitals["France"] gives the value "Paris".


# ------------------------------------------------------------
# 3. List nested inside a dictionary
# ------------------------------------------------------------

# A dictionary key can only have one value.
# If we want to store many cities for one country, we can use a list.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Step 1: Get the list stored under the key "France".
print(travel_log["France"])

# Step 2: Get item at index 1 from that list.
# List indexes start at 0:
# Paris = 0, Lille = 1, Dijon = 2
print(travel_log["France"][1])


# Key points:
# - travel_log["France"] gives the list of French cities.
# - travel_log["France"][1] gives the second item in that list.
# - Read nested access from left to right.


# ------------------------------------------------------------
# 4. List nested inside a list
# ------------------------------------------------------------

# A list can contain another list.

nested_list = ["A", "B", ["C", "D"]]

# Step 1: Get the nested list at index 2.
print(nested_list[2])

# Step 2: Get item at index 1 from the nested list.
print(nested_list[2][1])


# Key points:
# - nested_list[2] gives ["C", "D"].
# - nested_list[2][1] gives "D".
# - Each pair of square brackets goes one level deeper.


# ------------------------------------------------------------
# 5. Dictionary nested inside a dictionary
# ------------------------------------------------------------

# A dictionary can also store another dictionary as a value.
# This lets us store more detailed information.

detailed_travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
}

# Step 1: Get the dictionary stored under "Germany".
print(detailed_travel_log["Germany"])

# Step 2: Get the list stored under "cities_visited".
print(detailed_travel_log["Germany"]["cities_visited"])

# Step 3: Get item at index 2 from that list.
print(detailed_travel_log["Germany"]["cities_visited"][2])


# Key points:
# - Use dictionary keys to move through dictionaries.
# - Use list indexes to move through lists.
# - Combine them in order to reach nested data.


# ------------------------------------------------------------
# 6. Common mistakes
# ------------------------------------------------------------

# Mistake 1: Using the wrong key.

# print(detailed_travel_log["germany"])
# This would cause a KeyError because the key is "Germany", not "germany".


# Mistake 2: Using the wrong index.

# print(travel_log["France"][5])
# This would cause an IndexError because the France list only has indexes 0, 1, and 2.


# Mistake 3: Confusing dictionaries and lists.

# Dictionaries use keys:
print(detailed_travel_log["France"])

# Lists use indexes:
print(travel_log["France"][0])


# Beginner tip:
# When nested data feels confusing, break it into smaller steps.

germany_data = detailed_travel_log["Germany"]
cities = germany_data["cities_visited"]
stuttgart = cities[2]

print(stuttgart)


# ------------------------------------------------------------
# 7. Mini summary
# ------------------------------------------------------------

# - Nesting means storing one collection inside another.
# - Lists can be inside dictionaries.
# - Dictionaries can be inside dictionaries.
# - Lists can be inside lists.
# - Use keys for dictionaries.
# - Use indexes for lists.
# - Work from left to right and go one level deeper each time.
