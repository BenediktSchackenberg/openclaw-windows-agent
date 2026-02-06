from fastapi import FastAPI, Depends, HTTPException, status
import asyncpg
from routes import hardware, software, hotfixes, system, security, network, browser, full
from auth import AuthMiddleware

# FastAPI App
app = FastAPI()

# Database Connection Pool
DATABASE_URL = "postgresql://openclaw:openclaw_inventory_2026@127.0.0.1:5432/inventory"

async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL)

db_pool = None

@app.on_event("startup")
async def startup():
    global db_pool
    db_pool = await create_pool()

@app.on_event("shutdown")
async def shutdown():
    await db_pool.close()

# Middleware
app.add_middleware(AuthMiddleware)

# API Routes
app.include_router(hardware.router, prefix="/api/v1/inventory/hardware")
app.include_router(software.router, prefix="/api/v1/inventory/software")
app.include_router(hotfixes.router, prefix="/api/v1/inventory/hotfixes")
app.include_router(system.router, prefix="/api/v1/inventory/system")
app.include_router(security.router, prefix="/api/v1/inventory/security")
app.include_router(network.router, prefix="/api/v1/inventory/network")
app.include_router(browser.router, prefix="/api/v1/inventory/browser")
app.include_router(full.router, prefix="/api/v1/inventory/full")