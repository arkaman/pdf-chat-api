from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.pdf_service import process_pdf

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
    }