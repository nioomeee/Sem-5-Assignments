# Write a program to manage a contact book using dictionary. Allow user to
# add, update, delete, and search contacts using menu-driven approach.
contact_book = {}
def display():
    """Prints menu options"""
    print("\n--- Contact Book Menu ---")
    print("1. Add new contact")
    print("2. Update existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit")
    print("-" * 20)

while True:
    display()
    choice = int(input("Enter your choice(1-6): "))

    match choice:
        case 1:
            name = input("Enter the name: ")
            if name in contact_book:
                print(f"Contact {name} already exists")
            else:
                phone = input("Enter phone number: ")
                contact_book[name] = phone
                print(f"Contact {name} added successfully")

        case 2:
            name = input("Enter the name of the contact you wanna update: ").title()
            if name in contact_book:
                phone = input("Enter the new phone number: ")
                contact_book[name] = phone
            else:
                print(f"Contact {name} not found")

        case 3:
            name = input("Enter a name: ").title()
            if name in contact_book:
                del contact_book[name]
                print(f"Contact {name} deleted successfully")            
            else:
                print(f"Contact {name} not found")

        case 4:
            name = input("Enter a name: ").title()
            if name in contact_book:
                print("Search result: ")
                print(f"Name: {name}")
                print(f"Contact number: {contact_book[name]}")
                print("-" * 15)

        case 5:
            print("--- All Contacts ---")
            if not contact_book:
                print("The contact book is empty")
            else:
                for name, phone in contact_book.items():
                    print(f"Name: {name}, Phone: {phone}")
                print("-" * 10)

        case 6:
            print("Goodbye!")
            print("-" * 10)
            break

        case _:
            print("Enter valid choice")