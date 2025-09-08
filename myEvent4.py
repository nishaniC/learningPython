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
