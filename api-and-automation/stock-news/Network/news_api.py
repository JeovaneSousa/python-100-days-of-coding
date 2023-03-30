import requests 
import os

STOCK = "TSLA"

class NewsApi():

    def __init__(self) -> None:
        pass

    def fetch_headlines(self):
        base_url = "https://newsapi.org/v2/top-headlines"

        params = {
            "apiKey": os.getenv("NEWS_API_KEY"),
            "country": "us",
            "pageSize": 3,
            "q": f"Tesla"
        }

        response = requests.get(url=base_url, params=params)
        response.raise_for_status()

        data = response.json()
        result_count = data["totalResults"]

        if result_count > 0:
            articles = data["articles"][:3]
            content = ""

            for article in articles:
                title = article["title"]
                description = article["description"]
                source = article["url"]

                content += f"Title: {title}\nDescription: {description}\nSource: {source}\n\n\n"

            return content
        
        else:
            return "No article on the topic was found."


