## write a  python program to print all positive numbers in a range.
def print_positive_numbers(start, end):
    for num in range(start, end + 1):
        if num > 0:
            print(num)


# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Print all positive numbers in the range
print("Positive numbers in the range", start, "to", end, ":")
print_positive_numbers(start, end)
