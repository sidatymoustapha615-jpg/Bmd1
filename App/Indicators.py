import pandas as pd
import numpy as np


def calculate_indicators(df):
    if df is None or len(df) < 30:
        return None

    df = df.copy()

    # Moving averages
    df["EMA_9"] = df["close"].ewm(
        span=9, adjust=False
    ).mean()

    df["EMA_21"] = df["close"].ewm(
        span=21, adjust=False
    ).mean()

    # RSI
    delta = df["close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(
        alpha=1/14, adjust=False
    ).mean()

    avg_loss = loss.ewm(
        alpha=1/14, adjust=False
    ).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)

    df["RSI"] = 100 - (100 / (1 + rs))

    return df
