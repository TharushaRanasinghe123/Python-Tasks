import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    char_pool = list(string.ascii_lowercase)
    password = []

    if use_upper:
        char_pool += list(string.ascii_uppercase)
        password.append(random.choice(string.ascii_uppercase))
    
    if use_digits:
        char_pool += list(string.digits)
        password.append(random.choice(string.digits))
    
    if use_special:
        char_pool += list(string.punctuation)
        password.append(random.choice(string.punctuation))

    # Ensure the rest of the password is filled
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle to prevent predictable pattern
    random.shuffle(password)
    return ''.join(password)

# --- User input for customization ---
try:
    length = int(input("Enter desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_special)
    if password:
        print("Generated password:", password)
except ValueError:
    print("Invalid input! Please enter a number for password length.")
