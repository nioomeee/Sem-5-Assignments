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
    result_text = (f" Name: {student_name}\n Gender: {gender}\n Year: {year}\n Hobbies {', '.join(hobbies)}")

    # displaying the organized text on the result screen
    result_label.config(text=result_text)

# main window setup
root = tk.Tk() # creating main window object
root.title("Student Details Form") # title of our window
root.geometry("450x550")
root.config(bg="#e1d8b2")

# Style definitions
label_font = ("Roboto", 11)
button_style = ttk.Style()
button_style.configure("TButton", font = ("Roboto", 12, "bold"), padding = 10)


# tkinter variables
gender_var = tk.StringVar(value="Not Specified") #spot to store TEXT
hobby1_var = tk.IntVar() # spot to store number 0 or 1
hobby2_var = tk.IntVar() 

# Name 
ttk.Label(root, text="Name: ", font = label_font, background=root.cget('bg')).pack(pady=(20, 5))
name_entry = ttk.Entry(root, width=40, font = label_font)
name_entry.pack(pady=5, padx=20)

# radio buttons for gender
gender_frame = ttk.Frame(root)
gender_frame.pack(pady=10)
ttk.Label(gender_frame, text="Gender: ", font=label_font).pack(side=tk.LEFT, pady=5)
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side=tk.LEFT, padx=5)
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value = "Female").pack(side=tk.LEFT, padx=5)

# listbox for year
ttk.Label(root, text="Select Year: ", font=label_font, background=root.cget('bg')).pack(pady=5)
year_listbox = tk.Listbox(root, height=3, font=label_font, bg="#ffffff", selectbackground="#090b91") #height = 3 shows 3 items
year_listbox.insert(1, "FY")
year_listbox.insert(2, "SY")
year_listbox.insert(3, "TY")
year_listbox.pack(pady=5, padx=20)

# checkboxes button for hobbies
ttk.Label(root, text = "Hobbies: ", font=label_font, background=root.cget('bg')).pack(pady=5)
ttk.Checkbutton(root, text="Reading", variable=hobby1_var).pack()
ttk.Checkbutton(root, text="Swimming", variable=hobby2_var).pack()

# Submit button - we link this to function called submit_details
submit_button = ttk.Button(root, text="Submit", command=submit_details, style="TButton")
submit_button.pack(pady=30)

# Little screen at the bottom to show final result
result_label = ttk.Label(root, text = "", justify=tk.LEFT, font=label_font, background=root.cget('bg'))
result_label.pack(pady=10, padx=20)


root.mainloop() # this line should be the last. Tells the window to open and stay open