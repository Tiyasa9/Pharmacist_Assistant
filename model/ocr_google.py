import os
from google.cloud import vision

# Set credentials path (modify accordingly)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./service-acc-key.json"

def google_ocr(image_path):
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    
    # Perform text detection
    response = client.document_text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return "No text detected"
