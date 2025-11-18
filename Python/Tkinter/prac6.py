# Zone selection using listbox

import tkinter as tk

def show_zone(event):
    selection = zone_selection.curselection()
    if selection:
        index = selection[0]
        zone = zone_selection.get(index)
    
    result_label.config(text = f"Delivering to: {zone}", fg = "purple")

root = tk.Tk()
root.title("Zone Selection")
root.geometry("300x200")

# Label for Zone selection
tk.Label(root, text = "Select your zone:", font = ("Arial", 12, "bold")).pack(pady = 5)

# Listbox for zone selection
zone_selection = tk.Listbox(root, height = 3)
zone_selection.insert(1, "Zone A - Downtown")
zone_selection.insert(2, "Zone B - Suburbs")
zone_selection.insert(3, "Zone C - University")
zone_selection.pack(pady = 5)

# Binding
zone_selection.bind('<<ListboxSelect>>', show_zone)

# Result label
result_label = tk.Label(root, text = "Please select your zone", fg = "gray")
result_label.pack(pady = 10)

root.mainloop()