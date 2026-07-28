from google import genai

from app.core.config import GEMINI_API_KEY, EMBEDDING_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=chunks,
    )

    return [embedding.values for embedding in response.embeddings]

def generate_embedding(text: str):
    return generate_embeddings([text])[0]