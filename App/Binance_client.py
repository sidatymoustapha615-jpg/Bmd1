import pandas as pd
from binance.client import Client

from app.config import BINANCE_API_KEY, BINANCE_API_SECRET


def get_client():
    return Client(
        BINANCE_API_KEY or None,
        BINANCE_API_SECRET or None
    )


def get_market_data(symbol, interval="15m", limit=100):
    try:
        client = get_client()

        candles = client.get_klines(
            symbol=symbol,
            interval=interval,
            limit=limit
        )

        df = pd.DataFrame(candles, columns=[
            "time", "open", "high", "low", "close",
            "volume", "close_time", "quote_volume",
            "trades", "taker_buy_base",
            "taker_buy_quote", "ignore"
        ])

        for col in ["open", "high", "low", "close", "volume"]:
            df[col] = pd.to_numeric(df[col])

        return df

    except Exception as error:
        print(f"Binance connection error: {error}")
        return None


def get_current_price(symbol):
    try:
        client = get_client()
        ticker = client.get_symbol_ticker(symbol=symbol)
        return float(ticker["price"])

    except Exception as error:
        print(f"Price error: {error}")
        return None
