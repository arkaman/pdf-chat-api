from app.services.embedding_service import generate_embedding
from app.services.vector_store import search
from app.services.llm_service import generate_answer


def chat(question: str) -> str:
    """
    Execute the Retrieval-Augmented Generation (RAG) pipeline.
    """

    # Generate embedding for the user's question
    query_embedding = generate_embedding(question)

    # Retrieve the most relevant chunks
    results = search(query_embedding)

    documents = results["documents"]

    if not documents:
        return "No indexed documents found."

    # Combine retrieved chunks into a single context
    context = "\n\n".join(documents)

    # Generate answer
    answer = generate_answer(
        context=context,
        question=question,
    )

    return answer