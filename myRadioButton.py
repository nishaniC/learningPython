import tkinter as tk
from tkinter import messagebox


def show():
    messagebox.showinfo("", "radio_1=" + str(radio_1_var.get()) +
                        ",radio_2=" + str(radio_2_var.get()))


def command_1():
    radio_2_var.set(radio_1_var.get())


def command_2():
    radio_1_var.set(radio_2_var.get())


window = tk.Tk()
button = tk.Button(window, text="Show", command=show)
button.pack()
radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
radio_1_1.select()
radio_1_1.pack()
radio_1_2 = tk.Radiobutton(window, text="clams", variable=radio_1_var, value=2, command=command_1)
radio_1_2.pack()
radio_2_var = tk.IntVar()
radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
radio_2_1.pack()
radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
radio_2_2.select()
radio_2_2.pack()
window.mainloop()


# Radiobutton property	Property meaning
# command	            the callback being invoked when the Radiobutton (not the group it belongs to!) changes its state
# justify	            the same as for Button
# state	                the same as for Button
# variable	            an observable IntVar or StringVar variable reflecting the current selection within the Radiobutton’s group; changing the variable’s value automatically changes the selection
# value	                a unique (inside the group) value identifying the Radiobutton; can be an integer value or a string, and should be compatible with the variable’s type
# Some of the Radiobutton’s methods are shown here.
# Note: there is no toggle() method as a single Radiobutton performs such an operation.
#
# Radiobutton method	Method role
# deselect()	        unchecks the widget
# flash()	            the same as for Button
# invoke()	            the same as for Button
# select()	            checks the widget