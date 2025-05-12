import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils.chat_engine as chat_engine
from utils.chat_engine import get_gpt_answer
from utils.text_splitter import split_text
from utils.prompt_templates import get_persona_prompt

def test_get_gpt_answer(monkeypatch):
    class MockChain:
        def run(self, query):
            return f"Mock answer to: {query}"

    monkeypatch.setattr(chat_engine, "build_retrieval_chain", lambda docs, prompt: MockChain())

    docs = split_text("This is a test context.")
    prompt = get_persona_prompt("John Cena")
    response = get_gpt_answer(docs, "What is this?", prompt, "fake-key")

    assert response.startswith("Mock answer")
