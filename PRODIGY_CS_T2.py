from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = np.array(image)

    # Encrypt the image by applying a basic mathematical operation
    encrypted_data = (data + key) % 256

    # Create and save the encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_image.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")
    encrypted_image.show()

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image = encrypted_image.convert("RGB")
    encrypted_data = np.array(encrypted_image)

    # Decrypt the image by reversing the encryption operation
    decrypted_data = (encrypted_data - key) % 256

    # Create and save the decrypted image
    decrypted_image_path = "decrypted_image.png"
    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    decrypted_image.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

    # Display the decrypted image
    decrypted_image.show()

inputs=input("1)encryption-e 2)decryption-d")
# Get image path and key from the user
image_path = input("Enter the path of the image to be encrypted: ")
key = 50
if inputs=="e":
    # Encrypt the image
    encrypt_image(image_path, key)
else:
    # Decrypt the image
    decrypt_image(image_path, key)
