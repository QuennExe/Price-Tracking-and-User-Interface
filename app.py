
# Price Tracking Application with Python - Gmail SMTP Mailing - Bot Development
# Download the package with the 'pip install requests bs4' command from the project terminal.

import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.apple.com/tr/macbook-air-13-and-15-m2/'

headers = {'User-Agent': ''}  # Kullanıcı ajanınızı bulun ve bu alana yapıştırın


def check_price(url,target):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:18]

    print(title)

    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)

    print(price)

    if price < 15000:
        send_mail(title)


def send_mail(title):
    sender = 'Lolita@gmail.com'
    receiver = 'Lolita2@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login(sender, '85425412541252')  # Replace 'password' with the actual password
        subject = title + ' Sale !!!!!!!!!'
        body = 'Click This Link ---> ' + url
        mailContent = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender, receiver, mailContent)
        print('Email Sent')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

while True:
    # Call the check_price function
    check_price()
    time.sleep(60*60)
