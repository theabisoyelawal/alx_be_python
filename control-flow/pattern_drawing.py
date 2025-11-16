# pattern_drawing.py

# Prompt the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Initialize row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Stay on the same line
    print()  # Move to the next line after printing a row
    row += 1
