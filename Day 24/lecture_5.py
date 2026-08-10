"""
FILE PATHS: FINDING FILES AND FOLDERS
=====================================

A file path is an address that tells the computer where a file is stored.
Folders can contain other folders, so a path lists each folder in order.

KEY TERMS
---------
- Root: the top of the file system, such as `C:\\` on Windows or `/` on macOS.
- Working directory: the folder Python currently uses as its starting point.
- Absolute path: the complete address starting from the root.
- Relative path: directions starting from the current working directory.

RELATIVE-PATH SYMBOLS
---------------------
- `.` means the current folder.
- `..` means the parent folder (one level up).
- `notes.txt` and `./notes.txt` both mean a file in the current folder.
- `../notes.txt` means a file in the parent folder.
- `../../notes.txt` goes up two folder levels.

Path examples:
    project/notes.txt       -> go into `project`, then find `notes.txt`
    ../report.txt           -> go up once, then find `report.txt`
    ../../Desktop/file.txt  -> go up twice, then enter `Desktop`
"""

from pathlib import Path
from tempfile import TemporaryDirectory


# CURRENT WORKING DIRECTORY
# -------------------------
# Relative paths start here. The working directory may be different from the
# folder containing this Python file, especially when an IDE changes it.
working_directory = Path.cwd()

# __file__ is this script's path. `.parent` gives its containing folder.
script_directory = Path(__file__).resolve().parent


def read_file(file_path):
    """Read and return all the text from the given path."""
    with open(file_path, mode="r", encoding="utf-8") as file:
        return file.read()


def path_demo():
    """Create a small folder structure and demonstrate several path types."""
    with TemporaryDirectory() as temporary_folder:
        root = Path(temporary_folder)
        work_folder = root / "work"
        project_folder = work_folder / "project"
        project_folder.mkdir(parents=True)  # Create both nested folders.

        report_file = work_folder / "report.txt"
        talk_file = project_folder / "talk.txt"
        report_file.write_text("Quarterly report", encoding="utf-8")
        talk_file.write_text("Presentation notes", encoding="utf-8")

        # This is an absolute path because it starts from the file-system root.
        print("Absolute path:", talk_file.resolve())
        print("Is absolute?", talk_file.resolve().is_absolute())

        # Find `talk.txt` relative to the `work` folder.
        relative_talk = Path("project") / "talk.txt"
        print("Relative path:", relative_talk)
        print("Talk contents:", read_file(work_folder / relative_talk))

        # From the project folder, `..` moves up to `work`.
        parent_path = project_folder / ".." / "report.txt"
        print("Parent-folder contents:", read_file(parent_path))


# USING PATHLIB
# -------------
# `Path` joins path parts correctly for the current operating system.
# This is usually clearer and safer than typing slash characters yourself.
example_path = Path("project") / "data" / "scores.txt"


# BEGINNER TIPS AND COMMON MISTAKES
# ---------------------------------
# 1. A relative path depends on the current working directory. Use Path.cwd()
#    to check where Python is starting from.
# 2. Do not copy another person's absolute path: usernames and folders differ.
# 3. Windows backslashes can form escape sequences, such as `\n`. Prefer Path,
#    forward slashes, or a raw string: r"C:\Users\Name\Desktop\file.txt".
# 4. Include the filename extension, such as `.txt`, when it is part of the name.
# 5. FileNotFoundError usually means the path is wrong or the file is elsewhere.
# 6. Absolute paths are exact but less portable between computers. Relative
#    paths are usually better for files stored inside the same project.
# 7. To reliably find a file beside this script, use:
#       file_beside_script = Path(__file__).resolve().parent / "my_file.txt"


if __name__ == "__main__":
    print("Working directory:", working_directory)
    print("Script directory:", script_directory)
    print("Example joined path:", example_path)
    print()
    path_demo()
