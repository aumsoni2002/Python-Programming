# ============================================================
# TKINTER LAYOUTS: PACK, PLACE, GRID, AND PADDING
# ============================================================

import tkinter as tk


# Tkinter has three main geometry managers. A geometry manager decides where
# widgets appear inside their parent window or frame.


# 1. pack() - simple automatic layout
# -----------------------------------
# pack() arranges widgets next to each other. By default, widgets are placed
# from top to bottom in the order in which pack() is called.
#
# Example:
# label.pack()
# button.pack()
# entry.pack()
#
# The side option can use "top", "bottom", "left", or "right":
# label.pack(side="left")
#
# Best for: simple layouts where exact positions are not important.


# 2. place() - exact pixel positions
# ----------------------------------
# place() positions a widget using x and y coordinates.
# The top-left corner is x=0, y=0.
# Increasing x moves right; increasing y moves down.
#
# Example:
# label.place(x=100, y=50)
#
# Best for: small layouts that need exact positioning.
# Drawback: many fixed coordinates are difficult to manage and may not resize
# well on different screens.


# 3. grid() - row and column layout
# ---------------------------------
# grid() imagines the window as a table. Positions start at zero.
#   row=0, column=0 is the top-left cell.
#   A larger row number moves down.
#   A larger column number moves right.
#
# Best for: organised forms and layouts with several widgets.


# RUNNABLE GRID EXAMPLE
# ---------------------
window = tk.Tk()
window.title("Tkinter Grid Layout")
window.minsize(width=500, height=300)

# Add space between the window edges and its contents.
window.config(padx=30, pady=30)


def button_clicked():
    # Read the Entry and show its text in the Label.
    my_label.config(text=user_input.get())


# Create all widgets before starting mainloop().
my_label = tk.Label(window, text="Enter some text", font=("Arial", 18))
button = tk.Button(window, text="Update Label", command=button_clicked)
new_button = tk.Button(window, text="New Button")
user_input = tk.Entry(window, width=20)

# Place the widgets in grid cells.
my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
user_input.grid(column=3, row=2)

# Grid positions are relative to the other widgets. Empty columns and rows do
# not automatically have a visible size, so jumping straight to column 5 does
# not necessarily create a large blank gap.


# 4. Padding
# ----------
# Padding adds empty space so the interface does not look crowded.
#
# Padding on the parent window creates space around all its contents:
# window.config(padx=30, pady=30)
#
# padx and pady passed to grid() add outside space around one widget:
my_label.grid_configure(padx=10, pady=10)
button.grid_configure(padx=10, pady=10)

# padx and pady set directly on some widgets add space inside the widget:
new_button.config(padx=8, pady=4)


# Keep the window open and listen for user actions.
window.mainloop()


# KEY POINTS TO REMEMBER
# ----------------------
# - A widget is invisible until pack(), place(), or grid() manages it.
# - pack() is automatic and simple.
# - place() uses exact x and y pixel coordinates.
# - grid() uses rows and columns, starting at zero.
# - grid() positions are based on the other widgets in the same parent.
# - padx adds horizontal space; pady adds vertical space.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Do not use pack() and grid() inside the same parent window or frame.
#    Doing so raises a TclError. Choose one manager for that parent.
#
# 2. Different parent containers can use different managers. For example, the
#    window may pack a Frame while widgets inside that Frame use grid().
#
# 3. Remember the coordinate directions: column moves left/right, while row
#    moves up/down.
#
# 4. Creating a widget is not enough. Always give it a layout manager.
#
# 5. Very large place() coordinates can push a widget outside the visible area.
