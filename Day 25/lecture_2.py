"""
READING CSV DATA WITH PYTHON AND PANDAS
=======================================

CSV means Comma-Separated Values. It is a common format for table data.
Each line is a row, and commas separate the values into columns.

Example CSV:
    day,temp,condition
    Monday,12,Sunny
    Tuesday,14,Rain

KEY POINTS
----------
- `readlines()` makes a list in which each item is one line of text.
- Python's built-in `csv` module separates every row into a list of values.
- CSV values initially arrive as strings, even when they look like numbers.
- `int(value)` converts a temperature string such as `"12"` into `12`.
- pandas reads a CSV into a labelled table called a DataFrame.
- pandas is an external package, so it must be installed before importing it.
"""

import csv
from pathlib import Path


# Build a reliable path to the CSV stored beside this Python file.
WEATHER_FILE = Path(__file__).resolve().parent / "weather_data.csv"


# 1. READING A CSV AS PLAIN TEXT
# ------------------------------
def read_as_lines(file_path):
    """Return the file as a list of unprocessed text lines."""
    with open(file_path, mode="r", encoding="utf-8") as data_file:
        return data_file.readlines()


# Result example:
# ['day,temp,condition\n', 'Monday,12,Sunny\n', ...]
# This works, but every row is still one string and needs extra processing.


# 2. USING PYTHON'S BUILT-IN CSV MODULE
# --------------------------------------
def temperatures_with_csv(file_path):
    """Read the temperature column and return its values as integers."""
    temperatures = []

    # newline="" is recommended when the csv module opens a CSV file.
    with open(file_path, mode="r", encoding="utf-8", newline="") as data_file:
        reader = csv.reader(data_file)
        next(reader)  # Skip the header row: day,temp,condition

        for row in reader:
            temperature_text = row[1]  # Index 1 is the second column.
            temperatures.append(int(temperature_text))

    return temperatures


# A csv.reader object is iterable. Each row becomes a list such as:
# ['Monday', '12', 'Sunny']


# 3. USING PANDAS
# ---------------
def show_pandas_example(file_path):
    """Read, display, and select CSV data with pandas."""
    try:
        import pandas as pd  # `pd` is the usual short name for pandas.
    except ModuleNotFoundError:
        print("pandas is not installed. Install it to run this example.")
        return

    data = pd.read_csv(file_path)  # Creates a DataFrame (a labelled table).
    print("Entire pandas DataFrame:")
    print(data)

    # Select one column by using its header name.
    temperatures = data["temp"]  # This column is a pandas Series.
    print("\nTemperature column:")
    print(temperatures)

    # Convert the Series into a regular Python list when needed.
    print("\nTemperatures as a list:", temperatures.to_list())


# BEGINNER TIPS AND COMMON MISTAKES
# ---------------------------------
# 1. Do not split CSV lines manually with `.split(",")`. The csv module can
#    correctly handle special cases such as commas inside quoted text.
# 2. `readlines()` may keep the newline character (`\n`) on each line.
# 3. `csv.reader()` returns strings. Convert numeric data before doing maths.
# 4. Remember that list index 1 means the second item, because indexing starts 0.
# 5. Skip the header before converting values, or int("temp") raises ValueError.
# 6. Column names in pandas are case-sensitive: `data["temp"]` is different
#    from `data["Temp"]`.
# 7. FileNotFoundError means Python cannot find the CSV at the given path.
# 8. Use the built-in csv module for simple tasks. pandas is especially useful
#    for larger data sets, labelled columns, calculations, and data analysis.


if __name__ == "__main__":
    print("Plain text lines:")
    print(read_as_lines(WEATHER_FILE))

    print("\nTemperatures using csv:")
    print(temperatures_with_csv(WEATHER_FILE))

    print("\nPandas example:")
    show_pandas_example(WEATHER_FILE)
