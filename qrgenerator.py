import qrcode
from PIL import Image

# Get user input
data = input("Enter the text for the QR code: ")

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

# Display the QR code using PIL
qr_image.show()

# Save the QR code to a file (optional)
qr_image.save("qr_code.png")

