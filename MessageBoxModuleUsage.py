import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import CANCEL, ERROR


def question():
    answer = messagebox.askyesno("?", "To be or not to be?",icon='info'
)
    # icon – sets the non-default icon for the dialog: possible values are: ERROR, INFO, QUESTION-default icon, and WARNING.
    print(answer)

def question2():
    # creates a dialog equipped with two buttons titled OK and Cancel (it returns True for OK and False otherwise).
    answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    print(answer)

def question3():
    # creates a dialog containing a warning sign instead of a question mark and two buttons titled Retry and Cancel (it returns True for Retry and False otherwise).
    answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
    print(answer)

def question4():
    # displays two buttons titled Yes and No along with a question mark icon, but returns a string Yes when the user’s answer is positive and No otherwise.
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    print(answer)

def question5():
    # displays a red warning icon and doesn’t ask any questions – its only button is titled OK. It also returns a string OK in every case
    answer = messagebox.showerror("!", "Your code does nothing!")
    print(answer)

def question6():
    #  it’ll present a warning icon and always returns OK.
    answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
    print(answer)

window = tk.Tk()
button = tk.Button(window, text="Ask the question!", command=question)
button.pack()
button2 = tk.Button(window, text="What are your plans?", command=question2)
button2.pack()
button3 = tk.Button(window, text="What are your plans2?", command=question3)
button3.pack()
button4 = tk.Button(window, text="What are your plans3?", command=question4)
button4.pack()
button5 = tk.Button(window, text="Alarming message", command=question5)
button5.pack()
button6 = tk.Button(window, text="What's going on?", command=question6)
button6.pack()
window.mainloop()
# title – a string displayed in the dialog’s title bar (it can’t be very long, of course);
# message – a string displayed inside the dialog; note: the \n plays its normal role and breaks up the message’s lines;
# options – a set of options shaping the dialog in a non-default way, two of which are useful to us:
#       default – sets the default (pre-focused) answer; usually, it’s focused on the button located first from the left; this can be changed by setting the keyword argument with identifiers like CANCEL, IGNORE, OK, NO, RETRY, and YES;
#       icon – sets the non-default icon for the dialog: possible values are: ERROR, INFO, QUESTION, and WARNING.
# If you ever want to set defaults like CANCEL, YES, NO, RETRY, etc., they only work inside tk.call(...), not the handy helper like askyesno().