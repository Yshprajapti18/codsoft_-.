import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*'

    pool = lowercase_letters + uppercase_letters + digits + special_characters

    if length < 8:
        length = 8

    password = ''.join(random.choice(pool) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired password length: "))

    password = generate_password(length)

    print("Generated Password: " + password)

if __name__ == "__main__":
    main()
