# Create a Python program that displays following output & perform necessary operations:

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def Addition():
    try:
        num1 = float(num1_var.get())
        num2 = float(num2_var.get())

        result = num1 + num2
        result_var.set(f"{result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")


root=tk.Tk()
root.title("Addition")
root.config(bg="#9c9c9c")
root.geometry("300x300")
root.resizable(False, False)

# Style Configurations
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12), background="#9c9c9c", foreground="#ffffff")
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("Quit.TButton", font=("Segoe UI", 12, "bold"))
style.configure("Submit.TButton", font=("Segoe UI", 12, "bold"))


# main frame and usong grid()
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)

# Row 0
ttk.Label(main_frame, text="Enter Num 1: ").grid(row=0, column=0, padx=10, pady=10, sticky="w")
num1_var = ttk.Entry(main_frame, width=20)
num1_var.grid(row=0, column=1, padx=10, pady=10)

# Row1
ttk.Label(main_frame, text="Enter Num 2: ").grid(row=1, column=0, padx=10, pady=10, sticky="w")
num2_var=ttk.Entry(main_frame, width=20)
num2_var.grid(row=1, column=1, padx=10, pady=10)

result_var=tk.StringVar()
# Row 2
ttk.Label(main_frame, text="The Sum is: ").grid(row=2, column=0, padx=10, pady=10, sticky="w")
result_entry = ttk.Entry(main_frame, width=20, textvariable=result_var, state="readonly")
result_entry.grid(row=2, column=1, padx=10, pady=10)

# Row 3 - buttons
quit_button = ttk.Button(main_frame, text="Quit", command=root.destroy, style="Quit.TButton")
quit_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

show_button=ttk.Button(main_frame, text="Show", command=Addition, style="Submit.TButton")
show_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")



root.mainloop()