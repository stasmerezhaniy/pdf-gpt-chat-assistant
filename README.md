# PDF GPT Chat Assistant (v1.1)

A simple and powerful Streamlit-based chatbot that lets you chat with any PDF document — even scanned or image-based ones — using OpenAI GPT.

Supports OCR fallback via Tesseract, custom response personas (like John Cena or Elon Musk), and conversational memory.

---

## 🚀 Features

* 📄 Upload **any PDF**, including scanned image-based files
* 🧠 Intelligent fallback to **OCR** using Tesseract if no text is detected
* 🤖 Ask **natural language questions** about your document
* 🧑‍🎤 Choose a **response persona** (John Cena, Elon Musk, etc.)
* 💬 Maintains **chat history** inside Streamlit session

---

## 🖼 Example Use Case

Upload a lease agreement, then ask:

> "What can I be evicted for?"

📥 GPT will answer based on the extracted content:

> "You may be evicted for dumping grease into sinks or toilets, performing construction without landlord permission, or keeping animals without written approval."

---

## 🧩 Requirements

### Python packages (install via pip):

```
pip install -r requirements.txt
```

### Additionally, install manually:

#### 🛠 [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

For Windows, install to:

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

And update the following line in `ocr_fallback.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

#### 🧾 [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)

Extract and note the full path to the `bin/` folder. Then update `ocr_fallback.py`:

```python
poppler_path = r"C:\path\to\poppler\bin"
```

---

## 📂 Project Structure

```
pdf_gpt_chat/
├── app.py                # Main Streamlit app
├── api_key.py            # Your OpenAI key (DO NOT COMMIT)
├── requirements.txt      # Python dependencies
├── utils/
│   ├── pdf_reader.py     # Extract text or run OCR
│   ├── ocr_fallback.py   # OCR engine
│   ├── text_splitter.py  # Chunking text
│   ├── chat_engine.py    # GPT-based retriever chain
│   └── prompt_templates.py # Persona prompts
└── tests/                # Unit tests
```

---

## ▶️ Run Locally

```
streamlit run app.py
```

Then open the local URL in your browser.

---

## 🔒 Security

* Make sure `api_key.py` is in `.gitignore`.
* Never commit your OpenAI keys.

---

## 🏁 Roadmap

* [x] OCR fallback
* [x] Persona responses
* [x] Basic tests
* [ ] Add streaming output
* [ ] Hugging Face Spaces demo

---

## 🤝 Author

Developed by **Stanislav Merezhanyi** — a self-taught Python developer passionate about AI-powered tools.
