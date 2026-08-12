"""
PANDAS: DATAFRAMES, SERIES, FILTERING, AND CSV FILES
===================================================

pandas is a library for working with table-shaped data.

KEY IDEAS
---------
- DataFrame: a complete table with rows and columns.
- Series: one column from a DataFrame, similar to a Python list.
- The first CSV row normally becomes the DataFrame's column names.
- A Series has useful methods such as `.mean()`, `.max()`, and `.to_list()`.
- A Boolean condition can filter a DataFrame and return matching rows.
- pandas can create DataFrames from dictionaries and export them as CSV files.

pandas is not built into Python. Install it in the active environment first:
    pip install pandas
"""

from pathlib import Path

try:
    import pandas as pd  # `pd` is the conventional short name for pandas.
except ModuleNotFoundError:
    pd = None


PROJECT_FOLDER = Path(__file__).resolve().parent
WEATHER_FILE = PROJECT_FOLDER / "weather_data.csv"
OUTPUT_FILE = PROJECT_FOLDER / "new_data.csv"


def weather_data_demo():
    """Read and analyse the weather CSV with pandas."""
    # read_csv() turns the CSV table into a DataFrame.
    data = pd.read_csv(WEATHER_FILE)

    # 1. DATAFRAME AND SERIES
    # -----------------------
    print("Data type of the whole table:", type(data))

    temperatures = data["temp"]  # One column is a Series.
    print("Data type of one column:", type(temperatures))

    # Convert pandas objects into regular Python objects when useful.
    data_dictionary = data.to_dict()
    temperature_list = temperatures.to_list()
    print("\nDictionary:", data_dictionary)
    print("Temperature list:", temperature_list)

    # 2. CALCULATIONS ON A SERIES
    # ---------------------------
    python_average = sum(temperature_list) / len(temperature_list)
    pandas_average = temperatures.mean()  # pandas does the same calculation.
    highest_temperature = temperatures.max()

    print("\nAverage using Python:", python_average)
    print("Average using pandas:", pandas_average)
    print("Highest temperature:", highest_temperature)

    # Other useful Series methods include .min(), .median(), .mode(), and .sum().

    # 3. SELECTING COLUMNS
    # --------------------
    print("\nCondition column:")
    print(data["condition"])  # Recommended: works with almost any column name.

    # Attribute notation also works for simple column names:
    print("Same column using attribute notation:")
    print(data.condition)

    # 4. FILTERING ROWS
    # -----------------
    # This creates True/False values, one for each row.
    monday_filter = data["day"] == "Monday"

    # Passing that condition into data[...] keeps only matching rows.
    monday_row = data[monday_filter]
    hottest_row = data[data["temp"] == data["temp"].max()]

    print("\nMonday's row:")
    print(monday_row)
    print("\nRow with the highest temperature:")
    print(hottest_row)

    # 5. GETTING ONE VALUE AND CONVERTING TEMPERATURE
    # ------------------------------------------------
    # monday_row["temp"] is still a Series. `.iloc[0]` gets its first value.
    monday_celsius = monday_row["temp"].iloc[0]
    monday_fahrenheit = monday_celsius * 9 / 5 + 32
    print(f"\nMonday: {monday_celsius}°C = {monday_fahrenheit}°F")


def create_dataframe_demo():
    """Create a DataFrame from a dictionary and save it as a CSV file."""
    student_data = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65],
    }

    # Each dictionary key becomes a column heading.
    students = pd.DataFrame(student_data)
    print("\nStudent DataFrame:")
    print(students)

    # index=False prevents pandas from saving its row numbers as another column.
    students.to_csv(OUTPUT_FILE, index=False)
    print("Saved CSV to:", OUTPUT_FILE)


# BEGINNER TIPS AND COMMON MISTAKES
# ---------------------------------
# 1. Use parentheses when calling methods: temperatures.mean(), not .mean.
# 2. Column names are case-sensitive: "temp" and "Temp" are different.
# 3. Prefer data["column"] to data.column. Attribute notation fails when a
#    heading contains spaces, is not a valid identifier, or matches a method.
# 4. Use `==` to compare values. A single `=` assigns a value instead.
# 5. Put filtering conditions inside parentheses when combining them:
#       data[(data["temp"] > 15) & (data["condition"] == "Sunny")]
#    Use `&` and `|` for pandas conditions, not Python's `and` and `or`.
# 6. A filtered result can contain zero, one, or many rows. Check that it is not
#    empty before using `.iloc[0]` when the data might not contain a match.
# 7. DataFrame columns must have equal-length lists when created from a dict.
# 8. Use `index=False` if you do not want row numbers written to the CSV.


if __name__ == "__main__":
    if pd is None:
        print("pandas is not installed. Install it with: pip install pandas")
    elif not WEATHER_FILE.exists():
        print("Could not find:", WEATHER_FILE)
    else:
        weather_data_demo()
        create_dataframe_demo()
