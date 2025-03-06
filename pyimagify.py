import qrcode
import matplotlib.pyplot as plt

# Ask the user for input
data = input("Enter the text or URL to generate a QR code: ")

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
qr_img = qr.make_image(fill="black", back_color="white")

# Display the QR code
plt.imshow(qr_img, cmap="gray")
plt.axis("off")
plt.show()

# Save the QR code as an image
qr_img.save("qrcode.png")
print("QR code saved as 'qrcode.png'")