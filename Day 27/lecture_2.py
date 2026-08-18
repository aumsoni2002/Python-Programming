# ============================================================
# TKINTER AND GRAPHICAL USER INTERFACES (GUIs) - REVISION NOTES
# ============================================================

# What is a GUI?
# --------------
# GUI stands for Graphical User Interface.
# It lets a user interact with a program through visual items such as:
#   - windows
#   - buttons
#   - text and images
#   - menus
#
# A user can point and click instead of typing every instruction.


# Command-line program vs GUI program
# -----------------------------------
# A command-line program communicates using text in a terminal or console.
print("This message appears in the console.")

# A GUI program displays a visual window that the user can interact with.
# GUIs made computers easier to use because users did not need to remember
# lots of typed commands.


# What is Tkinter?
# ----------------
# Tkinter is Python's standard module for creating desktop GUI programs.
# It provides tools for making windows and adding visual components to them.
# These components are often called "widgets".

# Key points to remember:
#   - "GUI" means Graphical User Interface.
#   - Tkinter is used to build GUIs with Python.
#   - A Tkinter program needs a main window.
#   - mainloop() keeps the window open and listens for user actions.


# A small runnable Tkinter example
# --------------------------------
import tkinter as tk

# Create the program's main window.
window = tk.Tk()

# Set the text shown in the window's title bar.
window.title("My First GUI")

# Set the starting size: 350 pixels wide and 150 pixels high.
window.geometry("350x150")

# Create some text and place it inside the window.
message = tk.Label(window, text="Hello from Tkinter!")
message.pack()

# Keep the window visible and respond to actions such as mouse clicks.
# This is usually the final line of a simple Tkinter program.
window.mainloop()


# Beginner tips and common mistakes
# ---------------------------------
# 1. Do not forget to import tkinter before using it.
# 2. Python module names are case-sensitive: use "tkinter", not "Tkinter".
# 3. Do not forget the brackets in tk.Tk() and window.mainloop().
# 4. Without mainloop(), the GUI may close immediately or not respond.
# 5. A GUI opens in a separate window, so look behind the IDE if it is hidden.


# Brief history
# -------------
# Early computers mainly used text commands. Graphical interfaces and the
# mouse made computers easier to use by allowing people to point and click.
# Xerox PARC developed important early GUI ideas, which later influenced
# systems created by Apple and Microsoft.
