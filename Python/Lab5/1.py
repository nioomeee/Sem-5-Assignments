# Create a Python program that allows users to maintain a personal expense tracker. 
# Implementclasses for Expense and ExpenseManager with methods to add, delete, and 
# view expenses.Handle exceptions for invalid inputs, and store all expenses in a CSV file.

import csv
import os

# blueprint for single expense
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

# Expense Manager
class ExpenseManager:
    def __init__(self, filename = "expenses.csv"):
        self.filename = filename
        self.expenses = [] # epmty list initialized for expenses
        self.loadExpenses()

    def addExpense(self, expense):
        self.expenses.append(expense)
        print("\n ----- Expense added successfully -----")

    def viewExpense(self):
        if not self.expenses:
            print("\n No expenses yet")
            return

        print("\n ----- Your expenses are: -----")
        total = 0
        for i, expense in enumerate(self.expenses, start=1):
            print(f"\n {i}. Description : {expense.description}, Amount: {expense.amount:.2f}")
            total += expense.amount
        print("\n ----------")

        print(f"\n Total expense = {total:.2f}")


    def delExpense(self, index):
        try:
            idx = int(index) - 1

            if 0 <= idx < len(self.expenses):
                removed = self.expenses.pop(idx)
                print(f"\n Deleted expense {removed.description}")
                
            else:
                print("\n Error invalid number, please choose a valid number")

        except ValueError:
            print(f"\n An error occured")

    def loadExpenses(self):
        if not os.path.exists(self.filename):
            return
            
        try:
            with open(self.filename, mode="r", newline = '') as f:
                reader = csv.reader(f)
                next(reader)
                for description, amount_str in reader:
                    expense = Expense(description, float(amount_str))
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass

    def saveExpenses(self):
        with open(self.filename, mode="w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Amount"])

            for expense in self.expenses:
                writer.writerow([expense.description, expense.amount])
            print("\n All expenses have been saved")


def main():
    manager = ExpenseManager()

    while True:
        print("\n ----- Expense Tracker Menu -----")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                description = input("Enter expense description: ")
                amount = float(input("Enter expense amount: "))

                expense = Expense(description, amount)
                manager.addExpense(expense)

            except ValueError:
                print("\n Enter valid amount")

        elif choice == '2':
            manager.viewExpense()
        
        elif choice == '3':
            manager.viewExpense()
            if manager.expenses:
                index = input ("Enter the number of index you wanna delete: ")
                manager.delExpense(index)

        elif choice == '4':
            manager.saveExpenses()
            print("\n Goodbye")
            break

        else:
            print("\n Invalid choice. Enter proper number")

if __name__ == "__main__":
    main()