# Create a dictionary with employee names and salaries. Increase salary by
# 10% if it's <50,000. Remove employees whose updated salary exceeds 1,00,000.

n = int(input("Enter the number of employees: "))
employees = {}

try:
    for i in range(n):
        name = input(f"Enter name {i+1}: ")
        salary = float(input(f"Enter salary {i+1}: "))

        employees[name] = salary

    print("-----")
    print(f"\nOriginal dictionary: {employees}")

    updated_salaries = {
        name: (salary * 1.1) if salary < 50000 else salary
        for name, salary in employees.items()
    }

    print(f"\nSalaries with 10% added: {updated_salaries}")

    final_salaries = {
        name: salary
        for name, salary in updated_salaries.items()
        if salary <= 100000
    }

    print(f"\nFinal dictionary of he salaries: {final_salaries}")

except ValueError:
    print("Invalid input!")