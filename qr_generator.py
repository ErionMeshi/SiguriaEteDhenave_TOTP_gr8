import pyotp
import qrcode

def create_qr(username, issuer="MyApp"):
  secret=pyotp.random_base32()
  totp=pyotp.TOTP(secret)

uri=totp.provisioning_uri(name=username, issuer_name=issuer)

qr=qrcode.QRCode()
qr.add_data(uri)
qr.make()

print("\n Scan this QR with your phone:\n")
qr.print_ascii(invert=True)

img=qrcode.make(uri)
img.save("qrcode.png")

return secret
