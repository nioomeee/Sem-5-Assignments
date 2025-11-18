import tkinter as tk

def show_info():
    uname = username.get()
    pword = password.get()


    print(f"Username: {uname}\nPassword: {pword}")
    result_label.config(text = f"Info submitted!", fg = "blue")



root = tk.Tk()
root.title("Login Form with Frames")
root.geometry("300x300")

# creating frames
top_frame = tk.Frame(root, relief=tk.RIDGE, borderwidth=2)
top_frame.pack(pady = 10)

# Bottom frame
bottom_frame = tk.Frame(root, relief = tk.SUNKEN, borderwidth = 1)
bottom_frame.pack(pady = 10)

# Top Frame login form --------------------------

# Label for username (0, 0)
tk.Label(top_frame, text = "User Name:", font = ("Arial", 12, "bold")).grid(row = 0, column = 0, pady = 5)

# Entry for username (0, 1)
username = tk.Entry(top_frame)
username.grid(row = 0, column = 1, pady = 5)

# Label for Password (1, 0)
tk.Label(top_frame, text = "Password:", font = ("Arial", 12, "bold")).grid(row = 1, column = 0, pady = 5)

# Entry for password (1, 1)
password = tk.Entry(top_frame, show = "*")
password.grid(row = 1, column = 1, pady = 5)

# Bottom Frame --------------------------------

# Buttons 
tk.Button(bottom_frame, text = "Submit", bg = "#66C21F", command=show_info).pack(side = tk.LEFT, padx = 10)
tk.Button(bottom_frame, text = "Cancel", command = root.destroy, bg = "#FF0000").pack(side=tk.LEFT, padx = 10)

# Result label
result_label = tk.Label(bottom_frame, text = "Ready", fg = "gray")
result_label.pack(pady = 10)

root.mainloop()