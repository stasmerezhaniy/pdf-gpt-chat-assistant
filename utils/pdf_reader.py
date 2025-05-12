import fitz  # PyMuPDF

def extract_text_from_pdf(doc):
    text = ""
    for page in doc:
        text += page.get_text()
    return text
