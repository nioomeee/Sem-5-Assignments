import tkinter as tk

root = tk.Tk()
root.title("Smiling Face")
root.geometry("500x500")

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

# yellow circle
canvas.create_oval(50, 50, 450, 450, fill="#ffff00", outline="")

# black eyes
canvas.create_oval(150, 150, 200, 200, fill="#000000", outline="")
canvas.create_oval(300, 150, 350, 200, fill="#000000", outline="")

# smile line using create_arc
canvas.create_arc(120, 150, 380, 380, start=210, extent=120, style=tk.ARC, outline="#000000", width=5)


root.mainloop()