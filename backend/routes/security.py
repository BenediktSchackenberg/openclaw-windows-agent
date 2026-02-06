from fastapi import APIRouter, HTTPException, Depends
from models import Security

router = APIRouter()

@router.post("/", response_model=Security)
async def add_security(security: Security):
    # Logic to UPSERT security_current and INSERT security_changes
    return security