from Network.stock_api import StockApi
from brooker import Brooker
from Network.news_api import NewsApi

stock_api = StockApi()
news_api = NewsApi()
brooker = Brooker()

yesterday_close, the_day_before_close = stock_api.get_stock_close_prices()
is_change_significant, message = brooker.calculate_difference(yesterdays_value=yesterday_close, the_day_before_value=the_day_before_close)
content = news_api.fetch_headlines()

if is_change_significant:
    brooker.send_email(
        recipient="jeovanesousa@icloud.com",
        subject=message,
        content=content.encode()
        )
else:
    print(message)

