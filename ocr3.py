import cv2
import numpy as np

# Function to perform image preprocessing
def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to binarize the image
    binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Perform morphological operations (dilation and erosion) to remove noise
    kernel = np.ones((3,3), np.uint8)
    binary_image = cv2.dilate(binary_image, kernel, iterations=1)
    binary_image = cv2.erode(binary_image, kernel, iterations=1)

    # Apply Gaussian blur to smoothen the image
    blurred_image = cv2.GaussianBlur(binary_image, (5, 5), 0)

    # Perform edge detection using Canny edge detector
    edges = cv2.Canny(blurred_image, 30, 150)

    # Find contours in the image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Display the preprocessed image
    # cv2.imshow("Preprocessed Image", image)
    cv2.imwrite("preprocessed.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the input image
image_path = "myImage.jpg"

# Perform image preprocessing
preprocess_image(image_path)
