
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import os


site_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=site_url, headers={"Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,pl;q=0.7",
                                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" })

soup = BeautifulSoup(response.text, "html.parser")

pounds_price = soup.find(class_="a-price-whole").getText()
pence_price = soup.find(class_="a-price-fraction").getText()

full_price = float(pounds_price + pence_price)
name = str(soup.find(class_="a-size-large product-title-word-break").getText())
p_name = name.split()
product_name = ascii(" ".join(p_name))


MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

if full_price < 100:

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="kubaraczkiewicz1@gmail.com",
                        msg=f"Subject: Amazon Price Alert!\n\n {product_name} is below 100! Get on Amazon and buy it before the sale ends\r\n{site_url}")


