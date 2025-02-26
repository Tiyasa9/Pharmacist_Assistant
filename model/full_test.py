from preprocessing import preprocess_image
from ocr_hybrid import hybrid_ocr
from nlp_pipeline import postprocess_text
from ocr_google import google_ocr

image_path = preprocess_image("./img.png")  
# ocr_result = hybrid_ocr(image_path)  
ocr_result = google_ocr(image_path)
# final_result = ocr_result
print("Raw OCR Output:\n", ocr_result)
final_result = postprocess_text(ocr_result)  
# print(final_result)

# print("Final Corrected Text:\n", final_result["corrected_text"])
# print("Medicines Detected:\n", final_result["medicines_detected"])
# print("Final Corrected Text:\n", final_result["corrected_text"])
print("Medicines Detected:\n", final_result["medicines_detected"])
