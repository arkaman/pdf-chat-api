# PDF Chat API

A Retrieval-Augmented Generation (RAG) backend that allows users to upload PDF documents and chat with them using Google's Gemini models. The application extracts text from uploaded PDFs, splits it into chunks, generates embeddings, stores them in ChromaDB, and retrieves the most relevant context to answer user questions.

**Frontend Repo:** [github.com/arkaman/pdf-chat-client](https://github.com/arkaman/pdf-chat-client)

---

## Features

* 📄 Upload PDF documents
* ✂️ Automatic text extraction and chunking
* 🧠 Generate embeddings using Gemini
* 🗄️ Persistent vector storage with ChromaDB
* 💬 Chat with uploaded PDFs using Retrieval-Augmented Generation (RAG)
* 🗑️ Delete indexed documents
* 🚀 FastAPI backend with interactive Swagger documentation

---

## Tech Stack

* **Backend:** FastAPI
* **Language:** Python 3.12+
* **LLM:** Gemini 3.6 Flash
* **Embedding Model:** Gemini `text-embedding-001`
* **Vector Database:** ChromaDB
* **PDF Parser:** PyMuPDF
* **Configuration:** python-dotenv

---

## Architecture

```text
INDEXING PIPELINE:

             PDF Upload
                  │
                  ▼
         Extract Text (PyMuPDF)
                  │
                  ▼
              Chunk Text
                  │
                  ▼
          Generate Embeddings
               (Gemini)
                  │
                  ▼
          Store in ChromaDB


RETRIEVAL PIPELINE:

            User Question
                  │
                  ▼
      Generate Query Embedding
                  │
                  ▼
      Similarity Search (Chroma)
                  │
                  ▼
        Retrieve Top-k Chunks
                  │
                  ▼
           Gemini 3.6 Flash
                  │
                  ▼
              Final Answer
```

---

## Project Structure

```text
pdf-chat-api/
├── app/
│   ├── api/
│   │   ├── routes.py
│   │   └── schemas.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── embedding_service.py
│   │   ├── vector_store.py
│   │   ├── llm_service.py
│   │   └── chat_service.py
│   │
│   ├── utils/
│   │   ├── parser.py
│   │   └── chunker.py
│   │
│   ├── uploads/
│   └── db/
│       └── chroma_db/
│
├── .env
├── pyproject.toml
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/arkaman/pdf-chat-api.git
cd pdf-chat-api
```

### Create a virtual environment

Using `uv`

```bash
uv venv
source .venv/bin/activate
```

### Install dependencies

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key

LLM_MODEL=gemini-3.6-flash
EMBEDDING_MODEL=text-embedding-001

CHROMA_DB_PATH=app/db/chroma_db
```

---

## Running the Application

```bash
uv run fastapi dev
```

The API will be available at

```text
http://127.0.0.1:8000
```

Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Upload a PDF

```http
POST /upload
```

Upload a PDF document for indexing.

Response

```json
{
  "message": "PDF uploaded successfully.",
  "filename": "paper.pdf",
  "characters": 28456,
  "chunks": 36,
  "indexed": true
}
```

---

### Chat with Uploaded PDFs

```http
POST /chat
```

Request

```json
{
  "question": "What is Retrieval-Augmented Generation?"
}
```

Response

```json
{
  "answer": "Retrieval-Augmented Generation (RAG) combines vector search with a language model..."
}
```

---

### Delete a Document

```http
DELETE /documents/{filename}
```

Response

```json
{
  "message": "PDF deleted successfully.",
  "filename": "paper.pdf"
}
```

---

## Services

### `pdf_service.py`

Responsible for the document indexing pipeline.

* Save uploaded PDFs
* Extract text
* Chunk text
* Generate embeddings
* Store vectors in ChromaDB

---

### `embedding_service.py`

Generates embeddings using Gemini.

* Single query embedding
* Batch document embeddings

---

### `vector_store.py`

Wrapper around ChromaDB.

* Add documents
* Search similar chunks
* Delete documents
* Count indexed chunks

---

### `llm_service.py`

Communicates with Gemini.

* Builds prompts
* Generates answers using retrieved context

---

### `chat_service.py`

Coordinates the Retrieval-Augmented Generation workflow.

* Generate query embedding
* Retrieve relevant chunks
* Build context
* Generate the final answer

---

