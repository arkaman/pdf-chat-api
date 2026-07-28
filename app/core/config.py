from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-001")
LLM_MODEL = os.getenv("LLM_MODEL")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
UPLOAD_DIR = os.getenv("UPLOAD_DIR")