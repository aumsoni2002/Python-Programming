# ============================================================
# TKINTER WINDOWS, LABELS, AND PACK() - REVISION NOTES
# ============================================================

import tkinter


# 1. Importing Tkinter
# --------------------
# Tkinter is Python's standard library for creating desktop GUIs.
# It is normally included when Python is installed, so it usually does not
# need to be installed separately.

# Key point:
# Use "tkinter" with a lowercase t because Python names are case-sensitive.


# 2. Creating the main window
# ---------------------------
# Tk is a class inside the tkinter module.
# Calling tkinter.Tk() creates the main window object for the program.
window = tkinter.Tk()

# Change the text displayed in the window's title bar.
window.title("My First GUI Program")

# Set the smallest size to which the window can be resized.
# The values are measured in pixels: 500 wide and 300 high.
window.minsize(width=500, height=300)

# Key points:
#   - A Tkinter program normally has one main Tk window.
#   - Methods such as title() and minsize() change the window.
#   - GUI components are added after Tk() and before mainloop().


# 3. Creating a Label widget
# --------------------------
# A widget is a GUI component, such as a label, button, or text box.
# A Label displays text or an image that the user normally does not edit.
my_label = tkinter.Label(
    window,                         # Put this label inside the main window.
    text="I am a Label",           # Text shown by the label.
    font=("Arial", 24, "bold"),   # Font name, size, and style.
)

# The font setting is a tuple:
#   ("Arial", 24, "bold")
#   font name   size  style
# The style can also be "italic", or it can be left out for regular text.


# 4. Displaying a widget with pack()
# ----------------------------------
# Creating a widget is not enough - it must also be placed in the window.
# pack() is a simple geometry manager that automatically arranges widgets.
my_label.pack()

# Useful pack() options:
#
# my_label.pack(side="left")
# Places the label against the left side. Other choices are "right", "top",
# and "bottom". Use only one pack() call for this label.
#
# my_label.pack(expand=True)
# Gives the label's area extra available space. This can make the label appear
# centred when it is the only widget.
#
# Note: plain pack() normally places the first widget at the top centre.


# 5. Keeping the GUI running
# ---------------------------
# mainloop() keeps the window open and listens for user actions, such as
# clicking, typing, resizing the window, or closing it.
# It works like a loop that continues until the user closes the program.
# It should normally be the final line of a Tkinter program.
window.mainloop()


# ORDER TO REMEMBER
# -----------------
# 1. Import tkinter.
# 2. Create the main window with tkinter.Tk().
# 3. Configure the window.
# 4. Create widgets.
# 5. Lay out each widget with pack() or another geometry manager.
# 6. Call mainloop() last.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# - Forgetting mainloop(): the window may close immediately.
# - Forgetting pack(): the label is created but will not be visible.
# - Writing tkinter.Tk without (): this refers to the class but does not create
#   a window object.
# - Putting code after mainloop(): that code usually waits until the GUI closes.
# - Calling pack() several times on one widget: choose the required options and
#   call it once instead.
# - pack() accepts many named options. Its definition may show **kw, which means
#   it can receive multiple keyword arguments, such as side="left".
