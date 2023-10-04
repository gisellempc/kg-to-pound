from tkinter import *


def kg_to_pounds():
    kg = float(kg_input.get())
    pounds = kg * 2.205
    pounds_result.config(text=f"{pounds}")


window = Tk()
window.title("Kilograms to Pounds Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Kg entry
kg_input = Entry(width=6)
kg_input.grid(column=1, row=0)

# kg text
kg_txt = Label(text=" Kg")
kg_txt.grid(column=2, row=0)

# is equal
sentence = Label(text="is equal to: ")
sentence.grid(column=0, row=1)

# Pound Result Text
pounds_result = Label(text=" ")
pounds_result.grid(column=1, row=1)

# Pounds text
pounds_txt = Label(text=" Pounds")
pounds_txt.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=kg_to_pounds)
button.grid(column=1, row=2)

window.mainloop()
