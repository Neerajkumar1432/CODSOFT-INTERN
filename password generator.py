# Random password generator by using python

import random

def simple_password_generator():
    print("=== Simple Password Generator ===")
    
    # Ask user for password length
    length = int(input("lenght of password "))
    
    # Define possible characters
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    
    # Generate password
    password = " "
    for i in range(length):
        password += random.choice(chars)
    
    # Display the password
    print("Your new password is:", password)


simple_password_generator()    


