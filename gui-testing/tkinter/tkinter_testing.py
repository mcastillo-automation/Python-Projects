from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


def miles_to_km():
    mile_input = float(miles_input.get())
    km = mile_input * 1.609
    km_result.config(text=f"{km}")


# Widgets
miles_label = Label(text="Miles")
miles_input = Entry(bg="white", width=10)
is_equal_to = Label(text="is equal to")
km_result = Label(text=0)
km_label = Label(text="Km")
calculate_button = Button(text="Calculate", command=miles_to_km)


# Grid
miles_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equal_to.grid(column=0, row=1)
km_result.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)

window.mainloop()
