import getpass

username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")
print("Greetings,", username, "you are now logged in with a password.")

command = input("Please type a command: ")
if command == "log off":
    print("You have now been logged off again,", username)
    old_username = username
    old_password = password
    username = ""
    password = ""

username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")

while username != old_username or password != old_password:
    print("Sorry, username and/or password incorrect. Please re-enter for validation.")
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")

print("Greetings,", username, "you are now logged in with your password.")
