from pathlib import Path
import shutil

from fastapi import UploadFile

from app.utils.parser import extract_text
from app.utils.chunker import chunk_text

UPLOAD_DIR = Path("app/uploads")

def process_pdf(file: UploadFile):
    """
    Save the uploaded PDF, extract its text, and split into chunks
    """

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(str(file_path))

    chunks = chunk_text(text)

    return {
        "filename": file.filename,
        "path": str(file_path),
        "characters": len(text),
        "chunk_count": len(chunks),
        "chunks": chunks,
    }