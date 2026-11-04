def calculate_ema(prices, period):
    if len(prices) < period:
        return None

    multiplier = 2 / (period + 1)
    ema = sum(prices[:period]) / period

    for price in prices[period:]:
        ema = (price * multiplier) + (
            ema * (1 - multiplier)
        )

    return ema


def analyze_market(prices):
    if len(prices) < 30:
        return {
            "signal": "WAIT",
            "reason": "بيانات غير كافية"
        }

    ema_fast = calculate_ema(prices, 9)
    ema_slow = calculate_ema(prices, 21)

    if ema_fast > ema_slow:
        return {
            "signal": "BUY",
            "reason": "الاتجاه صاعد",
            "ema_fast": ema_fast,
            "ema_slow": ema_slow
        }

    if ema_fast < ema_slow:
        return {
            "signal": "SELL",
            "reason": "الاتجاه هابط",
            "ema_fast": ema_fast,
            "ema_slow": ema_slow
        }

    return {
        "signal": "WAIT",
        "reason": "لا توجد إشارة واضحة"
    }
