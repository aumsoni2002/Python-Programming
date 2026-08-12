from pathlib import Path

import pandas as pd


# Build paths from the location of this Python file. Your old paths started with
# "./", which means "the current working folder". Those paths worked only when
# the program happened to be started from inside Day 25. These paths work even
# when the script is started from the repository root or from an IDE.
PROJECT_FOLDER = Path(__file__).resolve().parent
SQUIRREL_DATA_FILE = PROJECT_FOLDER / "2018_Central_Park_Squirrel_Data.csv"
OUTPUT_FILE = PROJECT_FOLDER / "squirrel_count.csv"


def create_squirrel_count():
    """Count squirrels by primary fur color and save the results."""
    # The main work is inside a function instead of running immediately when
    # Python reads the file. This makes the code easier to reuse and test.
    data = pd.read_csv(SQUIRREL_DATA_FILE)

    # Each condition creates True or False for every row. `data[...]` keeps the
    # matching rows, and `len()` tells us how many matching squirrels there are.
    # The dataset calls red-looking squirrels "Cinnamon", so that is the value
    # we search for even though the output uses the simpler label "red".
    gray_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_count = len(data[data["Primary Fur Color"] == "Black"])

    # pandas can build a table from a dictionary. Each dictionary key becomes a
    # column heading, and the values underneath it become that column's rows.
    squirrel_count_data = {
        "Fur Color": ["gray", "red", "black"],
        "Count": [gray_count, red_count, black_count],
    }

    squirrel_count = pd.DataFrame(squirrel_count_data)

    # pandas normally writes its row index (0, 1, 2...) into the CSV. That index
    # is not part of our squirrel data, so `index=False` leaves it out.
    squirrel_count.to_csv(OUTPUT_FILE, index=False)
    print("Saved squirrel counts to:", OUTPUT_FILE)


# When this file is started directly, `__name__` equals "__main__" and the
# function runs. If another Python file imports this one, it can use the
# function without automatically reading or writing any CSV files.
if __name__ == "__main__":
    create_squirrel_count()
