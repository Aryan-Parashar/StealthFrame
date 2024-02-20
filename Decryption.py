import os
import imaplib
import email
from email import policy
from email.parser import BytesParser

def download_attachment(username, password, folder_path):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)

    mail.select("inbox")

    result, data = mail.search(None, '(SUBJECT "Image Transfer")')
    email_ids = data[0].split()

    if not email_ids:
        print("No emails found.")
        return None
    
    latest_email_id = email_ids[-1]
    print(f"Latest email ID: {latest_email_id}")

    try:
        result, msg_data = mail.fetch(latest_email_id, "(RFC822)")
    except Exception as e:
        print(f"Error fetching email: {e}")
        mail.logout()
        return None

    
    msg = BytesParser(policy=policy.default).parsebytes(msg_data[0][1])

    filepath = None

    if msg.is_multipart():
        for part in msg.iter_attachments():
            filename = part.get_filename()
            if filename:
                filepath = os.path.join(folder_path, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                print(f"Downloaded image filepath: {filepath}")
                break  

    
    mail.logout()

    return filepath


if __name__ == "__main__":
    
    receiver_email = 'aryan25ic011@satiengg.in'
    receiver_password = 'Parashar@12personal'
    decryption_key = '123'

    
    download_folder = 'C:/Users/aryan/OneDrive/Desktop/Steganography'

    
    encrypted_image_path = download_attachment(receiver_email, receiver_password, download_folder)

    if encrypted_image_path:
        print(f"Image downloaded to: {encrypted_image_path}")

        
        decrypted_message = decrypt_message(encrypted_image_path, decryption_key)

        if decrypted_message:
            print(f"Decrypted Message: {decrypted_message}")
        else:
            print("Error: Failed to decrypt the message.")
    else:
        print("Error: Failed to download the image.")

def decrypt_message(image_path, decryption_key):
    if image_path is None:
        print("Error: No image file provided.")
        return None

    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image file '{image_path}'.")
        return None

    img = img.copy()
    decrypted_message = ""

    n, m, z = 0, 0, 0

    for _ in range(img.shape[0] * img.shape[1]):
        decrypted_message += chr(img[n, m, z])
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return decrypted_message

if __name__ == "__main__":
    
    receiver_email = 'aryan25ic011@satiengg.in'
    receiver_password = 'Parashar@12personal'
    decryption_key = '123'

    
    download_folder = 'C:/Users/aryan/OneDrive/Desktop/Steganography/ReceivedImages'

    
    encrypted_image_path = download_attachment(receiver_email, receiver_password, download_folder)

    
    decrypted_message = decrypt_message(encrypted_image_path, decryption_key)

    print(f"Decrypted Message: {decrypted_message}")
