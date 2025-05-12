from utils.text_splitter import split_text

def test_split_text():
    text = "This is a sample text. " * 100
    chunks = split_text(text)
    assert isinstance(chunks, list)
    assert len(chunks) > 1
