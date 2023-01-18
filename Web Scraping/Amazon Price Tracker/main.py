import requests
from bs4 import BeautifulSoup as Bs
from smtplib import SMTP as S
from unidecode import unidecode
import config

product_link = "https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/B09MZTP44L"
SALE_PRICE = 99.00

amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept-Language": "en-US,en;q=0.5"
}

amazon_html = requests.get(url=product_link, headers=amazon_headers)
soup = Bs(markup=amazon_html.text, features="lxml")

product_title_contents = soup.select_one("span#productTitle")
product_title = unidecode(product_title_contents.getText().strip())
price_contents = soup.select_one("#apex_desktop_newAccordionRow .a-spacing-none .a-offscreen")
product_price = float(price_contents.getText().split(sep="$")[1])

if product_price <= SALE_PRICE:
    with S(config.email_server) as connection:
        connection.starttls()
        connection.login(user=config.email, password=config.email_app_password)
        connection.sendmail(
            from_addr=config.email,
            to_addrs=config.email,
            msg=f"Subject:Amazon Price Alert\n\n{product_title} is now ${product_price}.\n{product_link}",
        )
