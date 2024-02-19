import cv2
import os

image_path = "C:/Users/aryan/OneDrive/Desktop/Steganography/Bhim.jpg"

if not os.path.isfile(image_path):
    print(f"Error: Image file '{image_path}' not found.")
    exit()

img = cv2.imread(image_path)

if img is None:
    print(f"Error: Unable to read the image file '{image_path}'.")
    exit()

while True:
    access = input("Enter the access code: ")

    if access == "AByz110!":
        print("Access granted!")
        break
    else:
        print("Wrong Code, Access denied")

img = img.copy()
msg = str(input("Enter Secret Message"))
key = str(input("Choose the Encryption Key, Note: This will be a Symmetric Key Encryption"))

d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

n = 0
m = 0
z = 0

if len(msg) > img.shape[0] * img.shape[1]:
    raise ValueError("Message too long for the given image size")

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.startfile("encryptedImage.jpg")

# Decryption
message = ""
n = 0
m = 0
z = 0

pas = input("Enter Decryption Key")
if pas == key:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    print("Decrypted message is =", message)
else:
    print("You are not Authenticated")
