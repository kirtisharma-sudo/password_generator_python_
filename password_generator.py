import random
import string

print("🔐 PASSWORD GENERATOR 🔐")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(characters)
random.choice(characters)
    

# ---- Main Program ----generator = PasswordGenerator(length)
print("Generated Password:", password)

input("Press Enter to exit...")