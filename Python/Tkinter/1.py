# Create a Python program which have following widgets:
# • Button
# • MessageBox
# • When user clicks on Button, MessageBox is display with some message.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        result = num1 + num2

        result_var.set(f"{result:.2f}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("Addition")
root.geometry("350x250")
root.resizable(False, False)
root.config(bg="#8A6B2D")

# Style configs
style = ttk.Style()
style.theme_use("clam")

# style for labels
style.configure("TLabel", background="#2e2e2e", foreground="#ffffff", font=("Segoe UI", 12))

# style for entry boxes
style.configure("TEntry", font=("Segoe UI", 12))

# Sp. style for Quit Button
style.configure("Quit.TButton", font=("Segoe UI", 12, "bold"), foreground="#C50000")

# sp style for submit button
style.configure("Submit.TButton", font=("Segoe UI", 12, "bold"), foreground="#2333c5")

result_var = tk.StringVar()

# creating and placing widgets using grid()
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)

# Row 0
ttk.Label(main_frame, text="Enter num 1: ").grid(row=0, column=0, padx=10, pady=10, sticky="w")
num1_entry = ttk.Entry(main_frame, width=20)
num1_entry.grid(row=0, column=1, padx=10, pady=10)

# Row 1
ttk.Label(main_frame, text="Enter num 2: ").grid(row=1, column=0, padx=10, pady=10, sticky="w")
num2_entry = ttk.Entry(main_frame, width=20)
num2_entry.grid(row=1, column=1, padx=10, pady=10)

# Row 2
ttk.Label(main_frame, text="The Sum is: ").grid(row=2, column=0, padx=10, pady=10, sticky="w")
result_entry =ttk.Entry(main_frame, textvariable=result_var, width=20, state="readonly")
result_entry.grid(row=2, column=1, padx=10, pady=10)

# Row 3 - button frame
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=3, column=0, columnspan=2, pady=20)

show_button = ttk.Button(button_frame, text="Show Sum", command=calculate_sum, style="Submit.TButton")
show_button.pack(side="left", padx=10)

quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy, style="Quit.TButton")
quit_button.pack(side="left", padx = 20)

root.mainloop()