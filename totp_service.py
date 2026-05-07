import pyotp

def get_totp(secret):
    return pyotp.TOTP(secret)