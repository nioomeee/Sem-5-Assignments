import tkinter as tk

root = tk.Tk()
root.title("1st App")
root.geometry("300x450")

my_label = tk.Label(root, text = "This is a label", font = ("Arial", 12, "bold"))

my_label.pack()

root.mainloop()