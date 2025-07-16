import tkinter as tk


def do_it_again():
    text.set(text.get() + "and again...")


window = tk.Tk()
button = tk.Button(window, text="Go ahead!", command=do_it_again)
button.pack()
text = tk.StringVar()
message = tk.Message(window, textvariable=text, width=400)
text.set("You did it again... ")
message.pack()
window.mainloop()
# Message property	Property meaning
# text	            a string which will be shown within the Label; note: newline characters (\n) are interpreted in the usual way
# textvariable	    the same as for text, but makes use of an observable StringVar variable, so if you change the variable’s alteration, it will be immediately visible on the screen.