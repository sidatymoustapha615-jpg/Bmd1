from app.config import WATCHLIST, TIMEFRAME, INITIAL_CAPITAL
from app.binance_client import get_market_data
from app.strategy import analyze_market


def run_analysis():
    balance = INITIAL_CAPITAL

    print("================================")
    print("BMD AI TRADING AGENT")
    print("MODE: DEMO")
    print("MARKET: BINANCE SPOT")
    print("================================")

    for symbol in WATCHLIST:
        df = get_market_data(symbol, TIMEFRAME)

        if df is None or len(df) < 30:
            print(symbol, "WAIT - No data")
            continue

        prices = df["close"].astype(float).tolist()

        result = analyze_market(prices)

        price = prices[-1]

        print("--------------------------------")
        print("COIN:", symbol)
        print("PRICE:", price)
        print("SIGNAL:", result["signal"])
        print("REASON:", result["reason"])
        print("BALANCE:", balance, "USDT")


if __name__ == "__main__":
    run_analysis()
