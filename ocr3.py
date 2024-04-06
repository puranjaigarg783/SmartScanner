import cv2
import numpy as np

def deskew(image):

    co_ords = np.column_stack(np.where(image > 0))

    angle = cv2.minAreaRect(co_ords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    print(angle)
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated

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

    # Detect lines using Hough Line Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

    # Calculate the angle of rotation to straighten the image
    # angle = 0.0
    # if lines is not None:
    #     total_angle = 0.0
    #     num_lines = len(lines)
    #     for line in lines:
    #         x1, y1, x2, y2 = line[0]
    #         total_angle += np.arctan2(y2 - y1, x2 - x1)
    #     angle = total_angle / num_lines

    # Perform rotation to straighten the image
    # rotated_image = cv2.rotate(blurred_image, cv2.ROTATE_180)
    rotated_image = deskew(blurred_image)

    # Find contours in the image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Display the preprocessed image
    cv2.imshow("Preprocessed Image", rotated_image)
    cv2.imwrite("preprocessed.jpg", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the input image
image_path = "myImage.jpg"

# Perform image preprocessing
preprocess_image(image_path)
