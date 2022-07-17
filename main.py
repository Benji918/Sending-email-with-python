import smtplib
import datetime as dt
import random
my_email = '' #email
pwd = ''#password
date = dt.datetime.now()
week = date.weekday()
print(week)
if week == 5:
    with open('quotes.txt') as quotes_file:
        quotes = quotes_file.readlines()
        random_quote = random.choice(quotes)
    # Connect to  email server provider
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # secure connection
        connection.starttls()
        # login to email
        connection.login(user=my_email, password=pwd)
        # send an email
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Subject:Motivational Quote of the day!\n\n{random_quote}')


# now = dt.datetime.now()
# day_of_wk = now.weekday()
# print(day_of_wk)
#
# day_of_birth = dt.datetime(year=2002, month=9, day=18, hour=4, minute=45)
# print(day_of_birth)
