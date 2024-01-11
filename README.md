# Alpaca Trading Bot

This Python project demonstrates the use of the Alpaca API for automated trading. It includes scripts for placing buy and sell orders for both stocks and cryptocurrencies.

## Disclaimer

This script is provided for educational purposes only. Ensure you understand the risks involved in automated trading and test the script in a sandbox or paper trading environment before using it with real funds. The author is not responsible for any financial loss incurred using this script.

## Prerequisites

- Python 3.x
- Alpaca account and API credentials
- python-dotenv package
- alpaca-py package

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/MichaelCoughlinAN/Youre-An-Algo-Trader.git
   cd Youre-An-Algo-Trader
   ```

2. **Set Up a Virtual Environment (Optional)**

   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Required Packages**

   ```sh
   pip install alpaca-py python-dotenv
   ```

4. **Environment Variables**

   Create a `.env` file in the project directory and add your Alpaca API credentials:

   ```
   APCA_API_KEY_ID=your_alpaca_key
   APCA_API_SECRET_KEY=your_alpaca_secret
   ```

## Usage

To run the script:

```sh
python youre_a_trader.py
```

Replace `youre_a_trader.py` with the name of your Python script (if you changed the name).

## Features

- Place market orders for stocks and cryptocurrencies.
- Utilizes Alpaca's latest Python SDK for a seamless trading experience.
- Configurable for both paper and live trading.

## Contributing

Contributions to this project are welcome. Please ensure you follow best practices and update tests as appropriate.


## Contact

- Creator: contact@hiimmichael.com
- IG: @hiimmichael_
- Project Link: https://github.com/MichaelCoughlinAN/Youre-An-Algo-Trader