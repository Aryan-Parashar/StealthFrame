import cv2
import os

def encrypt_message(image_path, access_code, secret_message, encryption_key):
    if not os.path.isfile(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return

    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image file '{image_path}'.")
        return

    while True:
        access = input("Enter the access code: ")

        if access == access_code:
            print("Access granted!")
            break
        else:
            print("Wrong Code, Access denied")

    img = img.copy()

    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}

    n = 0
    m = 0
    z = 0

    if len(secret_message) > img.shape[0] * img.shape[1]:
        raise ValueError("Message too long for the given image size")

    for i in range(len(secret_message)):
        img[n, m, z] = d[secret_message[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    print("Encryption completed. Image saved as encryptedImage.jpg")

if __name__ == "__main__":
    image_path = "C:/Users/aryan/OneDrive/Desktop/Steganography/Bhim.jpg"
    access_code = "AByz110!"
    secret_message = input("Enter Secret Message: ")
    encryption_key = input("Choose the Encryption Key: ")

    encrypt_message(image_path, access_code, secret_message, encryption_key)

import cv2
import os

def decrypt_message(image_path, decryption_key, secret_message):
    if not os.path.isfile(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return

    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image file '{image_path}'.")
        return

    message = ""
    n = 0
    m = 0
    z = 0

    pas = input("Enter Decryption Key: ")
    if pas == decryption_key:
        for i in range(len(secret_message)):
            message = message + c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3

        print("Decrypted message is =", message)
    else:
        print("You are not Authenticated")

if __name__ == "__main__":
    image_path = "C:/Users/aryan/OneDrive/Desktop/Steganography/encryptedImage.jpg"
    decryption_key = input("Enter Decryption Key: ")

    # You need to provide the secret_message that was used during encryption
    secret_message = input("Enter the Secret Message used during encryption: ")

    decrypt_message(image_path, decryption_key, secret_message)