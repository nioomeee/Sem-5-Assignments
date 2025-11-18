import tkinter as tk

def show_greeting():
    user_name = entry.get()
    if user_name == "":
        result_label.config(text="Hey! You didn't type a name.", fg = "red")
    else:
        result_label.config(text=f"Hey {user_name}.", fg = "green")

        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Greeter")
root.geometry("300x400")

tk.Label(root, text = "Enter your name: ", font = ("Arial", 12, "bold")).pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text = "Enter", font = ("Arial", 14, "bold"), command = show_greeting).pack(pady = 10)

result_label = tk.Label(root, text = "Waiting...", font = ("Arial", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()