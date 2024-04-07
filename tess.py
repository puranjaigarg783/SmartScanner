import os
from PIL import Image
import pytesseract
import sys

# Use the first command line argument as the image path
image_path = sys.argv[1]

# Ensure the image file exists
if os.path.exists(image_path):
    # Perform OCR on the image
    text = pytesseract.image_to_string(Image.open(image_path), lang="eng", config='--psm 11')
    # Replace newline characters with spaces and print the result on a single line
    print(text.replace('\n', ' '))
else:
    print("Image file does not exist.")

