from auth import verify_password, verify_totp
from qr_generator import create_qr

def main():
    print("=== LOGIN SYSTEM (Password + TOTP) ===")

    username = input("Username: ")
    password = input("Password: ")

    # 1. Verifiko password
    if not verify_password(username, password):
        print("❌ Wrong username or password")
        return

    print("✅ Password correct")

    # 2. Setup TOTP (QR)
    secret = create_qr(username)

    print("\nOpen Google Authenticator and scan QR\n")

    # 3. Verifiko kodin nga telefoni
    code = input("Enter TOTP code: ")

    if verify_totp(secret, code):
        print("✅ Login SUCCESS (2FA passed)")
    else:
        print("❌ Invalid TOTP code")

if __name__ == "__main__":
    main()