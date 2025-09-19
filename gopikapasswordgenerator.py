import random
import string

def password(a, b, c):
    if c < 8:
        return "Password must be at least 8 characters long!"

    # First 2 letters of name and last 4 of DOB
    p1 = a[:2].capitalize()
    p2 = b[-4:]

    # All possible characters
    letters = string.ascii_letters + string.digits + string.punctuation

    # Random characters to fill the length
    r = ''.join(random.choice(letters) for _ in range(c - len(p1 + p2)))

    # Final password with shuffle
    final = p1 + p2 + r
    final = ''.join(random.sample(final, len(final)))

    return final


# --- Main Program ---

print("Password Generator Program 🔑")

a = input("Enter your name: ")
b = input("Enter your DOB (DD MM YYYY): ")
c = int(input("Password length? (min 8): "))

result = password(a, b, c)
print("Generated Password:", result)
