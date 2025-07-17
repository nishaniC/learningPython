import tkinter as tk

# --- Setup Window ---
window = tk.Tk()
window.title("Calculator")
window.geometry("300x250")
window.resizable(False, False)

# --- Variables ---
radio_1_var = tk.IntVar(value=1)  # Default to addition
text1 = tk.StringVar()
text2 = tk.StringVar()
last_valid1 = ''
last_valid2 = ''

# --- Validation Functions ---
def digits_only_1(*args):
    global last_valid1
    val = text1.get()
    if val == '' or (val.isdigit() and len(val) <= 5):
        last_valid1 = val
    else:
        text1.set(last_valid1)

def digits_only_2(*args):
    global last_valid2
    val = text2.get()
    if val == '' or (val.isdigit() and len(val) <= 5):
        last_valid2 = val
    else:
        text2.set(last_valid2)

# --- Calculation Logic ---
def evaluate():
    val1 = text1.get()
    val2 = text2.get()

    if val1 == '':
        entry1.focus_set()
        result_label.config(text="Please enter number1")
        return
    if val2 == '':
        entry2.focus_set()
        result_label.config(text="Please enter number2")
        return

    num1 = int(val1)
    num2 = int(val2)
    op = radio_1_var.get()

    try:
        if op == 1:
            result = num1 + num2
        elif op == 2:
            result = num1 - num2
        elif op == 3:
            result = num1 * num2
        elif op == 4:
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                text2.set('')
                entry2.focus_set()
                return
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# --- Widgets ---
# Title Label
title_label = tk.Label(window, text="Calculator", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Entry Fields
entry1 = tk.Entry(window, textvariable=text1, width=15)
entry1.grid(row=1, column=0, padx=10, pady=5)

entry2 = tk.Entry(window, textvariable=text2, width=15)
entry2.grid(row=2, column=0, padx=10, pady=5)

# Radio Buttons
radio_frame = tk.Frame(window)
radio_frame.grid(row=1, column=1, rowspan=2, padx=10)

tk.Radiobutton(radio_frame, text="+", variable=radio_1_var, value=1).pack(anchor='w')
tk.Radiobutton(radio_frame, text="-", variable=radio_1_var, value=2).pack(anchor='w')
tk.Radiobutton(radio_frame, text="*", variable=radio_1_var, value=3).pack(anchor='w')
tk.Radiobutton(radio_frame, text="/", variable=radio_1_var, value=4).pack(anchor='w')

# Evaluate Button
eval_button = tk.Button(window, text="Evaluate", command=evaluate)
eval_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# --- Traces ---
text1.trace_add("write", digits_only_1)
text2.trace_add("write", digits_only_2)

window.mainloop()