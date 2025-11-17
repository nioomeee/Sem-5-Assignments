# Accept 10 integers. Remove duplicates, sort in descending order, print the
# second highest and second lowest unique value, and average of top 5 values.

print("----- Enter 10 numbers -----")

try:
    numbers = [int(input(f"Enter {i+1} number: ")) for i in range(10)]
    print(f"Original list: {numbers}")

    unique = sorted(set(numbers), reverse=True)
    print(f"Unique descending sorted list: {unique}")

    if len(unique) > 1:
        second_highest = unique[1]
        second_lowest = unique[-2]

        print(f"Second highest: {second_highest}")
        print(f"Second lowest: {second_lowest}")

    else:
        print("Not enough unique numbers")

    if unique:
        top_nums = numbers[:5]

        average = sum(top_nums) / len(top_nums)

        print(f"Average of top 5 numbers: {average}")

except ValueError:
    print("Invalid input!")