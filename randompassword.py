import random
import string

def generate_password(length=12):
    if length < 3:
        raise ValueError("Password length should be at least 3 to include all character types.")

    # Define character sets
    lower = string.ascii_lowercase      
    upper = string.ascii_uppercase      
    digits = string.digits              

    
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    
    all_chars = lower + upper + digits
    password_chars += random.choices(all_chars, k=length - 3)

    
    random.shuffle(password_chars)

 
    password = ''.join(password_chars)
    return password


if __name__ == "__main__":
    password_length = 12  
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
