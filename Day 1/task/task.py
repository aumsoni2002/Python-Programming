# Variable naming rules and best practices in Python:
#
# MUST DO:
# A variable name must start with a letter or an underscore.
# Good examples:
# name
# _name
#
# A variable name can contain letters, numbers, and underscores.
# Good examples:
# name1
# user_name
# total_score
#
# Variable names are case-sensitive.
# This means name, Name, and NAME are three different variables.
#
# SHOULD DO:
# Use clear names that explain what the variable stores.
# For example, name is better than n if the variable stores a person's name.
# length is better than l if the variable stores the length of something.
#
# Use snake_case for variable names in Python.
# snake_case means using lowercase words separated by underscores.
# Good examples:
# user_name
# first_name
# total_score
# character_count
#
# Keep variable names readable.
# A slightly longer clear name is usually better than a short confusing name.
#
# SHOULD NOT DO:
# Do not start a variable name with a number.
# This is not allowed:
# 1name = "Angela"
#
# Do not use spaces in variable names.
# This is not allowed:
# user name = "Angela"
#
# Use underscores instead:
# user_name = "Angela"
#
# Do not use Python keywords as variable names.
# Keywords are words Python already uses for special meanings.
# Examples include print, input, if, else, for, while, and class.
#
# Avoid names that are too vague.
# For example, x, y, and z are usually not helpful unless you are doing math.
#
# In this code:
# name stores the text "Angela".
# length stores the number of characters inside name.
name = "Angela"
print(name[0])
length = len(name)
print(length) 
