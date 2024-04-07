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
    image_path = "C:/Users/aryan/OneDrive/Desktop/encryptedImage.jpg"
    decryption_key = input("Enter Decryption Key: ")

    # You need to provide the secret_message that was used during encryption
    secret_message = input("Enter the Secret Message used during encryption: ")

    decrypt_message(image_path, decryption_key, secret_message)
