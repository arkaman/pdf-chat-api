from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(
        text: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
) -> list[str]:
    """
    Split text into overlapping chunks

    Args:
        text: Full document text
        chunk_size: Maximum characters per chunk
        chunk_overlap: Number of overlapping characters

    Returns:
        List of text chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    return splitter.split_text(text)