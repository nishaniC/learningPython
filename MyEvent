Useful events
We’ve gathered some of the most usable event names – don’t try to learn them by heart.

Event name	Event role
<Button-1>	Single left-click (if your mouse is configured for a right-handed user)
<Button-2>	Single middle-click
<Button-3>	Single right-click
<ButtonRelease-1>	Left mouse button release

Note: there are also events named <ButtonRelease-2> and <ButtonRelease-3>
<DoubleButton-1>	Double left-click

Note: there are also events named <DoubleButton-2> and <DoubleButton-3>

Note again: the <Button-1> event is a part of <DoubleButton-1> too; if you assign a callback to <Button-1>, it will be launched, too!

Event name	Event role
<Enter>	Mouse cursor appears over the widget
<Leave>	Mouse cursor leaves the widget area
<Focus-In>	The widget gains the focus
<Focus-Out>	The widget loses the focus
<Return>	The user presses the Enter/Return key
<Key>	The user presses any key

Event name	Event role
x	The user presses x key (x can be neither a space nor the < key)
<space>	The user presses the spacebar
<less>	The user presses the < key
<Cancel>	The user presses the key/keys used by the current OS to stop the program (e.g., Ctrl-C or Ctrl-Break)
<BackSpace>	The user presses the Backspace key
<Tab>	The user presses Tab key


Event name	Event role
<Shift_L>	The user presses one of the Shift keys
<Control_L>	The user presses one of the Control keys
<Alt_L>	The user presses one of the Alt keys
<Pause>	The user presses the Pause key
<Caps_Lock>	The user presses the Caps Lock key
<Esc>	The user presses the Escape keys

Event name	Event role
<Prior>	The Page Up key
<Next>	The Page Down key
<End>	The End key
<Home>	The Home key
<Left>

<Right>

<Up>

<Down>	Cursor (arrows) keys
<Num_Lock>

<Scroll_Lock>	The two Lock keys
<Shift-x>

<Alt-x>

<Control-x>	The x key has been pressed along with any of the Shift, Alt, or Control keys

Property name	Property role
widget	The widget’s object (not the widget’s name!) to which the event is addressed
<x>

<y>	The mouse cursor’s coordinates at the moment of the event’s occurrence (both coordinates are counted relative to the target widget)
<x_root>

<y_root>	As above, but relative to the screen
<char>	The pressed key character code (only for keyboard events)
<keysym>	The pressed key symbol (only for keyboard events)
The full list of all recognized key symbols is presented here: https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
<keycode>	The pressed key numerical code (only for keyboard events)
Don’t confuse this with char, which is the ASCII/UNICODE code of the character bound to the key
<num>	The number of the clicked mouse button (only for mouse events)
<type>	The event’s type

#=============================================================================================================================




import tkinter as tk
from tkinter import messagebox


def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)        


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()
# ===========================================================================================================
import tkinter as tk
from tkinter import messagebox


def on_off():
    global switch
    if switch:
        button_2.config(command=lambda: None)
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch


def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")


def do_nothing():
    pass


switch = True
window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()
#==========================================================
import tkinter as tk

def on_off(event=None):
    global switch
    if switch:
        label.unbind("<Button-1>")
        status.config(text="Switched OFF")
    else:
        label.bind("<Button-1>", rhyme)
        status.config(text="Switched ON")
    switch = not switch

def rhyme(event):
    global word_no
    word_no += 1
    label.config(text=words[word_no % len(words)])

switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0

window = tk.Tk()
window.title("Whimsical Rhymer")

button = tk.Button(window, text="On/Off Button", command=on_off)
button.pack()

label = tk.Label(window, text=words[0], font=("Helvetica", 24))
label.bind("<Button-1>", rhyme)
label.bind("<Enter>", on_off)
label.bind("<Leave>", on_off)
label.pack(pady=10)

status = tk.Label(window, text="Switched ON")
status.pack()

# Bind spacebar to toggle
window.bind("<space>", on_off)
window.geometry("400x200")

window.mainloop()

