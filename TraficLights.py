import tkinter as tk

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

window = tk.Tk()
window.geometry("155x500")
canvas = tk.Canvas(window, width=150, height=400, bg='#363737')
canvas.grid(row=0)
num_phases=len(phases)
next_phase=0
num_lights=len(phases[0])
colours=['red','yellow','green']
oval_ids=[]
for i in range(num_lights):
    oval_ids.append(canvas.create_oval(40, 40+(i*120), 140, 140+(i*120), outline='black', width=5, fill='gray'))
    # tf2=canvas.create_oval(40, 160, 140, 260, outline='black', width=5, fill='gray')
    # tf3=canvas.create_oval(40, 280, 140, 380, outline='black', width=5, fill='gray')
# print(oval_ids)
button = tk.Button(window, text="Quit", command=window.destroy)

def nextstage():
    global next_phase
    for n in range(num_lights):
        canvas.itemconfig(oval_ids[n], fill='gray')
    if next_phase==num_phases:
        next_phase=0
    color_pattern=phases[next_phase]
    for j in range(len(color_pattern)):
        if color_pattern[j]:
            canvas.itemconfig(oval_ids[j], fill=colours[j])
    next_phase+=1

button2 = tk.Button(window, text="Next", command=nextstage)
button.grid(row=1)
button2.grid(row=2)
window.mainloop()