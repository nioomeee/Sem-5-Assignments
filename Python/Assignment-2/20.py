# Write a program that simulates a basic bank transaction system using
# dictionary: account numbers as keys and balance as values. Allow user to
# deposit, withdraw, and check balance.

bank = {}

def deposit(account_number, amount):
    if account_number in bank:
        bank[account_number] += amount
        print(f"Deposit successful. New balance for account {account_number}: ${bank[account_number]:.2f}")
    else:
        bank[account_number] = amount
        print(f"Account {account_number} created with initial deposit of ${amount:.2f}")

def withdraw(account_number, amount):
    if account_number not in bank:
        print(f"Error: Account {account_number} does not exist.")
    elif bank[account_number] < amount:
        print(f"Error: Insufficient funds in account {account_number}.")
    else:
        bank[account_number] -= amount
        print(f"Withdrawal successful. New balance for account {account_number}: ${bank[account_number]:.2f}")

def check_balance(account_number):
    if account_number in bank:
        print(f"Current balance for account {account_number}: ${bank[account_number]:.2f}")
    else:
        print(f"Error: Account {account_number} does not exist.")

while True:
    print("\n--- Bank Transaction System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        account = input("Enter account number: ")
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                deposit(account, amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == '2':
        account = input("Enter account number: ")
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            else:
                withdraw(account, amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == '3':
        account = input("Enter account number: ")
        check_balance(account)
    elif choice == '4':
        print("Exiting bank transaction system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")