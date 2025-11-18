# A simple ordering form.

# Create a window with title "Pizza Order".

# RadioButtons: "Small ($10)", "Large ($20)". (Variable: IntVar).

# CheckButtons: "Extra Cheese", "Pepperoni". (Variables: IntVar or BooleanVar).

# Button: "Calculate Cost".

# Logic: When clicked, calculate total and show it in a MessageBox.

# ListBox: Add a list of delivery zones (Zone A, Zone B). When the user selects one, update a Label to say "Delivering to [Zone Name]".

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Pizza Order")
root.geometry("350x450")

# 1. Radio buttons
tk.label(root, text = "Choose size: ", font = ("Arial", 12, "bold")).pack(pady=5)

size_var = tk.IntVar()

tk.RadioButton(root, text = "Small ($10)", variable = size_var, value = 10).pack()
tk.RadioButton(root, text = "Large ($20)", variable = size_var, value = 20).pack()

# Toppings (Checkbuttons)

tk.Label(root, text = "Extra Toppings: ", font = ("Arial", 12, "bold")).pack(pady=10)
cheese_var = tk.IntVar()
pepp_var = tk.IntVar()

tk.Checkbutton(root, text="Extra cheese (+$2)", value = 2, variable=cheese_var).pack()
tk.Checkbutton(root, text="Extra pepperoni (+$3)", value = 3, variable = pepp_var).pack()

# Button to calculate cost
tk.Button(root, text = "Calculate Cost", command = calculate_cost, bg = "lightblue").pack(pady=20)

# Delivery Zones (ListBox)
tk.Label(root, text = "Select delivery Zone: ", font = ("Arial", 12, "bold")).pack(pady=5)

zone_ListBox = tk.Listbox(root, height=3)
zone_ListBox.insert(1, "Zone A - Downtown")
zone_ListBox.insert(2, "Zone B - Suburbs")
zone_ListBox.insert(3, "Zone C - University")
zone_ListBox.pack()

zone_ListBox.bind('<<ListboxSelect>>', update_zone_label)

delivery_label = 

root.mainloop()