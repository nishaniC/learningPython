import tkinter as tk

def add(event=None):
    global operation
    global string1
    global number1
    global number2
    global afterAnOp
    operation = '+'
    print(operation)
    if number1 == '':
        try:
            number1 = int(string1)

        except:
            pass
        string1 = ''
        text.set(string1)
    elif number2 == '':
        try:
            number2 = int(string1)
        except :
            pass
        number1+=number2
        number2=''
        string1 = str(number1)
        if len(string1) > 10:
            number1=''
            string1=str(number1)
        number1 = int(string1)
        text.set(string1)
        afterAnOp=True

def subtraction(event=None):
    global operation
    global string1
    global number1
    global number2
    global afterAnOp
    operation = '-'
    if number1 == '':
        try:
            number1 = int(string1)

        except:
            pass
        string1 = ''
        text.set(string1)
    elif number2 == '':
        try:
            number2 = int(string1)
        except:
            pass
        number1 -= number2
        number2 = ''
        string1 = str(number1)
        if len(string1) > 10:
            number1 = ''
            string1 = number1
        number1 = int(string1)
        text.set(string1)
        afterAnOp = True

def multiplication(event=None):
    global operation
    global string1
    global number1
    global number2
    global afterAnOp
    operation = '*'
    if number1 == '':
        try:
            number1 = int(string1)

        except:
            pass
        string1 = ''
        text.set(string1)
    elif number2 == '':
        try:
            number2 = int(string1)
        except:
            pass
        number1 *= number2
        number2 = ''
        string1 = str(number1)
        if len(string1) > 10:
            number1 = ''
            string1 = number1
        number1 = int(string1)
        text.set(string1)
        afterAnOp = True

def division(event=None):
    global operation
    global string1
    global number1
    global number2
    global afterAnOp
    operation = '/'
    print(operation)
    if number1 == '':
        try:
            number1 = int(string1)

        except:
            pass
        string1 = ''
        text.set(string1)
    elif number2 == '':
        try:
            number2 = int(string1)
        except:
            pass
        print("number2 type = ",type(number2),", number1 = ",type(number1))
        number1 /= number2
        number2 = ''
        string1 = str(number1)
        if len(string1) > 10:
            number1 = string1[:10]
            string1 = str(number1)

        text.set(string1)
        number1 = float(string1)
        afterAnOp = True

def equal(event=None):
    global operation
    global number1
    global string1
    global number2
    print("in equal")
    if number1 != '':
        print("in equal and numers are filled")
        if operation == '+':
            print("btnplus.invoke()")
            btnplus.event_generate("<Button-1>")
        if operation == '-':
            print("btnminus.event_gen")
            btnminus.event_generate("<Button-1>")
        if operation == '*':
            print("btnmul.event_generate")
            btnmul.event_generate("<Button-1>")
        if operation == '/':
            print("btndivide.event_generate")
            btndivide.event_generate("<Button-1>")

def sign(event=None):
    button = event.widget
    global string1
    global sign1
    global number1
    sign2 = ''
    try:
        sign2=string1[0]
    except:
        pass
    if sign1=="+":
        sign1 = "-"
        if sign2 != '-'  :
            string1 = sign1 + string1[:9]
        else:
            string1=string1
    else:
        sign1 = "+"
        if sign2 == '-'  :
            string1 = string1[1:9]
        else:
            string1 = string1
    text.set(string1)
    if number1 != '':
        number1 = ''

def decimalpoint(event=None):
    button = event.widget
    global string1
    number = button["text"]
    if len(string1) < 9:
        string1 += str(number)
        text.set(string1)

def clicked(event=None):
    button=event.widget
    global afterAnOp
    global string1
    number = button["text"]
    if afterAnOp:
        string1 = ''
        text.set(string1)
        afterAnOp=False
    if len(string1) < 11:
        string1 += str(number)
        text.set(string1)

def clear(event=None):
    button = event.widget
    global string1
    global number1
    global number2
    string1 = string1[:len(string1)-1]

    if len(string1) < 11:
        text.set(string1)
    if len(string1) == 0:
        number1 = ''
        number2 = ''

string1 = ''
sign1 = "+"
afterAnOp = False
number1=''
number2=''
operation=''
window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(string1)
entry.place(x=10, y=10, width=150, height=25)

btn7 = tk.Button(window, text="7", width=6, height=3)
btn7.bind("<Button-1>", clicked)
btn7.place(x=10, y=40, width=25, height=25)
btn8 = tk.Button(window, text="8", width=6, height=3)
btn8.bind("<Button-1>", clicked)
btn8.place(x=40, y=40, width=25, height=25)
btn9 = tk.Button(window, text="9", width=6, height=3)
btn9.bind("<Button-1>", clicked)
btn9.place(x=70, y=40, width=25, height=25)
btnplus = tk.Button(window, text="+", width=6, height=3)
btnplus.bind("<Button-1>", add)
btnplus.place(x=130, y=40, width=25, height=25)

btn4 = tk.Button(window, text="4", width=6, height=3)
btn4.bind("<Button-1>", clicked)
btn4.place(x=10, y=70, width=25, height=25)
btn5 = tk.Button(window, text="5", width=6, height=3)
btn5.bind("<Button-1>", clicked)
btn5.place(x=40, y=70, width=25, height=25)
btn6 = tk.Button(window, text="6", width=6, height=3)
btn6.bind("<Button-1>", clicked)
btn6.place(x=70, y=70, width=25, height=25)
btnminus = tk.Button(window, text="-", width=6, height=3)
btnminus.bind("<Button-1>", subtraction)
btnminus.place(x=130, y=70, width=25, height=25)

btn1 = tk.Button(window, text="1", width=6, height=3)
btn1.bind("<Button-1>", clicked)
btn1.place(x=10, y=100, width=25, height=25)
btn2 = tk.Button(window, text="2", width=6, height=3)
btn2.bind("<Button-1>", clicked)
btn2.place(x=40, y=100, width=25, height=25)
btn3 = tk.Button(window, text="3", width=6, height=3)
btn3.bind("<Button-1>", clicked)
btn3.place(x=70, y=100, width=25, height=25)
btnequal = tk.Button(window, text="=", width=6, height=3)
btnequal.bind("<Button-1>", equal)
btnequal.place(x=100, y=100, width=25, height=25)
btnmul = tk.Button(window, text="*", width=6, height=3)
btnmul.bind("<Button-1>", multiplication)
btnmul.place(x=130, y=100, width=25, height=25)

btn0 = tk.Button(window, text="0", width=6, height=3)
btn0.bind("<Button-1>", clicked)
btn0.place(x=10, y=130, width=25, height=25)

btnc = tk.Button(window, text="C", width=6, height=3)
btnc.bind("<Button-1>", clear)
btnc.place(x=40, y=130, width=25, height=25)

btndot = tk.Button(window, text=".", width=6, height=3)
btndot.bind("<Button-1>", decimalpoint)
btndot.place(x=70, y=130, width=25, height=25)

btnsign = tk.Button(window, text="+/-", width=6, height=3)
btnsign.bind("<Button-1>", sign)
btnsign.place(x=100, y=130, width=25, height=25)

btndivide = tk.Button(window, text="/", width=6, height=3)
btndivide.bind("<Button-1>", division)
btndivide.place(x=130, y=130, width=25, height=25)
window.mainloop()

