from pathlib import Path
import shutil

from fastapi import UploadFile

from app.services.embedding_service import generate_embeddings
from app.utils.parser import extract_text
from app.utils.chunker import chunk_text
from app.services.vector_store import add_document
from app.services.vector_store import delete_document

import logging

logger = logging.getLogger(__name__)

UPLOAD_DIR = Path("app/uploads")

def process_pdf(file: UploadFile) -> dict:
    """
    Save the uploaded PDF, extract its text, and split into chunks
    """
    logger.info("Uploading PDF: %s", file.filename)

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(str(file_path))

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    add_document(
        filename=file.filename,
        chunks=chunks,
        embeddings=embeddings,
    )

    logger.info(
        "Processed PDF '%s': %d characters, %d chunks",
        file.filename,
        len(text),
        len(chunks),
    )

    return {
        "message": "PDF uploaded successfully.",
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks),
        "indexed": True,
    }



def delete_pdf(filename: str) -> dict:
    """
    Delete a PDF from storage and remove its embeddings.
    """

    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found.")

    # Remove vectors
    delete_document(filename)

    # Remove the uploaded file
    file_path.unlink()

    return {
        "message": "PDF deleted successfully.",
        "filename": filename,
    }