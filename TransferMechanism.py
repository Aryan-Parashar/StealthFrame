import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def execute_creation():
    try:
        subprocess.run(['python','C:/Users/aryan/Creation.py'], check=True)
        print("Creation.py executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing Creation.py: {e}")

def send_email(sender_email, sender_password, recipient_email, image_path):
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Image Transfer'

    
    with open(image_path, 'rb') as file:
        image = MIMEImage(file.read())
        message.attach(image)

    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        
        server.sendmail(sender_email, recipient_email, message.as_string())

if __name__ == "__main__":
    
    sender_email = 'aryanmayoor@gmail.com'
    sender_password = 'nczc nxlm djdu yexe'
    recipient_email = 'aryan25ic011@satiengg.in'
    output_image_path = 'C:/Users/aryan/OneDrive/Desktop/Steganography/encryptedImage.jpg'

  
    execute_working_model()

    send_email(sender_email, sender_password, recipient_email, output_image_path)
