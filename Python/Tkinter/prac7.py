# Multiple selections from a listbox

import tkinter as tk

def show_zones(event):
    indices = zone_selection.curselection()

    selected_items = []

    for i in indices:
        item = zone_selection.get(i)
        selected_items.append(item)

    if selected_items:
        output = "Selected Zones:\n" + "\n" . join(selected_items)
        output_fg = "purple"
    else:
        output = "No zone selected"
        output_fg = "gray"

    result_label.config(text = output, fg = output_fg)

root = tk.Tk()
root.title("Multiple Zones Selection")
root.geometry("300x200")

# Label zones selection
tk.Label(root, text="Select multiple zones:", font = ("Arial", 12, "bold")).pack(pady = 5)

# listbox 
zone_selection = tk.Listbox(root, height = 5, selectmode = tk.MULTIPLE)
zone_selection.insert(1, "Zone A - University")
zone_selection.insert(2, "Zone B - Suburbs")
zone_selection.insert(3, "Zone C - Downtown")
zone_selection.insert(4, "Zone 4 - Industrial")
zone_selection.insert(5, "Zone E - Airport")

zone_selection.pack(pady = 5)

# Binding
zone_selection.bind('<<ListboxSelect>>', show_zones)

# Result Label
result_label = tk.Label(root, text = "No zone selected", fg = "gray")
result_label.pack(pady = 5)

root.mainloop()