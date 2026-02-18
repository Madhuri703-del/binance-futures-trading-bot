from bot import BasicBot
from config import API_KEY, API_SECRET
from logger import log_info

log_info("Bot program started")


def validate_side(side):
    return side.upper() in ["BUY", "SELL"]

def validate_order_type(order_type):
    return order_type.upper() in ["MARKET", "LIMIT", "STOP"]

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter Side (BUY/SELL): ").upper()
    order_type = input("Enter Order Type (MARKET/LIMIT/STOP): ").upper()
    quantity = float(input("Enter Quantity: "))

    if not validate_side(side):
        print("Invalid side!")
        return

    if order_type == "MARKET":
        result = bot.place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        price = float(input("Enter Price: "))
        result = bot.place_limit_order(symbol, side, quantity, price)

    elif order_type == "STOP":
        price = float(input("Enter Limit Price: "))
        stop_price = float(input("Enter Stop Price: "))
        result = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)

    else:
        print("Invalid order type")
        return

    if result:
        print("Order Placed Successfully ✅")
        print(result)
    else:
        print("Order Failed ❌")

if __name__ == "__main__":
    main()
