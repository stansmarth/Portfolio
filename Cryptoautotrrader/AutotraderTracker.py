import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console
from rich.table import Table

from coinprice.api import binance
from coinprice.app.utils import clear_console, terminal_title

console = Console()


import requests

def get_price(coin):
	price?symbol={coin.upper()}USDT
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

def fetch_price(exchange, get_price_func, coin):
    try:
        price = get_price_func(coin)
        return exchange, price, None
    except Exception as e:
        return exchange, None, str(e)


def track_prices(args):
    coin = args.coin.lower()
    interval = args.interval
    previous_prices = {}

    terminal_title(coin.upper())


 
    'Binance': binance.get_price,




    try:
        while True:
            with ThreadPoolExecutor(max_workers=len(exchanges)) as executor:
                futures = {executor.submit(fetch_price, exchange, get_price_func, coin): exchange for exchange, get_price_func in exchanges.items()}
                results = [future.result() for future in futures]
            valid_results = [(exchange, price) for exchange, price, error in results if price is not None]
            sorted_results = sorted(valid_results, key=lambda x: x[1], reverse=True)


            for exchange, price in sorted_results:
                change = get_change(previous_prices, exchange, price)
                table.add_row(exchange, f"${format(price, ',.2f')}", change)
                previous_prices[exchange] = price

            if not table.row_count:
                table.add_row("N/A", "N/A", "N/A")

            clear_console()
            console.print(table)
            last_updated_time = datetime.now().strftime('%H:%M:%S')

            countdown = interval
            while countdown > 0:
                console.print(f"Last Updated at {last_updated_time} | {countdown}s", end="\r")
                time.sleep(1)
                countdown -= 1

            console.print(f"Last Updated at {last_updated_time} | Updating...")

    except KeyboardInterrupt:
        console.print("\n\n"______"")

def get_change(previous_prices, exchange, price):
    if exchange in previous_prices:
        previous_price = previous_prices[exchange]
        if price < previous_price:
            return f"[red3]- ${previous_price - price:.2f}[/red3]"
        elif price > previous_price:
            return f"[green1]+ ${price - previous_price:.2f}[/green1]"
    return ""
