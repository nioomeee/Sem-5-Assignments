# Create a Python program that displays following output. 
# Create Listbox, whenever user
# selects any option its value is printed on the label.

import tkinter as tk

def displayDetails(event):
    selection_indices = lang_listbox.curselection()

    if selection_indices:
        index = selection_indices[0]
        lang = lang_listbox.get(index)
        result_label.config(text=lang)


root = tk.Tk()
root.title("ListBox")
root.geometry("300x350")
root.config(bg="#868686")


# Listbox
tk.Label(root, text="ListBox", font=("Segoe UI", 12, "bold")).pack(ipady=10, fill="x")
lang_listbox = tk.Listbox(root, height=5, font=("Segoe UI", 12), foreground="#000000", background="#ffffff", selectbackground="#868686")
lang_listbox.insert(tk.END, "PHP")
lang_listbox.insert(tk.END, "ROR")
lang_listbox.insert(tk.END, "PYTHON")
lang_listbox.insert(tk.END, "ANDROID")
lang_listbox.insert(tk.END, "IOS")

lang_listbox.pack(padx=20, pady=10, fill="both", expand=True)
lang_listbox.bind("<<ListboxSelect>>", displayDetails)

result_label = tk.Label(root, text="No selection yet", font=("Segoe UI", 12, "bold"))
result_label.pack(pady=20, fill="x")

root.mainloop()