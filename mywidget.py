import tkinter as tk


def on_off():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()

#==================================================================
import tkinter as tk


def on_off():
    global button
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button.config(text=state)


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()

#====================================================================================
import tkinter as tk


window = tk.Tk()
label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
label_3.grid(column=0, row=2)
window.mainloop()
#===========================================================================
import tkinter as tk


window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Exceptional button")
button_2.pack()

button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
button_2["borderwidth"] = 16
#button_2["wraplength"] = 46
#button_2["height"] = 7
#button_2["width"] = 28

window.mainloop()

# Widget property name	Property role
# borderwidth	        The width of the 3D-frame surrounding some widgets (e.g., Button)
# highlightthickness	    The width of the additional frame drawn around the widget when it gains the focus
# padx

# pady	                The width/height of an additional empty space/margin around the widget
# wraplength	            If the text filling the widget becomes longer than this property’s value, it will be wrapped (possibly more than once)
# height	                The height of the widget
# underline	            The index of the character inside the widget’s text, which should be presented as underlined or -1 otherwise (the underlined letter/digit can be used as a shortcut key, but it needs a specialized callback to work – no automation here, sorry)
# width	                The width of the widget
#==============================================================
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Colorful button")
button_2.pack()
button_2.config(bg ="#000000")
button_2.config(fg ="yellow")
button_2.config(activeforeground ="#FF0000")
button_2.config(activebackground ="green")
window.mainloop()
# 
# Widget property name	Property role
# background

# bg	                The color of the widget’s background (you can freely use either of these two forms)
# foreground

# fg	                The color of the widget’s foreground (note: it can mean different things in different widgets; in general, it’s used to specify text color)
#activeforeground

# activebackground	    Like bg and fg but used when the widget becomes active
# disabledforeground	The width of the widget
#==========================================================================
import tkinter as tk


window = tk.Tk()
button_1 = tk.Button(window, text="Regular button");
button_1["anchor"] = tk.E
button_1["width"] = 20  # pixels!
button_1.pack()
button_2 = tk.Button(window, text="Another button")
button_2["anchor"] = tk.SW
button_2["width"] = 20
button_2["height"] = 3  # rows
button_2.pack()
window.mainloop()
