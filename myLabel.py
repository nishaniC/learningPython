import tkinter as tk


def to_string(x):
    return "Current counter\nvalue is:\n" + str(x)


def plus():
    global counter
    counter += 1
    text.set(to_string(counter))


counter = 0
window = tk.Tk()
button = tk.Button(window, text="Go on!", command=plus)
button.pack()
text = tk.StringVar()
label = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label.pack()
window.mainloop()




# Label property	Property meaning
# text	            a string which will be shown within the Label; note: newline characters (\n) are interpreted in the usual way
# textvariable	    the same as for text, but makes use of an observable StringVar variable, so if you change the variable’s alteration, it will be immediately visible on the screen.