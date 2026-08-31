'''
Write a program that prompts the user to enter a password repeatedly until a valid one is entered. For each
incorrect password entered, display the message “Invalid Password! Please try again:”. When the password
is entered correctly, display the message “Access Granted” and terminate the program.
Assume that the correct password is 2002.
'''

password = int(input("Enter your password: "))

while password != 2002:
    print("Invalid password: Please try again: ")
    password = int(input("Please try again: "))

print("access granted!")