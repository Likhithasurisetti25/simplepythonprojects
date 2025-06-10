import random
import string
import re

def get_user_input():
    """Get user preferences for password generation."""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 1): "))
            if length < 1:
                print("Password length must be at least 1")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_lowercase, use_numbers, use_special

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    """
    Generate a secure random password with customizable criteria.
    
    Args:
        length (int): Length of the password (default: 12)
        use_uppercase (bool): Include uppercase letters (default: True)
        use_lowercase (bool): Include lowercase letters (default: True)
        use_numbers (bool): Include numbers (default: True)
        use_special (bool): Include special characters (default: True)
    
    Returns:
        str: Generated password
    """
    # Define character sets based on user preferences
    character_sets = []
    
    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_numbers:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)
    
    # Ensure at least one character set is selected
    if not character_sets:
        raise ValueError("At least one character type must be selected")
    
    # Ensure password length is valid
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    # Generate password ensuring at least one character from each selected set
    password = []
    for char_set in character_sets:
        password.append(random.choice(char_set))
    
    # Fill remaining length with random characters from all sets
    all_chars = ''.join(character_sets)
    remaining_length = length - len(character_sets)
    password.extend(random.choices(all_chars, k=remaining_length))
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to Password Generator!")
    print("-" * 30)
    
    while True:
        # Get user preferences
        length, use_uppercase, use_lowercase, use_numbers, use_special = get_user_input()
        
        try:
            # Generate password with user-specified criteria
            password = generate_password(
                length=length,
                use_uppercase=use_uppercase,
                use_lowercase=use_lowercase,
                use_numbers=use_numbers,
                use_special=use_special
            )
            
            print("\nGenerated Password:", password)
            print("Password Strength:")
            print(f"Length: {length} characters")
            print(f"Includes uppercase: {use_uppercase}")
            print(f"Includes lowercase: {use_lowercase}")
            print(f"Includes numbers: {use_numbers}")
            print(f"Includes special characters: {use_special}")
            
            # Ask if user wants to generate another password
            continue_generating = input("\nGenerate another password? (y/n): ").lower()
            if continue_generating != 'y':
                break
                
        except ValueError as e:
            print(f"Error: {e}")
            continue