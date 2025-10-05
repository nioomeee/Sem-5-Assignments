import tkinter as tk

root = tk.Tk()
root.title("House Scene Drawing")
root.geometry("600x500")

# Create canvas
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack()

# draw sky which is big blue rectangle which is from (0,0) to (600, 350)
canvas.create_rectangle(0, 0, 600, 350, fill="#2986b4", outline="")

# Draw the grass: Big green rectangle starting from where sky ended
canvas.create_rectangle(0, 350, 600, 600, fill="#61d02e", outline="")

# House body: beige rectangle
canvas.create_rectangle(200, 200, 350, 400, fill="#ccc074", outline="")

# roof of house: Brown triangle using create_polygon
# we give 3 corner points 
canvas.create_polygon(170, 200, 380 ,200, 275, 100, fill="#704e17", outline="")

# Sun using create_oval. For it we have to make an invisible box a square
canvas.create_oval(50, 50, 120, 120, fill="#ffff00", outline="")

# Cloud: basically 3 overlapping white ovals
canvas.create_oval(400, 80, 480, 140, fill="#ffffff", outline="")
canvas.create_oval(450, 80, 530, 140, fill="#ffffff", outline="")
canvas.create_oval(420, 60, 500, 120, fill="#ffffff", outline="")

# Door: Simple brown rectangle
canvas.create_rectangle(250, 300, 300, 400, fill="#704e17", outline="")


root.mainloop()