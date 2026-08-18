# ============================================================
# TKINTER CONFIGURATION, BUTTONS, AND ENTRY - REVISION NOTES
# ============================================================

# The * imports all public Tkinter classes, including Tk, Label, Button,
# and Entry. This is convenient when using many Tkinter widgets.
from tkinter import *


# 1. Create and configure the main window
# ----------------------------------------
window = Tk()
window.title("My First GUI Click Program")
window.minsize(width=500, height=300)


# 2. Creating and changing a Label
# ---------------------------------
# Widget options can be set when the widget is created.
my_label = Label(
    window,
    text="Type something below",
    font=("Arial", 24, "bold"),
)
my_label.pack()

# There are two common ways to change one or more options later:
#
# Dictionary-style syntax:
# my_label["text"] = "New text"
#
# The config() method:
# my_label.config(text="New text", background="yellow")
#
# config() is especially useful for changing several options at once.


# 3. Creating an Entry widget
# ---------------------------
# Entry creates a single-line text input box.
user_input = Entry(window, width=20)
user_input.pack()

# user_input.get() returns the current contents as a string.
# It should be called when the text is needed, such as after a button click.


# 4. Responding to a button click
# --------------------------------
# This callback function runs each time the button is clicked.
def button_click():
    new_text = user_input.get()      # Read the current Entry text.
    my_label.config(text=new_text)   # Display that text in the Label.


# command receives the function name without parentheses.
# Tkinter will call button_click later when the user clicks the button.
button = Button(window, text="Click Me", command=button_click)
button.pack()


# 5. Keep the application running
# --------------------------------
# mainloop() displays the GUI and listens for events such as button clicks.
# It should normally be the final line of the program.
window.mainloop()


# KEY POINTS TO REMEMBER
# ----------------------
# - Label displays text; Entry accepts one line of user input.
# - A widget must use pack() or another geometry manager to appear.
# - Widgets packed earlier normally appear before widgets packed later.
# - entry.get() returns the text currently inside an Entry.
# - widget.config(option=value) changes a widget after it is created.
# - Button(command=function_name) connects a click to a function.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Do not write command=button_click(). The parentheses call the function
#    immediately while the GUI is being created. Use command=button_click.
#
# 2. Do not call user_input.get() only when creating the Entry. At that time,
#    the user has not typed anything. Call it inside the click function.
#
# 3. Do not forget pack(), or the widget will not be visible.
#
# 4. Entry.get() always returns a string. Convert it with int() or float() if
#    the program needs to perform calculations.
#
# 5. "from tkinter import *" is short, but it can hide where names come from.
#    In larger programs, "import tkinter as tk" is often clearer, followed by
#    names such as tk.Tk(), tk.Label(), and tk.Button().
