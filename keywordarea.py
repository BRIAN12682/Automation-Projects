# Define a function to calculate the area of a rectangle
def calculate_area(**kwargs):
    length = kwargs.get('length', 0)
    width = kwargs.get('width', 0)
    height = kwargs.get('height', 1)
    return length * width * height 

# Get user input for length and width
length = float(input("Enter length: "))
width = float(input("Enter width: "))
height= input("Enter height: ")
# Calculate the area of the rectangle
area = calculate_area(length=length, width=width)

# Print the area of the rectangle to the console
print("The area of the rectangle is:", area)
