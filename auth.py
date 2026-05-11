from totp_service import get_totp

#user i thjeshte(demo)
USER_DB = {
    "route66" : "12345678"
}

def verify_password(username, password):
    return USER_DB.get(username) == password

def verify_totp(secret, code):
    totp = get_totp(secret)
    return totp.verify(code)