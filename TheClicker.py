import tkinter as tk
from tkinter import messagebox
import random

def main():
    global window, starter, stop_timer, nextnum, counter, numbers, correct_click, sorted_numbers, label
    window = tk.Tk()
    window.title("Clicker")
    starter =True
    stop_timer=False
    nextnum = 0
    counter = 0  # Start from 0
    numbers=[]
    correct_click=0


    def update_timer():
        global stop_timer
        if not stop_timer:
            global counter
            counter += 1
            label.config(text=str(counter))
            window.after(1000, update_timer)  # Call again after 1 second

    def click(event=None):
        global nextnum
        global starter
        global stop_timer
        if starter:
            update_timer()
            nextnum=sorted_numbers[0]
            starter = False

        button1= event.widget
        global correct_click
        if int(button1.cget("text")) == nextnum:
            button1.configure(state=tk.DISABLED)
            if correct_click < len(sorted_numbers)-1:
                correct_click += 1
                nextnum = sorted_numbers[correct_click]
                print("nextnum: "+str(nextnum))
                print("correct_click: " + str(correct_click))
            else:
                stop_timer=True
                tk.messagebox.showinfo("Clicked!",  f"You did it in {counter} seconds!")

    for i in range(25):
        num = random.randint(1, 999)
        while num in numbers:
            num = random.randint(1, 999)
        numbers.append(num)
        col = i%5
        ro = i//5
        i = tk.Button(window, text=str(num))
        i.bind("<Button-1>", click)
        i.grid(column=col, row=ro)
    sorted_numbers = sorted(numbers)

    label = tk.Label(window, text="0")
    label.grid(column=2,row=6)

    def reset_game():
        window.destroy()
        main()  # Wrap your game setup in a main() function

    reset_btn = tk.Button(window, text="Reset", command=reset_game)
    reset_btn.grid(column=2, row=8)
    window.mainloop()

main()





