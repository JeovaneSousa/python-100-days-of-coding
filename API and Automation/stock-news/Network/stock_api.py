import os 
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CLOSING_TIME = "20:00:00"
CLOSE_KEY = "4. close"

class StockApi:

    def __init__(self) -> None:
        pass

    def get_stock_close_prices(self) -> tuple[float, float]:
        
        today = dt.date.today()
        today_weekday = today.isoweekday()

        yesterday:dt.date = dt.date(
                        year=today.year,
                        month=today.month,
                        day=today.day - 1
                        )

        the_day_before = dt.date(
                        year=yesterday.year,
                        month=yesterday.month,
                        day=yesterday.day - 1
    )
        base_url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": STOCK,
            "interval": "60min",
            "apikey": os.getenv("STOCK_API_KEY")
        }
        response = requests.get(url=base_url, params=params)
        response.raise_for_status()
        data = response.json()

        yesterday_close_value = data["Time Series (60min)"][f"{yesterday} {CLOSING_TIME}"][CLOSE_KEY]
        the_day_before_close_value = data["Time Series (60min)"][f"{the_day_before} {CLOSING_TIME}"][CLOSE_KEY]
        
        print(f"Yesterday`s value was: {yesterday_close_value} And the day before: {the_day_before_close_value}")

        return (float(yesterday_close_value), float(the_day_before_close_value))