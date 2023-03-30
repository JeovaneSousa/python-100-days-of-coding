import smtplib
import random
import datetime as dt

LIST_TO_SEND = ["adacarinadt@gmail.com",
                "jeovanesousa@icloud.com",
                "caroldourado_@hotmail.com",
                "alissoncleberdt60@gmail.com"]

MY_EMAIL = "xofas.motivational.message@gmail.com"
PASSWORD = "wpgnqtdmrcftxtuu"
GMAIL_SMTP = "smtp.gmail.com"

today = dt.datetime.now().isoweekday()

if today == 1:
    with open(file="quotes.txt") as file:
        quotes = []
        total_quotes = file.readlines()

        for quote in total_quotes:
            quote = "".join(quote.splitlines())
            quotes.append(quote)

    for recipient in LIST_TO_SEND:
        with smtplib.SMTP(GMAIL_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=recipient,
                                msg=f"Subject:MESSAGE OF THE DAY\n\n{random.choice(quotes)}")
            connection.close()
