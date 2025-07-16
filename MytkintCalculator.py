import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("      Calculator             ")


def click():
    if entry.get() == "" or entry2.get() == "":
        tk.messagebox.showerror("Error", "Please enter two numbers")
        return
    number1=int(entry.get())
    number2=int(entry2.get())
    calculatednum=0

    if radio_1_var.get()== 1:
        calculatednum = number1 + number2
    if radio_1_var.get() == 2:
        calculatednum = number1 - number2
    if radio_1_var.get() == 3:
        calculatednum = number1 * number2
    if radio_1_var.get() == 4:
        if number2 != 0:
            calculatednum = number1 / number2
        else:
            tk.messagebox.showerror("Error", "number2 cannot be zero")
            return

    tk.messagebox.showinfo("Click!", str(calculatednum))

def digits_only(*args):
    global last_string
    string = text.get()
    if string == '' or string.isdigit() and len(entry.get())<6:  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)

def digits_only2(*args):
    global last_string2
    string = text2.get()
    if string == '' or string.isdigit() and len(entry2.get())<6:  # Field's content is valid.
        last_string2 = string
    else:
        text.set(last_string2)

def command_1():
    radio_1_var.set(radio_1_var.get())



radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="+", variable=radio_1_var, value=1, command=command_1)
radio_1_1.select()
radio_1_1.grid(column=1,row=0)
radio_1_2 = tk.Radiobutton(window, text="-", variable=radio_1_var, value=2, command=command_1)
radio_1_2.grid(column=1,row=1)
radio_1_3 = tk.Radiobutton(window, text="*", variable=radio_1_var, value=3, command=command_1)
radio_1_3.grid(column=1,row=2)
radio_1_4 = tk.Radiobutton(window, text="/", variable=radio_1_var, value=4, command=command_1)
radio_1_4.grid(column=1,row=3)

last_string = ''
last_string2 = ''
text = tk.StringVar()
text2 = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
entry2 = tk.Entry(window, textvariable=text2)
text.set(last_string)
text.trace_add('write', digits_only)
text2.set(last_string2)
text2.trace_add('write', digits_only2)

button = tk.Button(window, text="Evaluate", command=click)
entry.grid(column=0,row=1)
entry2.grid(column=3,row=1)
button.grid(column=1,row=4)
window.mainloop()