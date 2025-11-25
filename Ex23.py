# Write a code combine both validations into a single program

import re

def validate_pan(pan):
    """Validate Indian PAN (AAAAA9999A)."""
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    return bool(re.match(pattern, pan))

def validate_gmail(email):
    """Validate Gmail address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(pattern, email))

# Main Program
print("Select what you want to validate:")
print("1. PAN Card Number")
print("2. Gmail Address")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    pan_number = input("Enter PAN card number: ").upper()
    if validate_pan(pan_number):
        print("Valid PAN card number.")
    else:
        print("Invalid PAN card number.")

elif choice == "2":
    gmail = input("Enter Gmail address: ")
    if validate_gmail(gmail):
        print("Valid Gmail address.")
    else:
        print("Invalid Gmail address. Must end with @gmail.com")

else:
    print("Invalid choice! Please enter 1 or 2.")