import random
import string

def generate_password(length):
    if length < 3:
        raise ValueError("Password length should be at least 3 characters")

    # Define the character sets to be used in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one character from each set if length allows
    password = []
    if length >= 4:
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special)
        ]

    # Fill the rest of the password length with random choices from all sets combined
    all_chars = lower + upper + digits + special
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle the resulting list to avoid predictable patterns
    random.shuffle(password)

    # Join the list into a string and return it
    return ''.join(password)

def main():
    print("Password Generator")
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        if num_passwords < 1:
            raise ValueError("You must generate at least one password.")
        
        passwords = []
        for i in range(1, num_passwords + 1):
            while True:
                try:
                    length = int(input(f"Enter the length of Password #{i}: "))
                    if length < 3:
                        raise ValueError("Minimum length of password should be 3")
                    passwords.append(generate_password(length))
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid length.")

        print(f"\nGenerating {num_passwords} passwords\n")
        for i, password in enumerate(passwords, 1):
            print(f"Password #{i}: {password}")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")

if __name__ == "__main__":
    main()
