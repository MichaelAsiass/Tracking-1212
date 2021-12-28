import requests
import smtplib


from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


url = 'https://www.amazon.sa/-/en/Apple-iPhone-11-FaceTime-SIM/dp/B07Y3L5KWP/ref=sr_1_5?dchild=1&keywords=iphone+11&qid=1613635330&sr=8-5'


page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "lxml")

title = soup.find(class_="a-price-whole").get_text()

print(title)
