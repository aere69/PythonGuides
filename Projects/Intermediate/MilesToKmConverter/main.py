from tkinter import *

# Create the program windod
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=100, height=100)
window.config(padx=10,pady=10)

# Miles Entry
miles = Entry(width=10)
miles.grid(row=1,column=2)

# Miles Label
miles_label = Label(text="miles")
miles_label.grid(row=1, column=3)

# is equal Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=2, column=1)

# result Label
result = Label(text="")
result.grid(row=2,column=2)

# KM Label
km_label = Label(text="km")
km_label.grid(row=2,column=3)

# Calculate Button
def action():
    res = float(miles.get())*1.609
    result.config(text=f"{res}")

button = Button(text="Calculate", command=action)
button.grid(row=3, column=2)

window.mainloop()
