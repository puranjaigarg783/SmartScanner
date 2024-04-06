import pytesseract
from PIL import Image

# Load the image
image_path = '/home/puranjai/projects/usfca/projX/myImage.jpg'
image = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
import pytesseract
from pytesseract import Output
from PIL import Image
import cv2

img_path1 = 'myImage.jpg'
text = pytesseract.image_to_string(img_path1,lang='eng')
print(text)
import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Open the image
image = 'image.jpg'

# Use the reader to read text from the image
results = reader.readtext(image)

# Print the detected text
for result in results:
    text = result[1]
    print(text)
import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Open the image
image = 'image.jpg'

# Use the reader to read text from the image
results = reader.readtext(image)

# Print the detected text
for result in results:
    text = result[1]
    print(text, end=' ')
