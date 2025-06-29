from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from app.routes.product_routes import router as product_router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Store API - Bootcamp Santander 2025")

@app.on_event("startup")
async def startup_db():
    app.mongodb_client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    app.mongodb = app.mongodb_client[os.getenv("MONGO_DB")]
    print("MongoDB connected!")

@app.on_event("shutdown")
async def shutdown_db():
    app.mongodb_client.close()

app.include_router(product_router)