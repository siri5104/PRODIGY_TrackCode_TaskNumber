#task1
def encrypt_caesar_cipher(text, shift):
   
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt_caesar_cipher(text, shift):
   
    return encrypt_caesar_cipher(text, -shift)

def main():
    while True:
        choice = input("Would you like to (e)ncrypt, (d)ecrypt, or (q)uit? ").lower()
        if choice == 'q':
            print("Thank You")
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please choose 'e', 'd', or 'q'.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue



        if choice == 'e':
            encrypted_message = encrypt_caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = decrypt_caesar_cipher(message, shift)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

