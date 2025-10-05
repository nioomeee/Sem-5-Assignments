# Create a Python program that have two Radiobutton having value as:
# Your Age:
# ● Less than 18
# ● Greater than 18
# When user selects any of the Radiobutton display proper message in label.
# Note: If user selects Less than 18 than it should give message “You are not eligible for
# voting” and if user selects Greater than 18 than it should give message “ You are eligible
# for voting”.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def eligible():
    age_choice=age_var.get()

    if age_choice == "less":
        message = "You are not eligible for voting"
    else:
        message = "You are eligible for voting"
    
    messagebox.showinfo("Eligibility Result: ", message)

root = tk.Tk()
root.title("Age Selector")
root.geometry("200x200")
root.configure(bg="#f1a3a3")

age_var = tk.StringVar(value="less")

style=ttk.Style()

style.configure("TLabel", font=("Segoe UI", 12), background=root.cget('bg'))

title_label = ttk.Label(root, text="Your Age:", style="TLabel")
title_label.pack(pady=10)

# frame for radio buttons
radio_frame = ttk.Frame(root)
radio_frame.pack(pady=5)

# radio buttons now
ttk.Radiobutton(radio_frame, text="Less than 18", variable=age_var, value="less", command=eligible).pack(anchor="w")
ttk.Radiobutton(radio_frame, text="Greater than 18", variable=age_var, value="greater", command=eligible).pack(anchor="w")

root.mainloop()