import requests
import time
from datetime import datetime
import smtplib

MY_LAT = -3.732714 # Your latitude
LAT_MIN_RANGE = MY_LAT - 5
LAT_MAX_RANGE = MY_LAT + 5

MY_LONG = -38.526997 # Your longitude
LONG_MIN_RANGE = MY_LONG - 5
LONG_MAX_RANGE = MY_LONG + 5

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"iss latitude: {iss_latitude}")
    print(f"iss longitude: {iss_longitude}")

    if  LAT_MIN_RANGE <= iss_latitude <= LAT_MAX_RANGE and LONG_MIN_RANGE <= iss_longitude <= LONG_MAX_RANGE:
        print("Iss Overhead!")
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(f"sunrise: {sunrise}")
    print(f"sunset: {sunset}")

    time_now = datetime.now()
    hour = time_now.hour

    if hour in range(1,sunrise) or hour in range(sunset,25):
        print("It`s night Time!")
        return True
    return False

def send_email():
    MY_EMAIL = "xofas.motivational.message@gmail.com"
    PASSWORD = "wpgnqtdmrcftxtuu"
    GMAIL_SMTP = "smtp.gmail.com"

    with smtplib.SMTP(GMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="jeovanesousa@icloud.com",
                            msg="Subject:ISS is Close! Look UP!\n\nHello! \nIss is flying above you. Go check it out! \nCya!")

while True:
    time.sleep(60)
    if is_iss_close() and is_night():
        send_email()




