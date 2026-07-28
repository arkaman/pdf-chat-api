from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.pdf_service import process_pdf
from app.services.chat_service import chat
from app.api.schemas import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    result = process_pdf(file)

    return {
        "message": "PDF uploaded successfully",
        "filename": result["filename"],
        "characters": result["characters"],
        "chunks": result["chunks"],
    }

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):

    answer = chat(request.question)

    return ChatResponse(answer=answer)