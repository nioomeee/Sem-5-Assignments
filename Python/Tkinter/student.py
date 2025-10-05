import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_details():
    student_name = name_entry.get() # reads name from the widget screen

    hobbies = []
    if hobby1_var.get() == 1:
        hobbies.append("Reading")
    if hobby2_var.get() == 1:
        hobbies.append("Swimming")

    gender = gender_var.get()

    # if no hobbies are selected 
    if not hobbies:
        messagebox.showerror("Validation error", "Please select atleast 1 hobby")
        return
    
    year_selection = year_listbox.curselection()
    year = year_listbox.get(year_selection) if year_selection else "Not Selected"
    
    # gathering all the collected information and writing it down in a sentence
    result_text = (f"Name: {student_name}\n Gender: {gender}\n Year: {year}\n Hobbies {', '.join(hobbies)}")

    # displaying the organized text on the result screen
    result_label.config(text=result_text)

# main window setup
root = tk.Tk() # creating main window object
root.title("Student Details Form") # title of our window
root.geometry("400x500")

# tkinter variables
gender_var = tk.StringVar(value="Not Specified") #spot to store TEXT
hobby1_var = tk.IntVar() # spot to store number 0 or 1
hobby2_var = tk.IntVar() 

# Name 
tk.Label(root, text="Name: ").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# radio buttons for gender
tk.Label(root, text="Gender: ").pack(pady=5)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value = "Female").pack()

# listbox for year
tk.Label(root, text="Select Year: ").pack(pady=5)
year_listbox = tk.Listbox(root, height=3) #height = 3 shows 3 items
year_listbox.insert(1, "FY")
year_listbox.insert(2, "SY")
year_listbox.insert(3, "TY")
year_listbox.pack()

# checkboxes button for hobbies
tk.Label(root, text = "Hobbies: ").pack(pady=5)
tk.Checkbutton(root, text="Reading", variable=hobby1_var).pack()
tk.Checkbutton(root, text="Swimming", variable=hobby2_var).pack()

# Submit button - we link this to function called submit_details
submit_button = tk.Button(root, text="Submit", command=submit_details)
submit_button.pack(pady=20)

# Little screen at the bottom to show final result
result_label = tk.Label(root, text = "", justify=tk.LEFT)
result_label.pack()


root.mainloop() # this line should be the last. Tells the window to open and stay open