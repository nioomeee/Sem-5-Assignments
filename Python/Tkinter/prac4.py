# Login form

import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("400x500")

# label for username (0, 0)
tk.Label(root, text= "User name:").grid(row=0, column=0, padx = 10, pady = 10)

# username entry (0,1)
username = tk.Entry(root)
username.grid(row = 0, column = 1, padx = 10, pady = 10)

# Password label (1, 0)
tk.Label(root, text = "Password:").grid(row = 1, column = 0, padx = 10, pady = 10)

# password entry (1, 1)
password = tk.Entry(root, show="*")
password.grid(row = 1, column = 1, padx = 10, pady = 10)

# submit button(2, 0) columnspan = 2
login = tk.Button(root, text = "Submit", bg = "Orange")
login.grid(row=2, column = 0, columnspan = 2, pady = 20)

root.mainloop()