import tkinter as tk

root = tk.Tk()
root.title("Traffic Signal")
root.geometry("500x800")
root.config(bg="#A9A7A7")

canvas = tk.Canvas(width=500, height=800)
canvas.pack()

# drawing the background for traffic lights
canvas.create_rectangle(200, 50, 450, 700, fill="#2f2f2f", outline="")

# red light which is off rn
canvas.create_oval(225, 75, 425, 250, fill="#4A0000", outline="")

# yellow light off rn
canvas.create_oval(225, 275, 425, 450, fill="#5D5D00", outline="")

# green light off rn
canvas.create_oval(225, 475, 425, 650, fill="#007200", outline="")

# post to hold the signal
canvas.create_rectangle(400, 700, 450, 800, fill="#1E1D1D", outline="")

root.mainloop()