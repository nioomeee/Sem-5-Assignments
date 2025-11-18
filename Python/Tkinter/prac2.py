import tkinter as tk

count = 0

def click_me():
    global count
    count += 1

    display_label.config(text = f"You clicked: {count} times")

    print(f"Consle log: Clicked: {count}")

root = tk.Tk()
root.title("Count Clicker")
root.geometry("300x400")

display_label = tk.Label(root, text = "You clicked 0 times", font = ("Arial", 14, "bold"))
display_label.pack(pady = 20)

action_button = tk.Button(root, text="Click me", command = click_me, bg="lightblue")
action_button.pack()

root.mainloop()