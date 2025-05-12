import streamlit as st
import fitz  # PyMuPDF
import openai
from api_key import API_KEY

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

st.title("📄 PDF Chat Assistant with GPT")

# Persona selector
selected_persona = st.selectbox("Choose a response persona:", personas)

# File upload
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

text = ""
chunks = []

if uploaded_file is not None:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = extract_text_from_pdf(doc)
    chunks = split_text(text)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
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
