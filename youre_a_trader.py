# DISCLAIMER:
# This script is provided for educational purposes only. 
# Ensure you understand the risks involved in automated trading 
# and test the script in a sandbox or paper trading environment 
# before using it with real funds. The author is not responsible 
# for any financial loss incurred using this script.

import os
import logging
from alpaca.data.requests import StockLatestTradeRequest
from alpaca.data.requests import CryptoLatestTradeRequest
from alpaca.data import StockDataStream
from alpaca.data import CryptoDataStream
from alpaca import TradingClient
from alpaca.orders import MarketOrder
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('APCA_API_KEY_ID')
API_SECRET = os.getenv('APCA_API_SECRET_KEY')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Initialize the trading client
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)  # Set paper to False for live trading

def place_order(symbol: str, qty: float, side: str, is_crypto: bool = False):
    """
    Place an order for stocks or crypto.
    :param symbol: Symbol of the asset to trade (e.g., 'AAPL' or 'BTCUSD')
    :param qty: Quantity to trade
    :param side: 'buy' or 'sell'
    :param is_crypto: Set True for crypto, False for stocks
    :return: Order response or None
    """
    try:
        if is_crypto:
            latest_trade = CryptoDataStream(client=trading_client).get_latest_trade(CryptoLatestTradeRequest(symbol))
        else:
            latest_trade = StockDataStream(client=trading_client).get_latest_trade(StockLatestTradeRequest(symbol))

        order = MarketOrder(
            symbol=symbol,
            qty=qty,
            side=side,
            time_in_force='gtc'
        )
        return trading_client.submit_order(order)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None

# Example usage
# Go follow me on Instagram, show me a little support! Don't be a dick: @hiimmichael_
if __name__ == "__main__":
    pass
    # Buy 5 shares of AAPL
    # buy_order = place_order("AAPL", 5, 'buy')
    # logger.info(buy_order)

    # Sell 2 shares of AAPL
    # sell_order = place_order("AAPL", 2, 'sell')
    # logger.info(sell_order)

    # Buy 0.1 BTC
    # buy_crypto = place_order("BTCUSD", 0.1, 'buy', True)
    # logger.info(buy_crypto)

    # Sell 0.05 BTC
    # sell_crypto = place_order("BTCUSD", 0.05, 'sell', True)
    # logger.info(sell_crypto)
