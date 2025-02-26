# from nlp_processing import spell_correct, extract_medicine_info

# def postprocess_text(ocr_text):
#     corrected_text = spell_correct(ocr_text)
#     medicines = extract_medicine_info(corrected_text)

#     return {
#         "corrected_text": corrected_text,
#         "medicines_detected": medicines
#     }

from nlp_processing import spell_correct, extract_medicine_info

def postprocess_text(ocr_text):
    corrected_text = spell_correct(ocr_text)
    medicines = extract_medicine_info(ocr_text)

    # Ensure medicines are properly formatted
    if isinstance(medicines, list):  # Check if it's a list
        medicines = ", ".join(medicines)  # Convert to a readable string

    return {
        # "corrected_text": corrected_text,
        "medicines_detected": medicines
    }
