def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            is_upper = char.isupper()
            # Convert the character to its ASCII code
            char_code = ord(char)
            # Apply the shift and ensure it wraps around the alphabet
            shifted_code = (char_code - 65 if is_upper else char_code - 97 + 26)
            encrypted_code = (shifted_code + shift) % 26
            # Convert back to a character
            encrypted_char = chr(encrypted_code + 65 if is_upper else encrypted_code + 97)
            ciphertext += encrypted_char
        else:
            # If the character is not a letter, keep it unchanged
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

# Get input from the user
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

# Encrypt the plaintext
encrypted_text = encrypt(plaintext, shift)
print("Ciphertext:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)
