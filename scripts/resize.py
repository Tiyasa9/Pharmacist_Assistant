import cv2
import os

input_folder = r"C:\Users\TIYASA SARKAR\OneDrive\Desktop\Pharmacist_Assistant\data\thresholded"
output_folder = r"C:\Users\TIYASA SARKAR\OneDrive\Desktop\Pharmacist_Assistant\data\resized"
resize_dim = (128, 32)  # Adjust dimensions as per requirement

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"⚠️ ERROR: Could not read {img_path}")
        continue
    
    resized_img = cv2.resize(img, resize_dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(output_folder, filename), resized_img)

print("✅ Resizing complete! Images saved in", output_folder)
