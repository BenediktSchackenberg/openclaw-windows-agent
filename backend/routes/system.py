from fastapi import APIRouter, HTTPException, Depends
from models import System

router = APIRouter()

@router.post("/", response_model=System)
async def add_system(system: System):
    # Logic to UPSERT system_current and INSERT system_changes
    return system