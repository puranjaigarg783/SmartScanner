import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Open the image
image = 'myImage.jpg'

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
image = 'myImage.jpg'

# Use the reader to read text from the image
results = reader.readtext(image)

# Print the detected text
for result in results:
    text = result[1]
    print(text, end=' ')
