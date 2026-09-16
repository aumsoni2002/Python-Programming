"""
REVISION NOTES: PYTHON'S DATETIME MODULE
========================================

1. What is datetime?
--------------------
The built-in ``datetime`` module helps Python work with dates and times. It is
part of Python, so it does not need to be installed.

Key points:
- ``import datetime as dt`` gives the module the shorter name ``dt``.
- The module and one of its classes are both named ``datetime``.
- Therefore, ``dt.datetime`` means the ``datetime`` class inside the module.

2. Getting the current date and time
------------------------------------
``dt.datetime.now()`` creates a datetime object containing the computer's
current local date and time.

A datetime object is not a string. Its individual values can be accessed using
attributes such as ``year``, ``month``, ``day``, ``hour``, and ``minute``.

3. Finding the weekday
----------------------
``weekday()`` returns an integer for the day of the week:

    Monday = 0, Tuesday = 1, ... Sunday = 6

Beginner tip: Python often starts counting from 0, not 1.

4. Creating a specific datetime
-------------------------------
Call ``dt.datetime()`` with at least a year, month, and day. Time values are
optional and default to zero, which means midnight (00:00:00).

Common mistakes:
- Supply numbers as integers: use ``month=12``, not ``month="12"``.
- The valid month range is 1-12; it does not start at 0.
- Invalid dates, such as 31 February, raise ``ValueError``.
- ``now()`` uses the computer's local time. Time zones need extra handling in
  applications used across different regions.
"""

import datetime as dt


def show_current_datetime() -> None:
    """Display the current date and time and some of its individual parts."""
    now = dt.datetime.now()  # Get the computer's current local date and time.

    print("Full datetime:", now)
    print("Year:", now.year)  # The year is an integer, such as 2026.
    print("Month:", now.month)  # January is 1 and December is 12.
    print("Day:", now.day)
    print("Hour:", now.hour)  # Uses the 24-hour clock: 0 to 23.
    print("Minute:", now.minute)
    print("Second:", now.second)
    print("Microsecond:", now.microsecond)

    # Because now.year is an integer, it can be used in a condition.
    if now.year >= 2020:
        print("This date is in 2020 or later.")


def show_weekday() -> None:
    """Display both the weekday number and a beginner-friendly weekday name."""
    now = dt.datetime.now()
    weekday_number = now.weekday()  # Monday is 0; Sunday is 6.
    weekday_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    print("Weekday number:", weekday_number)
    print("Weekday name:", weekday_names[weekday_number])


def show_custom_datetimes() -> None:
    """Create and display datetime objects for dates that we choose."""
    # Only year, month, and day are required. The time defaults to midnight.
    birthday_date = dt.datetime(year=1995, month=12, day=15)

    # Set hour=4 when the exact time should be 4:00 AM.
    birthday_with_time = dt.datetime(year=1995, month=12, day=15, hour=4)

    print("Birthday at default time:", birthday_date)
    print("Birthday with a time:", birthday_with_time)


if __name__ == "__main__":
    # These examples run only when this file is started directly.
    show_current_datetime()
    show_weekday()
    show_custom_datetimes()
