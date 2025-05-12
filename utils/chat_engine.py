from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os
import logging

def build_retrieval_chain(docs, prompt):
    db = Chroma.from_documents(docs, OpenAIEmbeddings())
    return RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 1}),
        chain_type_kwargs={"prompt": prompt},
    )

def get_gpt_answer(docs, query, prompt, api_key):
    try:
        os.environ["OPENAI_API_KEY"] = api_key
        chain = build_retrieval_chain(docs, prompt)
        output = chain.invoke({"query": query})
        return output["result"]
    except Exception as e:
        logging.error(f"GPT error: {e}")
        return "❌ GPT error"
