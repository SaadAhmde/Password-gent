import random
import string

def generate_password(length):
    # All possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example: generate a password of length 12
password = generate_password(11)
print("Generated Password:", password)
