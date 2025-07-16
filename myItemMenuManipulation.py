import tkinter as tk
from tkinter import messagebox


def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu.entryconfigure(1, state=accessible)

def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter))
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))

def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


accessible = tk.DISABLED
window = tk.Tk()
counter = 10
size = 100
grows = True
window.title(str(counter))
window.bind("<Button-1>", click)
# - window.tk.call(...) → Talks directly to the underlying Tcl interpreter.
# - 'wm', 'iconphoto', ... → Tells the window manager (wm) to set the iconphoto.
# - window._w → Internal Tcl name for your Tkinter window (used under the hood).
# - tk.PhotoImage(file='logo.png') → Loads the image you want as the icon (must be a .png or .gif).
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
# close the window when the user right-clicks anywhere on it
window.bind("<Button-3>", lambda e: window.destroy())
# window is sized to the specified size
window.geometry("100x100")
# user can not minimize the window more the mentioned dimension by dragging the window’s bottom-right corner
window.minsize(width=50, height=50)
# user can not maximize the window more the mentioned dimension
window.maxsize(width=700, height=700)
menu = tk.Menu(window)
window.config(menu=menu)
sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)

# - "WM_DELETE_WINDOW" → The signal sent when the user clicks the window’s close button
window.protocol("WM_DELETE_WINDOW", really)
window.mainloop()

# Property	        Property role
# postcommand	    a callback invoked every time a menu’s item is activated
# tearoff	        set to zero removes the tear-off decoration from the top of the cascade
# state	            when set to DISABLED, the menu item is grayed and inaccessible; setting it to ACTIVE restores its normal functionality
# accelerator	    a string describing a hot-key bound to the menu’s item
# Method	                            Method role
# add_cascade(prop=val, ...)	        adds a cascade to the menu’s item
# add_command(prop=val, ...)	        assigns an action to the menu’s item
# add_separator()	                    adds an separator line to the menu
# entryconfigure(i, prop=val,...)	    modifies the i-th menu item’s property named prop