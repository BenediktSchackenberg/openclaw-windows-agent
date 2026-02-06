from fastapi import APIRouter, HTTPException, Depends
from models import Hotfix

router = APIRouter()

@router.post("/", response_model=Hotfix)
async def add_hotfix(hotfix: Hotfix):
    # Logic to INSERT into hotfixes_current and hotfixes_changes
    return hotfix