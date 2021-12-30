import requests
import smtplib
import time


from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

url = 'https://www.amazon.sa/-/en/Apple-iPhone-11-FaceTime-SIM/dp/B07Y3L5KWP/ref=sr_1_5?dchild=1&keywords=iphone+11&qid=1613635330&sr=8-5'


def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")

    title = soup.find(id='productTitle').get_text()
    price = soup.find(class_="a-price-whole").get_text()
    converted_price = (price)
    converted_price2 = converted_price. replace(',', '')
    converted_price3 = float(converted_price2[0:5])

    if (converted_price3 < 3.000):
        send_mail()

    print(converted_price3)
    print(title.strip())

    if(converted_price3 > 3.000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('michael.asiass@gmail.com', 'rdsvragplpzwfmoi')

    subject = "Price Fell Down"
    body = 'Check The Amazon Link https: // www.amazon.sa/-/en/Apple-iPhone-11-FaceTime-SIM/dp/B07Y3L5KWP/ref = sr_1_5?dchild = 1 & keywords = iphone+11 & qid = 1613635330 & sr = 8-5'

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        'michael.asiass@gmail.com',
        'michael.asiass@hotmail.com',
        msg
    )

    print("Hey Email Has Been Sent")

    server.quit()


while(True):
    check_price()
    time.sleep(3600)
