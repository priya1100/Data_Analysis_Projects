import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_otp_email(receiver_email, otp):
    """
    Send the OTP to the specified email address.
    Raises:
        Exception: If there is an error during the email sending process.
    """
    try:
        # Your email credentials
        sender_email = "haripriyaavril2468@gmail.com"
        password = "uxag cjpb rjcj rbfs"

        # Create a MIMEText object to represent the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = "OTP Verification"

        # Add the OTP to the email body
        body = f"Your OTP for verification: {otp}"
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("OTP sent successfully!")
    except Exception as e:
        raise Exception("Error sending OTP email:", e)
