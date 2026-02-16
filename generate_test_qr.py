import qrcode
from PIL import Image, ImageDraw, ImageFont


qr_data = "https://example.com"
text_below = "ABC123"


qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(qr_data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

width, height = qr_img.size

extra_space = 120
canvas = Image.new("RGB", (width, height + extra_space), "white")
canvas.paste(qr_img, (0, 0))

draw = ImageDraw.Draw(canvas)

try:
    font = ImageFont.truetype("arial.ttf", 50)
except:
    font = ImageFont.load_default()

# Pillow 12 compatible text size
bbox = draw.textbbox((0, 0), text_below, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

text_x = (width - text_width) // 2
text_y = height + 30

draw.text((text_x, text_y), text_below, fill="black", font=font)


canvas.save("test_qr.png")

print("Test QR saved as test_qr.png")
