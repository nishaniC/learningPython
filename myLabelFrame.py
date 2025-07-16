import tkinter as tk

window = tk.Tk()
label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                              width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2",
                              labelanchor='se', width=200, height=100, bg='yellow')

button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

label_frame_1.pack()
label_frame_2.pack()
window.mainloop()
# LabelFrame property	Property meaning
# takefocus	            normally, the Frame doesn’t take the focus (which would seem to be obvious) but if you really want it to behave in this way, you can set the property to 1.
# text	                the LabelFrame’s title
# labelanchor	        the title’s location, defined as a string containing a quasi-compass coordinate('nw','n','ne','en','e','es','se','s','sw','ws','w','wn')