# Create a Python program that displays following output:
# When user clicks on any Checkbutton its value must be displayed in label.
# Note: Display multiple values when more than one Checkbutton is selected.
import tkinter as tk
from tkinter import ttk

def update_selection():
    selected_foods = []

    if bananas_var.get() == 1:
        selected_foods.append("Bananas")
    if chicken_var.get() == 1:
        selected_foods.append("Chicken")
    if stuffed_var.get() == 1:
        selected_foods.append("Stuffed Peppers")

    if selected_foods:
        result_text = "You chose: " + ", ".join(selected_foods)
    else:
        result_text = "You haven't selected any food yet"

    result_label.config(text=result_text)

root = tk.Tk()
root.title("Favourite food")
root.geometry("500x200")
root.configure(bg="#ebd17a")

# Variables
bananas_var = tk.IntVar()
chicken_var = tk.IntVar()
stuffed_var = tk.IntVar()

# Styles
style=ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12), background=root.cget('bg'))

title_label = ttk.Label(root, text="Choose your favourite food", style="TLabel", background=root.cget('bg'))
title_label.pack(pady=10)

# Frame for checkboxes
check_frame=ttk.Frame(root)
check_frame.pack(pady=5)

ttk.Checkbutton(check_frame, text="Bananas", variable=bananas_var, command=update_selection).pack(anchor="w", padx=20)
ttk.Checkbutton(check_frame, text="Chicken", variable=chicken_var, command=update_selection).pack(anchor="w", padx=20)
ttk.Checkbutton(check_frame, text="Stuffed Peppers", variable=stuffed_var, command=update_selection).pack(anchor="w", padx=20)

result_label=ttk.Label(root, text="You haven't selected any food yet", style="TLabel", background=root.cget('bg'))
result_label.pack(pady=20)


root.mainloop()