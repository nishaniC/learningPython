
# a classic menu is actually a horizontal bar located at the top of the application window;
# the bar contains a number of horizontally deployed options, often referred to as items or entries;
# these options can have hot-keys (keyboard shortcuts enabling the user to quickly access selected operations without using a mouse; usually, hot-keys are triggered by pressing Alt-hotkey on the keyboard)
# selecting a menu’s option (it doesn’t matter whether through a hotkey or by a mouse click) causes one of two effects:
# it launches a callback bound to the option;
# it unrolls a new menu (actually a submenu)
# if you want to have such a menu within your Tkinter application, you have to:
# create a top-level menu object;
# embed it inside the window;
# bind a number of required submenus (this is called a cascade) or connect a single callback.
import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")

def are_you_sure():
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()

def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")

window = tk.Tk()
# main menu creation
main_menu = tk.Menu(window)
window.config(menu=main_menu)
# The config() method is used to configure widget options after a widget has been created.
# - You can use config() to update: text, bg, fg, font, state, command, etc.
# You can also use .configure()—they're interchangeable in Tkinter.
# 1st main menu item a sub menu
sub_menu_file = tk.Menu(main_menu, tearoff=0)#Use tearoff=0 to remove the dashed line at the top of submenus.

main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)# setting the hotkey to "Alt-F"
# The .add_cascade() method in Tkinter is used to add a submenu to a menu—essentially creating a dropdown menu structure.
# It’s how you build hierarchical menus like “File → Open” or “Help → About”.
# 🧪 Syntax
# menu.add_cascade(label="Menu Name", menu=submenu, underline=N)
# - label: The name shown on the parent menu.
# - menu: The Menu object that acts as the submenu.
# - underline: (Optional) Index of the character to underline for Alt-key access.
# 🧠 Key Notes
# - .add_cascade() is used only to attach a submenu to a parent menu.
# - If you want to add a clickable item (not a submenu), use .add_command() instead.

# The .add_command() method in Tkinter is used to add a clickable menu item to a Menu widget. When the user clicks that item, a specified function (command) is executed.
# 🧪 Basic Syntax
# menu.add_command(label="Item Name", command=function_name, underline=N)
# - label: The text shown in the menu.
# - command: The function to call when the item is clicked.
# - underline: (Optional) Index of the character to underline for keyboard access (Alt + key).
# 🧠 Notes
# - You can add multiple add_command() items to the same menu.
# - Use add_separator() to insert a horizontal line between items.
# - command= can also be a lambda if you need to pass arguments.

# add the Open action to the submenu
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# another submenu
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)

    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

# separator is here!
sub_menu_file.add_separator()
# add the QUIT action to the submenu
sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)

# 2nd main menu item: a simple callback
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)# setting the hotkey to "Alt-B"
# Note: you’re obliged to ensure that all hotkeys are unique!
window.mainloop()
#
