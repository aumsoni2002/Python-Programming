"""
FILE HANDLING: READING AND WRITING TEXT FILES
================================================

Python can open files, read their contents, and save new information.
The built-in open() function is used, so no import is needed for normal files.

KEY POINTS
----------
- Use `with open(...) as file:` so Python closes the file automatically.
- `file.read()` returns the whole file as one string.
- Mode "r" reads a file. It is the default mode.
- Mode "w" writes to a file and ERASES its old contents first.
- Mode "a" appends new text to the end without erasing existing text.
- Opening a missing file in "w" or "a" mode creates it.
- `\n` adds a new line to a string.
"""

from pathlib import Path
from tempfile import TemporaryDirectory


def read_text_file(file_path):
    """Open a text file and return all its contents as a string."""
    with open(file_path, mode="r", encoding="utf-8") as file:
        contents = file.read()  # Read everything before the file closes.

    # The file is closed automatically after the `with` block.
    return contents


def write_text_file(file_path, text):
    """Replace a file's contents, or create the file if it does not exist."""
    with open(file_path, mode="w", encoding="utf-8") as file:
        file.write(text)  # Warning: "w" erased any previous contents.


def append_text_file(file_path, text):
    """Add text to the end of a file without deleting its contents."""
    with open(file_path, mode="a", encoding="utf-8") as file:
        file.write(text)  # Include \n yourself when a new line is needed.


def revision_demo():
    """Run the examples safely inside a temporary practice folder."""
    with TemporaryDirectory() as folder:
        practice_file = Path(folder) / "my_file.txt"

        # "w" creates the file because it does not exist yet.
        write_text_file(practice_file, "Hello, my name is Aum.")
        print("After writing:")
        print(read_text_file(practice_file))

        # "a" keeps the first line and adds this text at the end.
        append_text_file(practice_file, "\nThis is a new line.")
        print("\nAfter appending:")
        print(read_text_file(practice_file))


# BEGINNER TIPS AND COMMON MISTAKES
# ---------------------------------
# 1. open("notes.txt") means the same as open("notes.txt", mode="r").
# 2. Writing to a file opened with "r" raises an UnsupportedOperation error.
# 3. Be careful with "w": it replaces everything already in the file.
# 4. Append mode does not add spaces or new lines automatically; use "\n".
# 5. A relative path such as "my_file.txt" is looked up from the program's
#    current working directory. Check the path if Python says it cannot find it.
# 6. `encoding="utf-8"` helps text behave consistently across computers.
# 7. Prefer `with open(...)` to manually calling file.close(). It also closes
#    the file if an error occurs inside the block.


if __name__ == "__main__":
    revision_demo()
