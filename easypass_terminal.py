import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_numbers=True, use_special=True):
    char_pool = ""
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

    if not char_pool:
        print("❌ No character sets selected! Please enable at least one option.")
        return None

    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    print("🔐 Strong Password Generator (Terminal Version)")
    print("-" * 40)
    try:
        length = int(input("Enter password length (e.g. 12): "))
        if length <= 0:
            raise ValueError
    except ValueError:
        print("⚠️ Please enter a valid positive number.")
        return

    print("\nSelect character types to include:")
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_lower, use_upper, use_numbers, use_special)
    if password:
        print("\n✅ Your generated password:")
        print(password)

if __name__ == "__main__":
    main()
