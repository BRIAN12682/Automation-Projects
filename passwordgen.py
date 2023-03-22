import random
import string

def generate_password(length):
    # Define the character set for the password
    chars = string.ascii_letters + string.digits

    # Generate a random password of the specified length
     
    password = ''.join(random.choice(chars) for i in range(length))

    # Return the password
    return password

# Get user input for password length
length = int(input("Enter password length: "))

# Generate the password
password = generate_password(length)

# Print the password to the console
print("Your password is:", password)
