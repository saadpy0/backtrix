from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(
    title="AI Quant Strategy Builder",
    description="API for building and backtesting trading strategies using natural language",
    version="0.1.0"
)

# Include routers
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

@app.get("/health")
async def health_check():
    return {"status": "ok"} 