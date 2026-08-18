# ============================================================
# TKINTER WIDGET COOKBOOK - REVISION NOTES
# ============================================================

import tkinter as tk


# Create the main application window.
window = tk.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=650)


# 1. LABEL - displays text
# ------------------------
label = tk.Label(window, text="This is old text")

# config() changes a widget after it has been created.
label.config(text="Try the widgets below")
label.pack()


# 2. ENTRY - single-line text input
# ---------------------------------
entry = tk.Entry(window, width=30)

# Insert starting text at the end of the Entry.
entry.insert(tk.END, "Email address")
entry.pack()

# entry.get() returns all current Entry text as a string.


# 3. TEXT - multi-line text input
# --------------------------------
text_box = tk.Text(window, height=4, width=30)
text_box.insert(tk.END, "Write multiple lines here.")
text_box.focus()  # Place the typing cursor in this widget when the GUI opens.
text_box.pack()

# Text uses "line.character" indexes:
#   "1.0" = line 1, character 0 (the very beginning)
#   tk.END = the end of the text
# text_box.get("1.0", tk.END) reads all of its text.


# 4. BUTTON - runs a function when clicked
# -----------------------------------------
def button_clicked():
    # Read the current values only when the button is clicked.
    print(f"Entry: {entry.get()}")
    print(f"Text: {text_box.get('1.0', tk.END)}")


# Pass the function name without parentheses.
button = tk.Button(window, text="Print text", command=button_clicked)
button.pack()


# 5. SPINBOX - chooses a value using arrow buttons
# -------------------------------------------------
def spinbox_used():
    print(f"Spinbox: {spinbox.get()}")


spinbox = tk.Spinbox(
    window,
    from_=0,             # Lowest value; the underscore avoids Python's from.
    to=10,               # Highest value.
    width=5,
    command=spinbox_used,
)
spinbox.pack()


# 6. SCALE - chooses a value using a slider
# ------------------------------------------
def scale_used(value):
    # Tkinter automatically passes the current slider value to this callback.
    print(f"Scale: {value}")


scale = tk.Scale(window, from_=0, to=100, orient="horizontal", command=scale_used)
scale.pack()


# 7. CHECKBUTTON - switches one choice on or off
# ------------------------------------------------
# IntVar stores a Tkinter integer value: 0 means off and 1 means on.
checked_state = tk.IntVar()


def checkbutton_used():
    print(f"Checked: {checked_state.get()}")


checkbutton = tk.Checkbutton(
    window,
    text="Is on?",
    variable=checked_state,
    command=checkbutton_used,
)
checkbutton.pack()


# 8. RADIOBUTTONS - select one option from a group
# -------------------------------------------------
# Radio buttons belong to the same group when they share one variable.
radio_state = tk.IntVar(value=1)


def radio_used():
    print(f"Radio option: {radio_state.get()}")


# Each radio button needs a different value.
radio_button_1 = tk.Radiobutton(
    window, text="Option 1", value=1, variable=radio_state, command=radio_used
)
radio_button_2 = tk.Radiobutton(
    window, text="Option 2", value=2, variable=radio_state, command=radio_used
)
radio_button_1.pack()
radio_button_2.pack()


# 9. LISTBOX - select an item from a list
# ----------------------------------------
listbox = tk.Listbox(window, height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

# enumerate() supplies both an index and its item.
for index, fruit in enumerate(fruits):
    listbox.insert(index, fruit)


def listbox_used(event):
    selection = listbox.curselection()  # Returns selected indexes as a tuple.

    # Check first because the tuple can be empty when nothing is selected.
    if selection:
        selected_fruit = listbox.get(selection[0])
        print(f"Listbox: {selected_fruit}")


# bind() connects a Tkinter event to a callback.
# Event callbacks receive an event argument, even if it is not used.
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# Keep the window open and listen for user actions.
window.mainloop()


# KEY POINTS TO REMEMBER
# ----------------------
# - Entry is for one line; Text is for multiple lines.
# - Spinbox and Scale let the user choose a value.
# - Checkbutton represents on/off; IntVar tracks its state.
# - Radio buttons share a variable and must have different values.
# - ListboxSelect is a special event used with bind().
# - get() reads a widget's current value.
# - pack() makes each widget appear in the window.


# COMMON MISTAKES AND BEGINNER TIPS
# ---------------------------------
# 1. Use command=function_name, not command=function_name().
# 2. A Scale callback needs a value parameter; a Button callback usually does
#    not receive one.
# 3. Text.get() needs start and end indexes; Entry.get() needs no indexes.
# 4. Use from_ with an underscore because from is a Python keyword.
# 5. Give grouped radio buttons the same variable but different values.
# 6. Always check curselection() before reading a Listbox item.
