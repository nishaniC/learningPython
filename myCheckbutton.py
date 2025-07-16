# Checkbutton property	Property meaning
# bd	the checkbutton frame width (default is two pixels)
# command	the callback being invoked when the checkbutton changes its state
# justify	the same as for Button
# state	the same as for Button
# variable	an observable IntVar variable reflecting the widget’s state; defaultly it’s set to 1 when the checkbutton is checked, and to 0 otherwise
# offvalue	the non-default value being assigned to a variable when the checkbutton is not checked
# onvalue	the non-default value being assigned to a variable when the checkbutton is checked
#
# And now some of its methods:
#
# Checkbutton method	Method role
# deselect()	unchecks the widget
# flash()	the same as for Button
# invoke()	the same as for Button
# select()	checks the widget
# toggle()	toggles the widget (changes its state to the opposite one)

import tkinter as tk
from tkinter import messagebox


def count():
    global counter
    counter += 1

def show():
    messagebox.showinfo("","counter=" + str(counter) + ",state=" + str(switch.get()))


window = tk.Tk()
switch = tk.IntVar()
counter = 0
button = tk.Button(window, text="Show", command=show)
button.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()
window.mainloop()
