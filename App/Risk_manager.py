def calculate_position_size(
    balance,
    entry_price,
    stop_loss,
    risk_percent=0.01
):
    if balance <= 0 or entry_price <= 0:
        return 0

    risk_amount = balance * risk_percent
    loss_per_unit = abs(entry_price - stop_loss)

    if loss_per_unit <= 0:
        return 0

    quantity = risk_amount / loss_per_unit

    max_quantity = balance / entry_price

    return min(quantity, max_quantity)


def check_daily_loss(
    daily_loss,
    max_daily_loss=0.03
):
    return daily_loss < max_daily_loss


def can_open_trade(open_trades, max_trades=3):
    return open_trades < max_trades
