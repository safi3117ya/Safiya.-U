from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.gemini_generator import generate_legal_document

router = APIRouter()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str

@router.get("/")
def home():
    return {"message": "LegalEase API is running!"}

@router.post("/generate")
def generate_doc(request: DocumentRequest):
    generated_text = generate_legal_document(
        document_type=request.document_type,
        parties=request.parties,
        terms=request.terms,
        effective_date=request.effective_date
    )
    return {
        "status": "success",
        "document": generated_text
    }