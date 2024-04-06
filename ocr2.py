import keras_ocr

# Load the pre-trained pipeline
pipeline = keras_ocr.pipeline.Pipeline()

# Read the image
image_path = 'myImage7.jpg'
image = keras_ocr.tools.read(image_path)

# Generate text predictions
predictions = pipeline.recognize([image])[0]

# Extract the recognized text
recognized_text = ''
for text, box in predictions:
    recognized_text += text + ' '

print("Recognized Text:")
print(recognized_text)
