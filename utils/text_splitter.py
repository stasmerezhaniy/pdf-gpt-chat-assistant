from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text, chunk_size=1000, overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.create_documents([text])
