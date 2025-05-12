from langchain.prompts import PromptTemplate

def get_persona_prompt(persona: str):
    return PromptTemplate(
        template=f"""You are {persona}. Use the context below to answer the question.
Answer in the same language as the question.

{{context}}

Question: {{question}}
Answer:""",
        input_variables=["context", "question"]
    )
