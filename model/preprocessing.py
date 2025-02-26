import cv2
import numpy as np

def preprocess_image(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE for contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)

    # Apply Gaussian Blur to remove noise
    blurred = cv2.GaussianBlur(enhanced, (5,5), 0)

    # Apply Adaptive Thresholding
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)

    # Save the processed image
    preprocessed_path = "preprocessed.png"
    cv2.imwrite(preprocessed_path, binary)

    return preprocessed_path
