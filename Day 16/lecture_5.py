# Day 16 - PrettyTable: Objects, Methods, and Attributes

# ------------------------------------------------------------
# 1. Constructing a PrettyTable Object
# ------------------------------------------------------------

# Short explanation:
# PrettyTable is a class from the prettytable package.
# We can create a table object from this class.

try:
    from prettytable import PrettyTable

    # Create a new object from the PrettyTable class.
    table = PrettyTable()

    # At this point, the table exists, but it has no data yet.
    print("Empty table:")
    print(table)

except ModuleNotFoundError:
    print("PrettyTable is not installed yet.")
    print("Install PrettyTable in PyCharm before running this file.")

# Key points to remember:
# - PrettyTable is the class/blueprint.
# - table is the object created from that class.
# - The parentheses in PrettyTable() construct the object.
# - Printing an empty table shows a basic table with no data.

# Common mistake:
# table = PrettyTable      # Wrong: this stores the class itself.
# table = PrettyTable()    # Correct: this creates an object.


# ------------------------------------------------------------
# 2. Methods: Making the Object Do Something
# ------------------------------------------------------------

# Short explanation:
# A method is a function that belongs to an object.
# PrettyTable has methods that let us add data to the table.

try:
    from prettytable import PrettyTable

    table = PrettyTable()

    # add_column() is a method.
    # It adds one full column to the table.
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

    # The first input is the column heading.
    # The second input is a list of values for that column.
    table.add_column("Type", ["Electric", "Water", "Fire"])

    print("Table with columns:")
    print(table)

except ModuleNotFoundError:
    pass

# Key points:
# - Methods are called using dot notation.
# - Pattern: object_name.method_name(arguments)
# - add_column() takes two inputs:
#   1. the field/column name as a string
#   2. the column data as a list
# - The order of the data matters.

# Beginner tip:
# The first Pokemon matches the first type:
# Pikachu -> Electric
# Squirtle -> Water
# Charmander -> Fire


# ------------------------------------------------------------
# 3. Adding Rows Instead of Columns
# ------------------------------------------------------------

# Short explanation:
# PrettyTable can also add data one row at a time using add_row().

try:
    from prettytable import PrettyTable

    row_table = PrettyTable()

    # field_names is an attribute used to set the column headings.
    row_table.field_names = ["Pokemon Name", "Type"]

    # add_row() adds one full row at a time.
    row_table.add_row(["Pikachu", "Electric"])
    row_table.add_row(["Squirtle", "Water"])
    row_table.add_row(["Charmander", "Fire"])

    print("Table built with rows:")
    print(row_table)

except ModuleNotFoundError:
    pass

# Key points:
# - add_column() adds data column by column.
# - add_row() adds data row by row.
# - Both are methods because they do actions.

# Common mistake:
# Make sure each row has the same number of items as the table has columns.
# row_table.add_row(["Pikachu"])  # Missing the type value.


# ------------------------------------------------------------
# 4. Attributes: Changing Object Data or Settings
# ------------------------------------------------------------

# Short explanation:
# An attribute is data or a setting that belongs to an object.
# We can read or change attributes using dot notation.

try:
    from prettytable import PrettyTable

    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])

    # align is an attribute that controls text alignment.
    print("Current alignment:")
    print(table.align)

    # Change the align attribute.
    # "l" means left-align.
    table.align = "l"

    print("Left-aligned table:")
    print(table)

except ModuleNotFoundError:
    pass

# Key points:
# - Attributes are accessed with object_name.attribute_name.
# - Methods use parentheses, attributes usually do not.
# - We can change attributes using equals.
# - table.align = "l" changes the table alignment.

# Alignment values:
# - "l" = left
# - "c" = centre
# - "r" = right

# Common mistake:
# table.align("l")   # Wrong: align is an attribute, not a method.
# table.align = "l"  # Correct: change the attribute value.


# ------------------------------------------------------------
# 5. Final Clean Example
# ------------------------------------------------------------

# This is the main version to remember.

try:
    from prettytable import PrettyTable

    pokemon_table = PrettyTable()

    pokemon_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    pokemon_table.add_column("Type", ["Electric", "Water", "Fire"])

    # Set all columns to left alignment.
    pokemon_table.align = "l"

    print("Final Pokemon table:")
    print(pokemon_table)

except ModuleNotFoundError:
    pass


# ------------------------------------------------------------
# 6. Quick Summary
# ------------------------------------------------------------

# Class:
# - PrettyTable is the class.
# - It is the blueprint used to create table objects.

# Object:
# - table = PrettyTable()
# - table is an object created from the PrettyTable class.

# Method:
# - A function that belongs to an object.
# - Example: table.add_column(...)
# - Methods do actions.

# Attribute:
# - Data or a setting that belongs to an object.
# - Example: table.align
# - Attributes can often be read or changed.

# Dot notation:
# - table.add_column(...) calls a method.
# - table.align = "l" changes an attribute.

# Main idea:
# Use documentation to find which methods and attributes an object has.
