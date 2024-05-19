# This dictionary will store OTPs temporarily
from otp_generator import generate_otp


otp_store = {}

def verify_otp(user_id, entered_otp):
    """
    Verify if the entered OTP matches the generated OTP for a specific user.
    Returns:
        bool: True if the entered OTP matches the generated OTP, False otherwise.
    """
    generated_otp = otp_store.get(user_id)
    if generated_otp is None:
        return False
    return entered_otp == generated_otp

def generate_and_store_otp(user_id):
    """
    Returns:
        str: The generated OTP.
    """
    otp = generate_otp()
    otp_store[user_id] = otp
    return otp


