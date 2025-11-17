# Take 10 numbers from the user. Use `continue` to skip numbers divisible
# by both 3 and 5. Use `break` if number is negative. If loop completes, 
# use`else` to print “Input complete”.

print("Enter 10 numbers (Negative numbers stop the loop)")

try:
    
    for i in range(10):
        num = int(input(f"Enter num {i+1}: "))

        if num < 0:
            print(f"Exiting loop ({num} is negative)")
            break
        elif num % 15 == 0:
            print(f"Skipping {num} (divisible by 3 and 5)")
            continue;
        else:
            print(f"Processing {num}...")

    else:
        print("Input complete")
except ValueError:
    print("Invalid input!")