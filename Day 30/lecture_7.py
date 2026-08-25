# ============================================================
# WORKING WITH JSON IN PYTHON - REVISION NOTES
# ============================================================

import json
from pathlib import Path


# 1. What is JSON?
# ----------------
# JSON stands for JavaScript Object Notation.
# It is a popular text format for storing and transferring structured data.
# JSON looks similar to nested Python dictionaries and lists.

# Common Python-to-JSON conversions:
#   Python dict  -> JSON object
#   Python list  -> JSON array
#   Python str   -> JSON string
#   True / False -> true / false
#   None         -> null

# Example Python data that can be converted to JSON:
student_data = {
    "Alice": {
        "age": 21,
        "subjects": ["Python", "Maths"],
        "active": True,
    }
}


# 2. Writing JSON to a file with json.dump()
# ------------------------------------------------
# json.dump(data, file) converts Python data to JSON and writes it to a file.
# Write mode creates the file if it is missing, but replaces its contents if
# it already exists.

# Store the practice file beside this Python file.
file_path = Path(__file__).with_name("json_revision_data.json")

with open(file_path, mode="w", encoding="utf-8") as data_file:
    # indent=4 makes the file easier for people to read.
    json.dump(student_data, data_file, indent=4)

print(f"JSON data was written to: {file_path.name}")


# 3. Reading JSON from a file with json.load()
# ---------------------------------------------
# json.load(file) reads JSON from an open file and converts it into Python
# objects, such as dictionaries and lists.
with open(file_path, mode="r", encoding="utf-8") as data_file:
    loaded_data = json.load(data_file)

print(loaded_data)
print(type(loaded_data))  # <class 'dict'>
print(loaded_data["Alice"]["subjects"][0])  # Python


# 4. Updating JSON data
# ---------------------
# JSON files are not updated with Python's append file mode. Appending a second
# JSON object usually creates invalid JSON. Use these three steps instead:
#   1. Read the existing JSON into Python.
#   2. Update the Python dictionary.
#   3. Write the entire updated dictionary back to the file.

new_data = {
    "Ben": {
        "age": 24,
        "subjects": ["History"],
        "active": False,
    }
}

# Step 1: read the existing data.
with open(file_path, mode="r", encoding="utf-8") as data_file:
    data = json.load(data_file)

# Step 2: update the normal Python dictionary.
data.update(new_data)

# Step 3: save the complete updated dictionary.
with open(file_path, mode="w", encoding="utf-8") as data_file:
    json.dump(data, data_file, indent=4)

print(data)  # Contains both Alice and Ben.

# Important: dict.update() replaces the value if the new dictionary contains
# a key that already exists.


# 5. dump/load compared with dumps/loads
# --------------------------------------
# Methods without "s" work with open files:
#   json.dump() -> write JSON to a file
#   json.load() -> read JSON from a file
#
# Methods ending in "s" work with JSON strings:
#   json.dumps() -> convert Python data to a JSON string
#   json.loads() -> convert a JSON string to Python data

json_string = json.dumps({"name": "Cara", "score": 95}, indent=2)
print(json_string)
print(type(json_string))  # <class 'str'>

python_data = json.loads(json_string)
print(python_data["score"])  # 95
print(type(python_data))      # <class 'dict'>


# KEY POINTS TO REMEMBER
# ----------------------
# - Import JSON with: import json
# - json.dump() writes Python data to a JSON file.
# - json.load() reads a JSON file into Python.
# - indent=4 changes formatting only; it does not change the data.
# - Loaded JSON can be used like normal Python dictionaries and lists.
# - To update a JSON file: load, update, then dump.
# - JSON is a text format, even when it contains numbers or booleans.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Use json.dump(data, file), not file.write(data). A dictionary cannot be
#    written directly as text.
#
# 2. Do not confuse dump() with dumps(): the "s" version returns a string.
#
# 3. Use double quotes in JSON written by hand. Standard JSON does not accept
#    Python-style single-quoted strings.
#
# 4. Opening a file with "w" erases its previous contents. Load the old data
#    before opening the file in write mode when performing an update.
#
# 5. json.load() can raise FileNotFoundError when the file is missing and
#    json.JSONDecodeError when the file contains empty or invalid JSON.
#
# 6. Use with open(...) so Python closes the file automatically.
