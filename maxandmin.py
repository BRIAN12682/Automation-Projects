def find_min_max(numbers):
    # Initialize min and max to the first number in the list
    min_num = numbers[0]
    max_num = numbers[0]

    # Loop through the list and update min and max if necessary
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    # Return the min and max as a tuple
    return (min_num, max_num)

# Get user input for a list of numbers
numbers = input("Enter a list of numbers, separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Find the minimum and maximum numbers in the list
min_num, max_num = find_min_max(numbers)

# Print the result to the console
print("Minimum number:", min_num)
print("Maximum number:", max_num)
