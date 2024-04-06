import cv2
import numpy as np

def preprocess_image_for_ocr(image):
    # Grayscale conversion 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarization 
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Noise reduction 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Sharpening 
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(opening, -1, kernel)

    return sharpened

image = cv2.imread('myImage.jpg')
preprocessed_image = preprocess_image_for_ocr(image)
cv2.imwrite("preprocessed.jpg", preprocessed_image)