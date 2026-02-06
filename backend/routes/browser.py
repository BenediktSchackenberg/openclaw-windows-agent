from fastapi import APIRouter, HTTPException, Depends
from models import Browser

router = APIRouter()

@router.post("/", response_model=Browser)
async def add_browser(browser: Browser):
    # Logic to UPSERT browser_current and INSERT browser_changes
    return browser