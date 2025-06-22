from cryptography.fernet import Fernet

# Generate a Fernet key
key = Fernet.generate_key()

# Save the key to a file
with open("answer.key", "wb") as key_file:
    key_file.write(key)

print("✅ Key generated and saved to answer.key")
