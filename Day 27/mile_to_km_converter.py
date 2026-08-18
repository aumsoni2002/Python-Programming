import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# ENTRY(single line text input), Location: row=0, column=1, User enters number of miles
miles_entered = tk.Entry(window, width=10)
miles_entered.grid(row=0, column=1)

# LABEL(displays text), Location: row=0, column=2, Shows the text 'Miles'
miles_label = tk.Label(window, text="Miles")
miles_label.grid(row=0, column=2)

# LABEL(displays text), Location: row=1, column=0, Shows the text 'is equal to'
is_equal_to_label = tk.Label(window, text="is equal to")
is_equal_to_label.grid(row=1, column=0)

# LABEL(displays number), Location: row=1, column=1, Shows the default before conversion number '0'
converted_number_label = tk.Label(window, text=0)
converted_number_label.grid(row=1, column=1)

# LABEL(displays text), Location: row=1, column=2, Shows the text 'Km'
km_label = tk.Label(window, text="Km")
km_label.grid(row=1, column=2)

# BUTTON(runs a function when clicked), Location: row=2, column=1, Shows the button 'Calculate'
def miles_to_km():
   km = round(float (miles_entered.get()) * 1.60934, 2)
   converted_number_label.config(text=km)


calculate_button = tk.Button(window, text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)


# Keep the window open and listen for user actions.
window.mainloop()