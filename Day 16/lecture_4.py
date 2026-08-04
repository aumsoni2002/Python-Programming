# Day 16 - Using Python Packages and PrettyTable

# ------------------------------------------------------------
# 1. Modules vs Packages
# ------------------------------------------------------------

# Short explanation:
# A module is usually one Python file.
# A package is a collection of modules/files grouped together to solve a
# particular problem.

# Key points to remember:
# - Every .py file you create can be used as a module.
# - A package is bigger than one module.
# - Packages often contain code written by other developers.
# - We use packages so we do not have to write everything from scratch.


# ------------------------------------------------------------
# 2. Why Use Other People's Code?
# ------------------------------------------------------------

# Short explanation:
# If someone has already solved a common problem well, we can use their package
# instead of building the same thing ourselves.

# Example problem:
# Printing a neat table in the console using only text can be annoying.

print("| Pokemon Name | Type     |")
print("|--------------|----------|")
print("| Pikachu      | Electric |")
print("| Squirtle     | Water    |")

# Key points:
# - Formatting tables manually takes time.
# - Manual formatting can break if text lengths change.
# - A package can handle the formatting for us.

# Beginner tip:
# Do not try to memorise every package. Learn how to find packages,
# read documentation, and use the examples.


# ------------------------------------------------------------
# 3. PyPI: Python Package Index
# ------------------------------------------------------------

# Short explanation:
# PyPI is the Python Package Index. It is a website where Python developers
# share packages that other people can install and use.

# Key points:
# - PyPI contains many third-party Python packages.
# - You can search PyPI for packages that solve specific problems.
# - Package pages usually include installation instructions.
# - Good packages usually have documentation and examples.

# Example:
# If you want to print pretty tables, you can search PyPI for "prettytable".


# ------------------------------------------------------------
# 4. Installing Packages
# ------------------------------------------------------------

# Short explanation:
# Some libraries, like turtle, come built into Python.
# Other packages, like prettytable, usually need to be installed first.

# In PyCharm:
# 1. Open Settings/Preferences.
# 2. Go to your project.
# 3. Open the Python Interpreter settings.
# 4. Click the plus button.
# 5. Search for the package name, for example PrettyTable.
# 6. Install it.

# Key points:
# - Built-in libraries are already available.
# - Third-party packages must be installed into your project environment.
# - Install the package before importing it in your code.

# Common mistake:
# If you see ModuleNotFoundError, the package may not be installed in the
# Python environment that is running your project.


# ------------------------------------------------------------
# 5. Importing a Package or Class
# ------------------------------------------------------------

# Short explanation:
# After installing a package, we import it so we can use its code.

# There are two common styles:

# Style 1:
# import prettytable
# table = prettytable.PrettyTable()

# Style 2:
# from prettytable import PrettyTable
# table = PrettyTable()

# Key points:
# - import package_name imports the whole package/module.
# - from package_name import Thing imports one specific class/function.
# - PrettyTable is a class, so it uses PascalCase.


# ------------------------------------------------------------
# 6. PrettyTable Example
# ------------------------------------------------------------

# Short explanation:
# PrettyTable helps us create neat ASCII tables in the console.

try:
    from prettytable import PrettyTable

    # Create a PrettyTable object from the PrettyTable class.
    table = PrettyTable()

    # Add column headings and data.
    table.field_names = ["Pokemon Name", "Type"]
    table.add_row(["Pikachu", "Electric"])
    table.add_row(["Squirtle", "Water"])
    table.add_row(["Charmander", "Fire"])

    # Print the finished table.
    print(table)

except ModuleNotFoundError:
    # This message runs only if PrettyTable is not installed.
    print("PrettyTable is not installed yet.")
    print("Install it in PyCharm before running this example.")

# Key points:
# - PrettyTable() creates a table object.
# - field_names is an attribute that stores the column headings.
# - add_row() is a method that adds a row to the table.
# - print(table) displays the table in the console.

# Beginner tip:
# An attribute stores data:
# table.field_names = ["Pokemon Name", "Type"]
#
# A method performs an action:
# table.add_row(["Pikachu", "Electric"])


# ------------------------------------------------------------
# 7. Documentation
# ------------------------------------------------------------

# Short explanation:
# Documentation tells you how to use a package.
# You do not need to understand all the source code to use a package well.

# Key points:
# - Read the package documentation for examples.
# - Look for class names, methods, attributes, and arguments.
# - You can inspect source code, but beginners usually do not need to.
# - Focus first on how to use the package correctly.

# Common beginner mistake:
# Trying to understand every line of a package's source code before using it.
# It is okay to rely on documentation and examples.


# ------------------------------------------------------------
# 8. Quick Summary
# ------------------------------------------------------------

# Module:
# - Usually one Python file.
# - Example: another_module.py

# Package:
# - A collection of code files/modules.
# - Often created by other developers.
# - Example: prettytable

# PyPI:
# - A place to find Python packages.

# PrettyTable:
# - A package/class used to create neat text tables.

# Main idea:
# Packages let us reuse existing code so we can build projects faster.

