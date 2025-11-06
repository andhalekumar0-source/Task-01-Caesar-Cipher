# Caesar Cipher Program

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            stay_in_alphabet = 65 if char.isupper() else 97
            result += chr((ord(char) - stay_in_alphabet + shift) % 26 + stay_in_alphabet)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("===== Caesar Cipher Program =====")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
print(f"\nEncrypted Message: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted Message: {decrypted}")
