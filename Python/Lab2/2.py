# Print the following hollow triangle pattern using nested `for` loops:
#    *
#   * *
#  *   *
# *     *
#  ******

height = int(input("Enter the height of the pyramid(number of rows): "))

if height <= 0:
    print("Please enter a positive number.")
else:
    for i in range(height):
        curr_row = i+1

        for _ in range(height-curr_row):
            print(" ", end="")

        width = (2 * curr_row) - 1

        for j in range(width):
            if j == 0 or j == width -1 or curr_row == height:
                print("*", end = "")
            else:
                print(" ", end = "")

        print()
