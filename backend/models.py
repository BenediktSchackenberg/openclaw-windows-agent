from pydantic import BaseModel, Field
from typing import List, Optional

# Pydantic Models

class Hardware(BaseModel):
    id: str
    name: str
    type: str
    manufacturer: Optional[str] = None
    specifications: dict

class Software(BaseModel):
    id: str
    name: str
    version: str
    license_key: Optional[str] = None

class Hotfix(BaseModel):
    id: str
    description: str
    applied_date: Optional[str] = None

class System(BaseModel):
    id: str
    hostname: str
    operating_system: str
    state: str

class Security(BaseModel):
    id: str
    vulnerability: str
    severity: int
    status: str

class Network(BaseModel):
    id: str
    interface: str
    ip_address: str
    mac_address: str

class Browser(BaseModel):
    id: str
    name: str
    version: str
    settings: dict

class FullInventory(BaseModel):
    hardware: List[Hardware]
    software: List[Software]
    hotfixes: List[Hotfix]
    system: System
    security: List[Security]
    network: List[Network]
    browser: List[Browser]