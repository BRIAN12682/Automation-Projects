import random
import string

def generate_password(length):
    chars = string.ascii_letters 
    # + string.digits
    password = ''.join(random.choice(chars) for i in range(length))
    return password
    
length = int(input("Enter password length: "))
password = generate_password(length)
print("Your password is:", password)
