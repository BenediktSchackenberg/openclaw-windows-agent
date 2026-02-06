from fastapi import APIRouter, HTTPException, Depends
from models import Software

router = APIRouter()

@router.post("/", response_model=Software)
async def add_software(software: Software):
    # Logic to UPSERT software_current and INSERT software_changes
    return software