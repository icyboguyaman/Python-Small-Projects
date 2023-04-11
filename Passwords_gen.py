import random
import string

def generate_password(length):
    """Generate a random alphanumeric password of given length"""
    # Define the set of characters to use
    characters = string.ascii_letters + string.digits
    
    # Use random.choices() to generate a list of random characters
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Generate a random alphanumeric password of length 10
password = generate_password(10)

# Print the password
print(password)
