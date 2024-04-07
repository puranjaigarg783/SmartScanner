import easyocr
import sys

# Use the first command line argument as the image path
image_path = sys.argv[1]

reader = easyocr.Reader(['en'])  # Initialize the reader with English language.
result = reader.readtext(image_path, detail=0)  # detail=0 will return only the text

# Join all the text items into a single line and print
recognized_text = ' '.join(result)
print(recognized_text)

