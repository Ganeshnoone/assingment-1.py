## Task 1.wite a Python program which accepts the radius of a circle from the user and computes area

import math
radius =float(input("enter the radius of the circle:"))
area=math.pi*radius**2
print("radius:",radius)
print("area:",area)

## Taksk 2. write a Python program to accept a filename from the user and print the extension of that.

def get_file_extension(filename):
    # Split the filename by the dot
    parts = filename.split(".")

    # Check if there is at least one dot in the filename
    if len(parts) > 1:
        # Return the last part (extension)
        return parts[-1]
    else:
        # No extension found
        return "No extension found"


# Prompt the user to enter a filename
filename = input("Enter a filename: ")

# Get the extension of the filename
extension = get_file_extension(filename)

# Print the extension
print("File extension:", extension)
                    
