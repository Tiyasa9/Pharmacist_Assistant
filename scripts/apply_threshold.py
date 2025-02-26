import cv2
import os

# Paths
input_folder = r"C:\Users\TIYASA SARKAR\OneDrive\Desktop\Pharmacist_Assistant\data\processed" # Use processed grayscale images
output_folder = r"C:\Users\TIYASA SARKAR\OneDrive\Desktop\Pharmacist_Assistant\data\thresholded"  # Create a new folder for thresholded images

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each grayscale image
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):  # Change extension if needed
        img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)

        # Apply Otsu's Thresholding
        _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Save the thresholded image
        cv2.imwrite(os.path.join(output_folder, filename), thresh)

print("Thresholding completed! Check the 'data/thresholded' folder.")
