import qrcode

# Data to encode with line breaks
data = "for more details:\n" \
       "contact: +91 9441182728\n" \
       "email: mnatarju73@gmail.com"

# Create a QRCode object
qr = qrcode.make(data)

# Save the QR code as an image
qr.save("contact.png")

print("QR generated successfully")
