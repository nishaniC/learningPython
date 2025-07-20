from random import randrange
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

def computersturn2():
    if not buttons or not game_active:
        return
    while True:
        if len(buttons) == 8:
            randomnumber = randrange(0, len(buttons))
            button = buttons[randomnumber]
        else:
            info = clicked_buttons[len(clicked_buttons-1)].grid_info()
            row = info["row"]
            column = info["column"]


        if button["state"] != tk.DISABLED:
            button.configure(text="X", state=tk.DISABLED)
            buttons.remove(button)
            clicked_buttons.append(button)
            check()
            break

def computersturn():
    if not buttons or not game_active:
        return
    while True:
        randomnumber = randrange(0, len(buttons))
        button = buttons[randomnumber]
        if button["state"] != tk.DISABLED:
            button.configure(text="X", state=tk.DISABLED)
            buttons.remove(button)
            clicked_buttons.append(button)
            check()
            break
    # randomnumber = randrange(0,len(buttons))
    # button = buttons[randomnumber]
    # if button["state"] != tk.DISABLED:
    #     button.configure(text="X")
    #     button.configure(state=tk.DISABLED)
    #     buttons.remove(button)
    #     clicked_buttons.append(button)
    #     check()
def disable_all_buttons():
    global game_active
    game_active = False
    for btn in buttons:
        btn.configure(state=tk.DISABLED)

def createxo():
    for clicked_button in clicked_buttons:
        info = clicked_button.grid_info()
        row = info["row"]
        column = info["column"]
        mark = clicked_button["text"]
        if row == 0:
            index= column
        elif row==1:
            index = 3 + column
        elif row==2:
            index = 6 + column

        xo[index] = mark


win_patterns = [
    [0,1,2], [3,4,5], [6,7,8],  # rows
    [0,3,6], [1,4,7], [2,5,8],  # columns
    [0,4,8], [2,4,6]            # diagonals
]

def check():
    createxo()
    print(xo)
    for pattern in win_patterns:
        a, b, c = pattern
        if xo[a] == xo[b] == xo[c]:
            winner = xo[a]
            if winner in ("X", "O"):
                messagebox.showinfo("Game Over", f"{'Computer' if winner == 'X' else 'You'} win!")
                disable_all_buttons()
                return

    # if xo[0]==xo[1]==xo[2]== "X":
    #     print(xo)
    #     messagebox.showinfo("Game Over", "computer wins!")
    #
    # elif xo[0]==xo[1]==xo[2]== "O":
    #     print(xo)
    #     messagebox.showinfo("Game Over","You win!")
    #
    # elif xo[3]==xo[4]==xo[5]== "X":
    #     print(xo)
    #     messagebox.showinfo("Game Over","computer wins!")
    #
    # elif xo[3]==xo[4]==xo[5]== "O":
    #     print(xo)
    #     messagebox.showinfo("Game Over","You win!")
    #
    # elif xo[6]==xo[7]==xo[8]== "X":
    #     print(xo)
    #     messagebox.showinfo("Game Over","computer wins!")
    #
    # elif xo[6]==xo[7]==xo[8]== "O":
    #     print(xo)
    #     messagebox.showinfo("Game Over","You win!")
    #
    # elif xo[0]==xo[3]==xo[6]== "X":
    #     print(xo)
    #     messagebox.showinfo("Game Over","computer wins!")
    #
    # elif xo[0]==xo[3]==xo[6]== "O":
    #     print(xo)
    #     messagebox.showinfo("Game Over","You win!")
    #
    # elif xo[1]==xo[4]==xo[7]== "X":
    #     print(xo)
    #     messagebox.showinfo("Game Over","computer wins!")
    #
    # elif xo[1]==xo[4]==xo[7]== "O":
    #     print(xo)
    #     messagebox.showinfo("Game Over","You win!")
    # elif xo[2]==xo[5]==xo[8]== "X":
    #     print(xo)
    #     messagebox.showinfo("Game Over","computer wins!")
    # elif xo[2]==xo[5]==xo[8]== "O":
    #     print(xo)
    #     messagebox.showinfo("Game Over","You win!")
    # elif xo[0]==xo[4]==xo[8]== "X":
    #     print(xo)
    #     messagebox.showinfo("Game Over","computer wins!")
    # elif xo[0]==xo[4]==xo[8]== "O":
    #     print(xo)
    #     messagebox.showinfo("Game Over","You win!")
    #
    # elif len(clicked_buttons)==9:
    #     print(xo)
    #     messagebox.showinfo("Game Over", "No more moves!")



def clicked(event=None):
    print("user clicked the Button!")
    button = event.widget
    if button["state"] != tk.DISABLED:

        # try:
        #     index = buttons.index(button)
        #     xo.remove(str(index+1))
        #     xo.insert(index, "O")
        # except ValueError:
        #     print(xo)
        # return
        button.configure(state=tk.DISABLED)
        button.configure(text="O")
        buttons.remove(button)
        clicked_buttons.append(button)
        check()
        if buttons:
            window.after(300,computersturn)

game_active = True
clicked_buttons=[]
buttons=[]
xo=["1", "2","3","4","5","6","7","8","9"]
for i in range(3):
    for j in range(3):
        btn = tk.Button(window, text=" ", width=6, height=3)
        btn.bind("<Button-1>", clicked)
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(btn)
print(buttons)

window.mainloop()












