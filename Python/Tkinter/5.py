# Create a Python program that displays following output:
# When user clicks on any of the Radiobutton then show its value in the label and when
# user clicks on Quit button than window is closed.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def showSelection():
    selection = gender_var.get()
    messagebox.showinfo("Selection", f"You selected: {selection}")

root = tk.Tk()
root.title("Gender")
root.geometry("200x200")
root.config(bg="#B3B2B2")

style=ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12), background=root.cget('bg'))
style.configure("TRadiobutton", font=("Segoe UI", 12), background=root.cget('bg'))

gender_var = tk.StringVar(value="None")

title_label = ttk.Label(root, text="Pls Select..." )
title_label.pack(pady=20)

ttk.Radiobutton(root, text="Male", value="Male", variable=gender_var).pack(anchor="w", padx=20)
ttk.Radiobutton(root, text="Female", value="Female", variable=gender_var).pack(anchor="w", padx=20)

button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

showButton = ttk.Button(button_frame, text="Show", command=showSelection)
showButton.pack(side="left", padx=10)

quitButton = ttk.Button(button_frame, text="Quit", command=root.destroy)
quitButton.pack(side="left", padx=10)


root.mainloop()