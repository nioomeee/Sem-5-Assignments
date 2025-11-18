import tkinter as tk

# 1. setup canvas

canvas = tk.Canvas(root, width = 600, height = 400) # root = window
canvas.pack() # stuffing the canvas onto the window

# 2. Create rectangle
canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="") # x1 and y1 are the coordinates of top left corner, 
# x2 and y2 are coordinates of bootom right corner

# 3. Polygon
canvas.create_polygon(x1, y1, x2, y2, x3, y3, ..., fill="#000000")
# Connect the dots of the listed coordinates

# 4. Oval
canvas.create_oval(x1, y1, x2, y2, fill="#0f0f0f", outline="")
# Similar to rectangle, will create an oval in the given rectangle

# 5. Arc
canvas.create_arc(x1, y1, x2, y2, start = Angle, extent = Angle, style = tk.ARC)
# x1 y1 x2 y2: Bounding box for the full circle
# start: where to start cutting(0 -> East/Right, 90 -> North/Top)
# extent: how big the slice is (in degrees)
# style = tk.ARC : Draws the curved line

# 6. Line
canvas.create_line(x1, y1, x2, y2, options)
# x1, y1: Starting point of line
# x2, y2: Ending point of line
# width=Integer: Thickness of line
# arrow = tk.LAST: puts an arrowhead at the end
# dash= (4, 4): makes a dashed line (4 pixels line, 4 pixels gap)
# fill = "#000000": color of the line

# 7. Text
canvas.create_text(x, y, text="String", options)
# x, y: Exact center of the string
# font = ("Arial", 20 "bold"): control the look
# fill = "color": Text color

# 8. Clear everything
canvas.delete("all")

# 9. Delete specific
my_ball = canvas.create_oval()
canvas.delete(my_ball)

