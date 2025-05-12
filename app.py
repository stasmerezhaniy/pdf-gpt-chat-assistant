import streamlit as st
import fitz  # PyMuPDF
import openai
from api_key import API_KEY
import tempfile
from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.chat_engine import get_gpt_answer
from utils.prompt_templates import get_persona_prompt

openai.api_key = API_KEY

# Available personas for response style
personas = [
    "John Cena",
    "Winston Churchill",
    "Elon Musk",
    "Taras Shevchenko",
    "Marie Curie"
]

st.title("📄 PDF Chat Assistant with GPT + OCR")

# Persona selector
selected_persona = st.selectbox("Choose a response persona:", personas)

# PDF upload
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

chunks = []  # ensure chunks is defined in case file is not uploaded

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    raw_text = extract_text_from_pdf(tmp_path)

    if not raw_text or not isinstance(raw_text, str):
        st.error("❌ No text could be extracted from this PDF.")
        st.stop()

    chunks = split_text(raw_text)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask a question about the PDF"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if chunks:
        prompt_template = get_persona_prompt(selected_persona)
        response = get_gpt_answer(chunks, prompt, prompt_template, API_KEY)
    else:
        response = "❌ PDF not uploaded or failed to process."

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
