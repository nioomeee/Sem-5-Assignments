# Create a Python program that displays following output:
# When user clicks on any Radiobutton its value must be displayed in label.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# function
def language_selected():
    selection = language_var.get()
    result_label.config(text=f"Your selection = {selection}")

# main window
root = tk.Tk()
root.title("Programming language")
root.geometry("400x250")
root.configure(bg="#FFFF63")

languages = ["Python", "Perl", "Java", "C++", "C"]
language_var = tk.StringVar(value=languages[0]) # single StringVar will link all radio buttons together

title_label = ttk.Label(root, text="Choose your favourite programming language", font=("Segoe UI", 12))
title_label.pack(pady=10)

# frame to hold radio buttons
radio_frame = ttk.Frame(root)
radio_frame.pack(pady=5)

for lang in languages:
    rb = ttk.Radiobutton(radio_frame, text=lang, variable=language_var, value=lang, command=language_selected)
    rb.pack(anchor="w", padx=20)

result_label = ttk.Label(root, text="", font=("Segoe UI", 12, "bold"))
result_label.pack(pady=20)

language_selected()


root.mainloop()