import requests

def get_binance_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return data["price"]

if __name__ == "__main__":
    symbol = "BTCUSDT"  # можно заменить на любой другой символ, например ETHUSDT
    price = get_binance_price(symbol)
    print(f"Цена {symbol} на Binance: {price}")