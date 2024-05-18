from PIL import Image, ImageDraw, ImageFont

# Open the image
img = Image.open('1.jpg') #as a file uploaded
draw = ImageDraw.Draw(img)

# Watermark text
text = "Adrian"

# Font settings
font_size = 50
try:
    font = ImageFont.truetype('arial.ttf', font_size)
except IOError:
    font = ImageFont.load_default()

# Calculate text width and height using textbbox
text_bbox = draw.textbbox((0, 0), text, font=font)
textwidth = text_bbox[2] - text_bbox[0]
textheight = text_bbox[3] - text_bbox[1]

# Image dimensions
width, height = img.size

# Position for the watermark text
x = (width - textwidth) // 2
y = (height - textheight) // 2

# Add text to image
draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

# Save the image with watermark
img.save('watermark.png')

# Open the saved watermarked image to verify
watermarked_img = Image.open('watermark.png')
watermarked_img.show()
