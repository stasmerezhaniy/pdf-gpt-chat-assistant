from utils.prompt_templates import get_persona_prompt

def test_get_persona_prompt():
    persona = "John Cena"
    prompt = get_persona_prompt(persona)
    assert "John Cena" in prompt.template
    assert "context" in prompt.input_variables
    assert "question" in prompt.input_variables
