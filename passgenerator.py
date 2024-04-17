import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Length should be at least 4 to include one number and one punctuation character.")

    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length - 1))

    # Add one random digit
    password += random.choice(string.digits)

    # Add one random punctuation character
    password += random.choice(string.punctuation)

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

desired_length = int(input("Enter the desired length for the password (minimum 4 letters): "))
print("Generated Password:", generate_password(desired_length))
