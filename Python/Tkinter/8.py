# Create a Python program that displays following output & perform necessary operations:
# Display the all the five details on label when show button is clicked.

import tkinter as tk
from tkinter import ttk

def DisplayDetails():
    fname = first_entry.get()
    lname = last_entry.get()
    design = design_entry.get()
    company = comp_entry.get()
    country = country_entry.get()

    result = f" Name = {fname} {lname}\n Designation = {design}\n Company = {company}\n Country = {country}"

    result_label.config(text=result)

root=tk.Tk()
root.title("Information")
root.geometry("550x550")
root.config(bg="#a4a3a3")

# Style configurations
style=ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12), foreground="#000000")
style.configure("TEntry", font=("Segoe UI", 12), background="#ffffff", foreground="#545454")
style.configure("TButton", font=("Segoe UI", 12, "bold"), background="#757575", foreground="#000000")

main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)

# Row 0
ttk.Label(main_frame, text="First Name ", style="TLabel").grid(row=0, column=0, padx=10, pady=10, sticky="w")

first_entry = ttk.Entry(main_frame, width=40, style="TEntry")
first_entry.grid(row=0, column=1, padx=10, pady=10)

# Row 1
ttk.Label(main_frame, text="Last Name ", style="TLabel").grid(row=1, column=0, padx=10, pady=10, sticky="w")

last_entry = ttk.Entry(main_frame, width=40, style="TEntry")
last_entry.grid(row=1, column=1, padx=10, pady=10)

# Row 2
ttk.Label(main_frame, text="Designation ", style="TLabel").grid(row=2, column=0, padx=10, pady=10, sticky="w")

design_entry = ttk.Entry(main_frame, width=40, style="TEntry")
design_entry.grid(row=2, column=1, padx=10, pady=10)

# Row 3
ttk.Label(main_frame, text="Company", style="TLabel").grid(row=3, column=0, padx=10, pady=10, sticky="w")

comp_entry = ttk.Entry(main_frame, width=40, style="TEntry")
comp_entry.grid(row=3, column=1, padx=10, pady=10)

# Row 4
ttk.Label(main_frame, text="Country", style="TLabel").grid(row=4, column=0, padx=10, pady=10, sticky="w")

country_entry = ttk.Entry(main_frame, width=40, style="TEntry")
country_entry.grid(row=4, column=1, padx=10, pady=10)

# Row 5
quit_button = ttk.Button(main_frame, text="Quit", style="TButton", command=root.destroy)
quit_button.grid(row=5, column=0, padx=10, pady=10)

show_button = ttk.Button(main_frame, text="Show", style="TButton", command=DisplayDetails)
show_button.grid(row=5, column=1, padx=10, pady=10)

# Row 6
result_label=ttk.Label(main_frame, text="", justify=tk.LEFT, wraplength=400, style="TLabel")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()