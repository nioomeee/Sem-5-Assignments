# Write a Python program which will have Main Menu for selecting Elective Subjects asfollows:
# Main Menu:
# 1. Joomla
# 2. Ruby onRails
# 3. Drupal
# 4. Android
# 5. iOS
# Display proper message for every choice. Use elif to create a menu

print("\n---Elective subject Main Menu---")
print("1. Joomla")
print("2. Ruby onRails")
print("3. Drupal")
print("4. Android")
print("5. iOS")
print("-" * 15)

choice = int(input("Enter your choice(1-5): "))

if choice == 1:
    print("\n You've selected Joomla!")
elif choice == 2:
    print("\n You've selected Ruby on Rails!")
elif choice == 3:
    print("\n You've selected Drupal!")
elif choice == 4:
    print("\n You've selected Android!")
elif choice == 5:
    print("\n You've selected iOS!")
else:
    print("\n Select a valid option!")
    