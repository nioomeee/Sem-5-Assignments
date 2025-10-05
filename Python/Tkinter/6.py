import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def showColor(color_name):
    messagebox.showinfo("Color clicked!", f"You clicked {color_name} button")

root = tk.Tk()
root.title("Colors")
root.geometry("300x500")

# list of tuples for buttons (text, bgcolor, text color)
colors_data = [
    ("RED", "#b60000", "white"),
    ("YELLOW", "#dad417", "black"),
    ("PINK", "#d42e95", "black"),
    ("GREEN", "#51c70d", "black"),
    ("PURPLE", "#7d019c", "white"),
    ("ORANGE", "#ff9100", "black"),
    ("BLUE", "#0015d6", "white")
]

button_font = ("Segoe UI", 14, "bold")

for text, bgcolor, fgcolor in colors_data:
    command_with_argument = lambda color_name=text: showColor(color_name)

    button = tk.Button(root, text=text, bg=bgcolor, fg=fgcolor, font=button_font, command=command_with_argument)

    button.pack(fill="x", pady=10, padx=20)


root.mainloop()