import tkinter as tk
from tkinter import messagebox
from email_sender import send_otp_email
from otp_verifier import generate_and_store_otp, verify_otp

class OTPVerificationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("OTP Verification System")

        self.email_label = tk.Label(master, text="Enter your email address:")
        self.email_label.pack()

        self.email_entry = tk.Entry(master)
        self.email_entry.pack()

        self.send_otp_button = tk.Button(master, text="Send OTP", command=self.send_otp)
        self.send_otp_button.pack()

        self.otp_label = tk.Label(master, text="Enter OTP:")
        self.otp_label.pack()

        self.otp_entry = tk.Entry(master)
        self.otp_entry.pack()

        self.verify_button = tk.Button(master, text="Verify OTP", command=self.verify_otp)
        self.verify_button.pack()

    def send_otp(self):
        email = self.email_entry.get()
        if not email:
            messagebox.showerror("Error", "Email address cannot be empty")
            return
        generated_otp = generate_and_store_otp(email)
        # For simplicity, let's just print the OTP to the console
        print(f"OTP sent to {email}: {generated_otp}")
        send_otp_email(email, generated_otp)
        messagebox.showinfo("OTP Sent", f"OTP sent to {email}")

    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        email = self.email_entry.get()
        if not entered_otp or not email:
            messagebox.showerror("Error", "Please enter both email address and OTP")
            return

        if verify_otp(email, entered_otp):
            messagebox.showinfo("Success", "Access Granted!")
        else:
            messagebox.showerror("Access Denied", "Incorrect OTP. Access Denied!")

def main():
    root = tk.Tk()
    app = OTPVerificationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
