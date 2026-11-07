
import secrets
import string

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


length = int(input("Enter password length: "))

if length < 8:
    print("Password length must be at least 8.")
else:
    print("Generated Password:", generate_password(length))
