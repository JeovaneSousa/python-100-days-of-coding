import os
import smtplib

STOCK = "TSLA"

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
EMAIL_SMTP = "smtp.gmail.com"

class Brooker:
    def __init__(self) -> None:
        pass

    def calculate_difference(self, yesterdays_value: float, the_day_before_value: float):
        difference = yesterdays_value - the_day_before_value
        
        percent_change = ((100 * difference) / the_day_before_value)
        percent_change = round(percent_change)
        print(f"Percent change was: {percent_change}%")

        if percent_change > 0:
            return (True, f"{STOCK}: +{abs(percent_change)}%")

        elif percent_change < 0:
            return (True, f"{STOCK}: -{abs(percent_change)}%")
        
        else:
            return (False, "No significant changes occurred.")

    def send_email(self,recipient, subject, content):
        with smtplib.SMTP(EMAIL_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient,
                msg=f"Subject:{subject}\n\n{content}"
            )