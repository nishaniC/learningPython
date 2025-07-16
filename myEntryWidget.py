import tkinter as tk


def digits_only(*args):
    global last_string
    string = text.get()
    if string == '' or string.isdigit() and len(entry.get())<6:  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)

def show_input():
    user_input = entry.get()
    print("You entered:", user_input)


last_string = ''
window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(last_string)
text.trace('w', digits_only)
entry.pack()
# entry.focus_set()
button = tk.Button(window, text="Submit", command=show_input)
button.pack()
window.mainloop()
# Entry property	Property meaning
# command	        although Entry is obviously a clickable widget, it doesn’t allow you to bind a callback through the command property.
#                   You can observe and control all occurring changes instead by setting the tracer function for the observable variable
#                   which cooperates with Entry
# show	            a string assigned to this property will be displayed instead of the actual characters entered into the input field;
#                   e.g., if you set show='*', this will enable the widget to safely edit the user’s password
# state	            the same as for Button(if you set the property to DISABLED, the button becomes deaf and doesn’t react to clicks, while its title is shown in gray;
#                   setting it to NORMAL restores normal button functioning; when the mouse is located above the button, the property changes its value to ACTIVE)
# textvariable	    an observable StringVar reflecting the current state of the input field
# width	            the input field’s width (in characters)
#
# Entry method	            Method role
# get()	                    returns the current input field’s contents as a string
# set(s)	                sets the whole input field’s contents with the s string
# delete(first, last=None)	deletes a part of the input field’s contents; first and last can be integers with values indexing the string;
#                           if the last argument is omitted, a single character is deleted; if last is specified as END, it points to the place after the last field’s character
# insert(index, s)	        inserts the s string at the field position pointed to by index