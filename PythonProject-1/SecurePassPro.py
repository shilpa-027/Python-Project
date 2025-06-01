import random
import string
from colorama import Fore, Style, init

init(autoreset=True)

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_specials=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        raise ValueError("Select at least one character type!")

    return ''.join(random.choice(characters) for _ in range(length))

def password_strength(password):
    length = len(password)
    categories = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password),
    ])

    if length >= 12 and categories == 4:
        return Fore.GREEN + "Strong 💪"
    elif length >= 8 and categories >= 3:
        return Fore.YELLOW + "Medium 🛡️"
    else:
        return Fore.RED + "Weak ⚠️"

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print(Fore.RED + "Please enter 'y' or 'n'.")

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            else:
                print(Fore.RED + "Please enter a positive number.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

def main():
    print(Fore.CYAN + "=== Welcome to SecurePassPro 🔐 ===")

    length = get_int("Password length (e.g., 8,12,16): ")

    use_upper = get_yes_no("Include uppercase? (y/n): ")
    use_lower = get_yes_no("Include lowercase? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_specials = get_yes_no("Include special chars? (y/n): ")

    if not any([use_upper, use_lower, use_digits, use_specials]):
        print(Fore.RED + "Select at least one character type!")
        return

    # Generate one password
    password = generate_password(length, use_upper, use_lower, use_digits, use_specials)
    print(Fore.GREEN + f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")

    # Check custom password strength
    if get_yes_no("\nCheck strength of your own password? (y/n): "):
        custom = input("Enter your password: ")
        print(f"Strength: {password_strength(custom)}")

    # Generate multiple passwords
    if get_yes_no("\nGenerate multiple passwords? (y/n): "):
        count = get_int("How many passwords to generate? ")
        print(Fore.CYAN + "\n--- Generated Passwords ---")
        passwords = []
        for i in range(count):
            pw = generate_password(length, use_upper, use_lower, use_digits, use_specials)
            print(f"{i+1}. {pw} ({password_strength(pw)})")
            passwords.append(pw)

        # Save to file option
        if get_yes_no("\nSave these passwords to a file? (y/n): "):
            filename = input("Enter filename (e.g. passwords.txt): ").strip()
            try:
                with open(filename, 'w') as f:
                    for pw in passwords:
                        f.write(pw + '\n')
                print(Fore.GREEN + f"Passwords saved to {filename}")
            except Exception as e:
                print(Fore.RED + f"Failed to save file: {e}")

    print(Fore.CYAN + "\nThank you for using SecurePassPro! 🔒")

if __name__ == "__main__":
    main()
