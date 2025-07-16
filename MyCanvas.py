import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
# creates a 400 x 400-pixel canvas with a yellow background
canvas = tk.Canvas(window, width=600, height=600, bg='yellow')
# draws a line (precisely: a polygonal chain) consisting of three line segments
# This creates line segments connecting these points in order:
# - (10, 380) → (200, 10)
# - (200, 10) → (380, 380)
# - (380, 380) → (10, 380)
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380,
                   arrow=tk.BOTH, fill='red', smooth=True, width=4)

# Both the top-left and bottom-right coordinates in create_rectangle(x1, y1, x2, y2) are measured relative to the canvas's top-left corner, which is (0, 0)
# Draws a rectangle from top-left (50, 50) to bottom-right (150, 150)
canvas.create_rectangle(50, 50, 150, 150, outline='white', width=5, fill='red')
canvas.create_rectangle(200, 100, 300, 300, outline='black', width=5, fill='purple')

# Drawing a polygon looks very similar to drawing a line, with the difference being that the last segment
#(connecting the first and the last points) in the chain is drawn automatically (you don’t need to specify the same point as the first and the last (x,y) pair
canvas.create_polygon(20, 180, 200, 68, 80, 80,250,70, outline='green', width=5, fill='pink')

# The method draws an ellipse inscribed in a rectangle with vertices at the points (x0,y0) and (x1,y1).
# Vertices are the corner points where two or more lines or edges meet, forming the shape's structure.
# If the rectangle is a square, the ellipse becomes a circle.
canvas.create_oval(40, 40, 140, 140, outline='orange', width=20, fill='white')

# arc (a part of an ellipse)
# The method draws the arc of an ellipse inscribed inside a rectangle with vertices at points (x0,y0) and (x1,y1).
# Option name	Option meaning
# style	        can be set to one of the following: PIESLICE (default)(A filled wedge shape, like slicing into a pie),
#               CHORD(A filled shape bordered by the arc and a straight line between start/end.) and ARC(Just the outline curve of the arc. No fill, no connecting lines.);
# start	        the angle (in degrees) of the arc’s start relative to the X-axis (e.g., 90 means the highest point of the ellipse, while 0 is the right-most point. The default is 0)
#               - Where the arc begins, in degrees, measured from the positive X-axis (3 o’clock position).
#               - 0° is right
#               - 90° is top
#               - 180° is left
#               - 270° is bottom
# extent	    the arc’s span (in degrees) relative to the start point; note: the span is calculated counter-clockwise. The default is 90 (a quarter of an ellipse)
#               - 90° gives you one quarter of the ellipse
#               - 180° gives you a half
#               - 360° gives you a full ellipse (but the effect depends on style
canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
                  style=tk.CHORD, start=90, fill='white')
canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
                  style=tk.ARC, start=180, extent=180)

# puts text on the Canvas. The text is placed inside a rectangle whose center is located at point (x,y)
# Option name	    Option meaning
# fill	            text color
# font	            text font
# justify	        text justification: LEFT (default), CENTER, RIGHT
# text	            text to display (\n works as expected)
# width	            normally, the rectangle is as wide as the longest text line; using the width option forces the text to be aligned to that size
canvas.create_text(300, 200, text="Mary\nhad\na\nlittle\nlamb",
                   font=("Arial","40","bold"),
                   justify=tk.CENTER,
                   fill='white')

image = tk.PhotoImage(file='logo2.png')
canvas.create_image(175, 500, image=image)

jpg = Image.open('logo3.jpg')
image2 = ImageTk.PhotoImage(jpg)
canvas.create_image(500, 500, image=image2)

button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# -  Coordinates in methods like create_rectangle(), create_oval(), create_line(), and create_polygon() are always based on the canvas's top-left origin (0, 0).

# Property name	    Property role
# borderwidth	    canvas border’s width in pixels (default: 2)
# background (bg)	canvas border’s color (default: the same as the underlying window’s color)
# height	        canvas height (in pixels)
# width	            canvas width (in pixels)

# The most interesting create_line() options are as follows:
# Option name	Option meaning
# arrow	        normally, the chain ends aren’t marked in any special way, but you may want them to be finished with arrowheads; setting the arrow option to FIRST results in drawing an arrowhead at the chain’s beginning, LAST at the chain’s end, BOTH at both sides of the chain.
# fill	        chain color (setting the option to an empty string causes the line to be transparent)
# smooth	    setting it to True rounds the chain’s corners using a set of connected parabolas
# width	        line width (default: 1 pixel)