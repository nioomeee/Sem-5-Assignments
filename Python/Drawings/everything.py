# Objective: Create a 600x400 canvas and draw a scene with a Bow, an Arrow 
# flying through the air, a Target, and scenery.

# Specifications:

# Background: Blue sky (top 300px) and Green grass (bottom 100px). (Tool: Rectangle)

# The Mountain: A gray triangle in the background sitting on the grass line. (Tool: Polygon)

# The Sun: A yellow circle in the top-right corner. (Tool: Oval)

# The Target:

# Two wooden legs (thick brown lines). (Tool: Line + Width)

# A Red outer circle and a White inner circle. (Tool: Oval + Ordering)

# The Bow: A black curve on the left side. (Tool: Arc + Style)

# The Arrow Path: A straight line going from the bow to the target.

# It must be dashed. (Tool: Line + Dash)

# It must have an arrowhead at the end. (Tool: Line + Arrow)

# The Score: Text at the top center saying "PERFECT SHOT" in a large, 
# bold font. (Tool: Text + Font)

import tkinter as tk

root = tk.Tk()
root.title("Archery Range")
root.geometry("600x400")

canvas = tk.Canvas(root, width = 600, height = 400, bg="#ffffff")
canvas.pack()

# Sky
canvas.create_rectangle(0, 0, 600, 300, fill="#86D1FF", outline = "")

# Grass
canvas.create_rectangle(0, 300, 600, 400, fill = "#2A791E", outline="")

# Mountain
canvas.create_polygon(100, 300, 300, 100, 500, 300, fill = "#5E5E5E")

# Sun
canvas.create_oval(500, 0, 600, 100, fill = "#ECFF43", outline="")

# Target legs
canvas.create_line(450, 250, 450, 350, fill="#460D0D", width=10)
canvas.create_line(500, 250, 500, 350, fill = "#460D0D", width=10)

# Red outer circle
canvas.create_oval(430, 190, 520, 280, fill="red", outline="")

# white inner circle
canvas.create_oval(450, 210, 500, 260, fill="white", outline="")

# Bow for shooting
canvas.create_arc(50, 250, 80, 350, start = 270, extent = 180, style = tk.ARC, outline = "black")

# Arrow path
canvas.create_line(400, 235, 475, 235, arrow=tk.LAST, fill="black", dash=(5, 3))

# TEXT
canvas.create_text(300, 80, text="PERFECT SHOT!", font=("Arial", 24, "bold"), fill="darkblue")

root.mainloop()