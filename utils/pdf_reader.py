import fitz  # PyMuPDF
from utils.ocr_fallback import extract_text_with_ocr

def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()

        if not text.strip():
            print("⚠️ No extractable text found. Falling back to OCR.")
            text = extract_text_with_ocr(file_path)

        return text
    except Exception as e:
        print(f"❌ PDF read error: {e}")
        return ""
