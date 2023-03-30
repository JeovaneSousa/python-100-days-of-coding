import requests
import datetime as dt
import os
from twilio.rest import Client

account_sid = "AC5bc5662190a4081fe10afee6d551b3ed"
auth_token = "5f4ec99588fc590a5406f821623e107b"
client = Client(account_sid, auth_token)

weather_api_key = "be17e07d3fea69d1e6760b5e01e1371f"

def five_days_three_hours_api_call():
    base_url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
    "lat": -3.732714,
    "lon": -38.526997,
    "units": "metric",
    "lang":"pt-br",
    "appid": weather_api_key
    }

    response = requests.get(url=base_url, params=params)
    response.raise_for_status()

    return response.json()


response = five_days_three_hours_api_call()
today = dt.date.today()
will_rain = False

for prediction in response["list"]:

    if not will_rain:
        date_text:str = prediction["dt_txt"]
        date_text_list = date_text.split()
        date_text_list.pop()
        formated_date = date_text_list[0].split(sep="-")
        prediction_date = dt.date(year=int(formated_date[0]),
                                month=int(formated_date[1]),
                                day=int(formated_date[2]))
    
        if today == prediction_date:
            for weather in prediction["weather"]:
                weather_id = weather["id"]
                if weather_id < 700:
                    will_rain = True

if will_rain:
    message = client.messages \
                .create(
                     body="It`s gonna rain tooday.. Bring an umbrella, dummy!",
                     from_='+14065187251',
                     to='+5585988550687'
                 )

    print(message.status)

    