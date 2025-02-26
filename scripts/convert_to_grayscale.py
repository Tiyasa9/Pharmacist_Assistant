import os
import cv2

# Set the absolute path directly
input_folder = r"C:\Users\TIYASA SARKAR\OneDrive\Desktop\Pharmacist_Assistant\data\raw\iam_words\words"
output_folder = r"C:\Users\TIYASA SARKAR\OneDrive\Desktop\Pharmacist_Assistant\data\processed"

print(f"📂 Looking for images in: {input_folder}")

if not os.path.exists(input_folder):
    print("❌ ERROR: Input folder does not exist! Check the path.")
    exit()

os.makedirs(output_folder, exist_ok=True)

found_images = 0
processed_images = 0

for root, _, files in os.walk(input_folder):
    for filename in files:
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            found_images += 1
            image_path = os.path.join(root, filename)
            # print(f"🔍 Processing: {image_path}")

            img = cv2.imread(image_path)
            if img is None:
                print(f"⚠️ ERROR: Could not read {image_path}")
                continue  # Skip this file

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            save_path = os.path.join(output_folder, filename)
            cv2.imwrite(save_path, gray)
            processed_images += 1
            # print(f"✅ Saved: {save_path}")

print(f"✅ Processing complete! Found: {found_images}, Processed: {processed_images}")

