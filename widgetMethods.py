import tkinter as tk


def blink():
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    global number
    number+=1
    print(number)
    event_id = frame.after(1500, blink)
    if number == 10:
        frame.after_cancel(event_id)
        window.destroy()


is_white = True
number = 1

window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
frame.after(500, blink)
frame.pack()
window.mainloop()
