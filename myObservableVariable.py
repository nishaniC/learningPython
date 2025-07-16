# import tkinter as tk
# from tkinter import messagebox
#
#
# def hi(id, ix, act):
#     messagebox.showinfo('Message', 'Hello')
#
# window = tk.Tk()
#
# s = tk.StringVar()
# obsid = s.trace("r", hi)
# s.set("To be or not to be")
# sn = s.get()
#
# print(sn)
# window.mainloop()


import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)
variable.set(variable.get() + 'd')  # read followed by write
variable.trace_remove("read", r_obsid)
variable.set(variable.get() + 'e')
variable.trace_remove("write", w_obsid)
variable.set(variable.get() + 'f')
print(variable.get())
