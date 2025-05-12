from pdf2image import convert_from_path
import os
import tempfile
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_with_ocr(pdf_path):
    try:
        text = ""
        poppler_path = os.path.abspath("poppler/Library/bin")

        images = convert_from_path(
            pdf_path,
            poppler_path=poppler_path
        )

        for i, image in enumerate(images):
            page_text = pytesseract.image_to_string(image, lang='eng+ukr')
            text += f"\n--- Page {i + 1} ---\n" + page_text.strip()
        return text
    except Exception as e:
        print(f"OCR error: {e}")
        return ""
