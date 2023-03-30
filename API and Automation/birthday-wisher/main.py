
import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "xofas.motivational.message@gmail.com"
PASSWORD = "wpgnqtdmrcftxtuu"
GMAIL_SMTP = "smtp.gmail.com"

def send_email(message, recipient):
    with smtplib.SMTP(GMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=recipient, 
                            msg=f"Subject: Happy Birthday!!\n\n{message}")
        
today = dt.date.today()

data = pandas.read_csv("birthdays.csv", index_col=[0])
birthday_rows = data[(data.month == today.month) & (data.day == today.day)]

if len(birthday_rows.index) != 0:
    for (_ ,row) in birthday_rows.iterrows():
        random_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
        name = str(row.name).capitalize()
        email_to_send = str(row.email)

        with open(random_letter, mode="r") as file:
            letter = file.readlines()
            adapted_letter = "".join(letter).replace("[NAME]",name)
            send_email(adapted_letter, email_to_send)
else:
    print("No birthdays today.")



