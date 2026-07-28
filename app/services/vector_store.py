from chromadb import PersistentClient

from app.core.config import CHROMA_DB_PATH

COLLECTION_NAME = "pdf_documents"

client = PersistentClient(path=CHROMA_DB_PATH)


def get_collection():
    """Get or create the ChromaDB collection."""
    return client.get_or_create_collection(name=COLLECTION_NAME)


collection = get_collection()


def add_document(
    filename: str,
    chunks: list[str],
    embeddings: list[list[float]],
) -> None:
    """
    Store a document's chunks and embeddings in ChromaDB.
    """

    if len(chunks) != len(embeddings):
        raise ValueError(
            "Number of chunks and embeddings must match."
        )

    # Replace old document if it already exists
    delete_document(filename)

    ids = [
        f"{filename}_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        {
            "filename": filename,
            "chunk": i,
        }
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search(
    query_embedding: list[float],
    k: int = 5,
) -> dict:
    """
    Search for the top-k most similar document chunks.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
    )

    return {
        "documents": results["documents"][0],
        "metadatas": results["metadatas"][0],
        "distances": results["distances"][0],
    }


def delete_document(filename: str) -> None:
    """
    Delete all chunks belonging to a document.
    """

    collection.delete(
        where={"filename": filename}
    )


def count() -> int:
    """
    Return the total number of indexed chunks.
    """

    return collection.count()