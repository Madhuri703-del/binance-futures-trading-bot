from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import FUTURES_TESTNET_URL
from logger import log_info, log_error


class BasicBot:

    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = FUTURES_TESTNET_URL

    def place_market_order(self, symbol, side, quantity):
        try:
            log_info(f"Placing MARKET order | {side} {quantity} {symbol}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            log_info(f"Order Response: {order}")
            return order

        except BinanceAPIException as e:
            log_error(f"API Error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            log_info(f"Placing LIMIT order | {side} {quantity} {symbol} @ {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            log_info(f"Order Response: {order}")
            return order

        except BinanceAPIException as e:
            log_error(f"API Error: {e}")
            return None
