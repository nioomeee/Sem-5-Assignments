# Choice selector - using radio buttons as well as check buttons

import tkinter as tk

def show_order():
    size = size_var.get()

    total = size

    toppings = []

    if cheese_var.get() == 1:
        toppings.append("Extra cheese (+$2)")
        total += 2
    
    if pepp_var.get() == 1:
        toppings.append("Extra pepperoni (+$3)")
        total += 3

    toppings_str = "\n - " . join(toppings) if toppings else " - None"

    output = (
        f"Base Price = ${size}\n"
        f"Extra Toppings = \n{toppings_str}\n"
        "--------------------------------\n"
        f"TOTAL = ${total}"
    )

    result_label.config(text = output, fg = "darkblue")

root = tk.Tk()
root.title("Pizza Selection")
root.geometry("300x400")

# Variables
size_var = tk.IntVar()
cheese_var = tk.IntVar()
pepp_var = tk.IntVar()

# Size label
tk.Label(root, text = "Select size:", font = ("Arial", 12)).grid(row = 0, column = 0, columnspan = 2, pady = 5)

# size radio buttons
tk.Radiobutton(root, text = "Small ($10)", value = 10, variable = size_var).grid(row = 1, column = 0, sticky="w", padx = 10)
tk.Radiobutton(root, text = "Large ($20)", value = 20, variable = size_var).grid(row = 1, column = 1, padx =10, sticky = "w")

# Toppings label
tk.Label(root, text = "Select toppings:", font = ("Arial", 12)).grid(row=2, column = 0, columnspan = 2, pady = 5)

# Toppings checkbuttons
tk.Checkbutton(root, text = "Cheese (+$2)", variable = cheese_var).grid(row = 3, column = 0, padx = 10, sticky = "w")
tk.Checkbutton(root, text = "Pepperoni (+$3)", variable = pepp_var).grid(row = 3, column = 1, padx = 10, sticky = "w")

# Submit button
tk.Button(root, text = "Show order", bg="#91E35E", command = show_order).grid(row = 4, column = 0, columnspan = 2, pady = 5)

# Result label
result_label = tk.Label(root, text = "Order details...", justify = tk.LEFT)
result_label.grid(row = 5, column = 0, columnspan = 2, pady = 10)

root.mainloop()
    
