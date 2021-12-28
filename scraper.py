import requests
import smtplib

from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


url = 'https://www.amazon.sa/-/en/Apple-iPhone-11-FaceTime-SIM/dp/B07Y3L5KWP/ref=sr_1_5?dchild=1&keywords=iphone+11&qid=1613635330&sr=8-5'


def check_price():

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parsel")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[3:9])

    new_converted_price = print(int(converted_price.replace(",", "")))

    if(new_converted_price < 3000):
        send_mail()

        print(int(new_converted_price))

    if (new_converted_price > 3000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('michael.asiass@gmail.com', 'buxktvqhnkdysqoe')

    subject = "Price Fell Down"
    body = 'Check The Amazon Link https: // www.amazon.sa/-/en/Apple-iPhone-11-FaceTime-SIM/dp/B07Y3L5KWP/ref = sr_1_5?dchild = 1 & keywords = iphone+11 & qid = 1613635330 & sr = 8-5'

    msg = f"subject: {subject}\n\n{body}"

    server.sentmail(
        'michael.asiass@gmail.com',
        'michael.asiass@gmail.com',
        msg

    )

    print("Hey Email Has Been Sent")

    server.quit()


check_price()
