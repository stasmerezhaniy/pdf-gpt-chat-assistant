import fitz
from utils.pdf_reader import extract_text_from_pdf

def test_extract_text_from_pdf():
    doc = fitz.open("sample.pdf")
    text = extract_text_from_pdf(doc)
    assert isinstance(text, str)
    assert len(text) > 0
