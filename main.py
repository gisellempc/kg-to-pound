from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


# Button
def button_clicked():
    key = input_text.get()
    my_label["text"] = key


button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

button2 = Button(text="useless button")
button2.grid(row=2, column=0)

#Entry
input_text = Entry(width=10)
input_text.grid(row=3, column=2)

window.mainloop()
