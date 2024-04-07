import os
import sys
import contextlib
import keras_ocr
import sys

# Use the first command line argument as the image path
image_path = sys.argv[1]

# Function to suppress print statements
@contextlib.contextmanager
def suppress_print():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

# Suppressing the keras_ocr output
with suppress_print():
    pipeline = keras_ocr.pipeline.Pipeline()
    image = keras_ocr.tools.read(image_path)
    predictions = pipeline.recognize([image])[0]

# Extract the recognized text
recognized_text = ' '.join([text for text, box in predictions])

print(recognized_text)

