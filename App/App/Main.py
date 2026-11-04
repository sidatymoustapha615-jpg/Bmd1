from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.config import (
    MODE,
    STARTING_BALANCE,
    EXCHANGE,
    MARKET_TYPE,
    TIMEFRAME,
    FAST_EMA,
    SLOW_EMA,
    SYMBOLS
)

app = FastAPI(
    title="BMD AI Trading Agent",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "project": "BMD AI Trading Agent",
        "status": "Running",
        "mode": MODE,
        "exchange": EXCHANGE,
        "market": MARKET_TYPE,
        "timeframe": TIMEFRAME,
        "balance": STARTING_BALANCE,
        "strategy": f"EMA {FAST_EMA}/{SLOW_EMA}",
        "monitored_coins": len(SYMBOLS),
        "message": "Welcome to BMD AI Trading Agent"
    }

@app.get("/api/status")
def status():
    return {
        "mode": MODE,
        "balance": STARTING_BALANCE,
        "exchange": EXCHANGE,
        "market": MARKET_TYPE,
        "timeframe": TIMEFRAME,
        "strategy": "EMA",
        "symbols": SYMBOLS,
        "real_trading": False
    }

@app.get("/health")
def health():
    return {
        "ok": True,
        "message": "BMD Agent is healthy"
    }
