import tkinter as tk
from tkinter import messagebox

def click():
    tk.messagebox.showinfo("Clicked!", "You win")

def jump(event=None):
    # Get current mouse position
    x1 = event.x_root - window.winfo_rootx()
    y1 = event.y_root - window.winfo_rooty()

    if x1+50<500:
            x1=x1+50
    else:
            x1=10
    if y1+50<500:
            y1=y1+50
    else:
            y1=10
    button.place(x=x1, y=y1)

window = tk.Tk()
window.title("Catch me!")
window.geometry("500x500")
button = tk.Button(window, text="Catch me!", command=click)
button.bind("<Enter>", jump)
button.place(x=10, y=10)
window.mainloop()