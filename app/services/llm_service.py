from google import genai

from app.core.config import (
    GEMINI_API_KEY,
    LLM_MODEL,
)

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_answer(
    context: str,
    question: str,
) -> str:
    """
    Generate an answer using the retrieved document context.
    """

    prompt = f"""
    You are a helpful assistant.
        
    Answer ONLY using the provided context.
        
    If the answer cannot be found, say:
    "I couldn't find that information in the uploaded document."
        
    Context:
    {context}
        
    Question:
    {question}
    """

    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt,
    )

    if response.text is None:
        raise ValueError("Gemini returned an empty response.")

    return response.text.strip()