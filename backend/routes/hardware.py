from fastapi import APIRouter, HTTPException, Depends
from models import Hardware

router = APIRouter()

@router.post("/", response_model=Hardware)
async def add_hardware(hardware: Hardware):
    # Logic to UPSERT hardware_current and INSERT hardware_changes
    return hardware