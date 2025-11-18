# Scrollbars and multi-line text
import tkinter as tk

root = tk.Tk()
root.title("Multi-line text with scrollbar")
root.geometry("400x300")

# Scrollbar
scrollbar = tk.Scrollbar(root)

# Multi-line text
text = tk.Text(root, wrap = tk.WORD, yscrollcommand=scrollbar.set)

# Binding
text.grid(row = 0, column = 0, sticky = "nsew")

scrollbar.grid(row = 0, column = 1, sticky = "ns")

scrollbar.config(command=text.yview)

long_text = "This is the first line.\n"

for i in range (2, 50):
    long_text += f"Processing file {i}: Status OK.\n"

text.insert(tk.END, long_text)

root.mainloop()