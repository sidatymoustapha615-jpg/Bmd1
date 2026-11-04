from app.config import (
    WATCHLIST,
    TIMEFRAME,
    INITIAL_CAPITAL
)

from app.binance_client import get_market_data
from app.indicators import calculate_indicators
from app.strategy import generate_signal


def run_analysis():
    balance = INITIAL_CAPITAL

    print("BMD AI TRADING AGENT")
    print("Mode: DEMO")
    print("Market: BINANCE SPOT")

    for symbol in WATCHLIST:
        df = get_market_data(symbol, TIMEFRAME)

        if df is None:
            continue

        df = calculate_indicators(df)

        if df is None:
            continue

        signal = generate_signal(df)

        price = float(df["close"].iloc[-1])

        print(
            f"{symbol} | "
            f"Price: {price} | "
            f"Signal: {signal} | "
            f"Balance: {balance} USDT"
        )


if __name__ == "__main__":
    run_analysis()
