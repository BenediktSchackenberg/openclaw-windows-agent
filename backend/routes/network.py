from fastapi import APIRouter, HTTPException, Depends
from models import Network

router = APIRouter()

@router.post("/", response_model=Network)
async def add_network(network: Network):
    # Logic to UPSERT network_current and INSERT network_changes
    return network