from fastapi import FastAPI

app = FastAPI(
    title="AI Quant Strategy Builder",
    description="API for building and backtesting trading strategies using natural language",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    return {"status": "ok"} 