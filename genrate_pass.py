import random
import string

def generate_random_password():
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range (12))
    entry_password.insert(0, password)

    return password

# Example usage:
random_password = generate_random_password()
print(random_password)
