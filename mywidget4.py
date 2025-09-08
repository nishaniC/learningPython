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

