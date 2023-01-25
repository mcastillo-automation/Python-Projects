import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable as clickable

form = "https://forms.gle/KCy4K7RAFvDEY9Dg7"
zillow_url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.884030776813404%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.666392961164114%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}

# Using requests, let's grab the HTML for ZILLOW
zillow_request = requests.get(url=zillow_url, headers=headers)
print(zillow_request.raise_for_status())
zillow_results = zillow_request.text

# Convert to a BeautifulSoup object
soup = BeautifulSoup(markup=zillow_results, features="lxml")

# Results are in json object, so we need to convert that to a dictionary via json.loads()
data = json.loads(str(soup.select_one("script[data-zrr-shared-data-key]").contents[0]).strip("!<>-"))

# Collect all the urls.
urls = [result['detailUrl'] for result in data['cat1']['searchResults']['listResults']]

# Most urls are inoperable. We must convert to usable zillow links.

links = []
for link in urls:
    if link.startswith('https'):
        links.append(link)
    else:
        link = f'https://www.zillow.com{link}'
        links.append(link)

print(f'There are {len(links)} results')

# grab all prices for listings

prices = [
    int(result["units"][0]["price"].strip("$").replace(",", "").strip("+"))
    if "units" in result
    else result["unformattedPrice"]
    for result in data["cat1"]["searchResults"]["listResults"]]

print(f'There are {len(prices)} prices')

# grab all addresses for listings

addresses = [result['address'] for result in data["cat1"]["searchResults"]["listResults"]]
print(f'There are {len(addresses)} addresses')

# load Selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

for (address, price, address_link) in zip(addresses, prices, links):
    # Navigate to form
    driver.get(url=form)

    # wait for and locate address input
    address_input = driver.find_element(By.CSS_SELECTOR,
                                        value="[role] [role='listitem']:nth-of-type(1) .AgroKb [jscontroller] input")
    WebDriverWait(driver=driver, timeout=3).until(method=clickable(address_input))
    address_input.click()
    address_input.send_keys(address)

    # locate price input
    price_input = driver.find_element(By.CSS_SELECTOR,
                                      value="[role] [role='listitem']:nth-of-type(2) .AgroKb [jscontroller] input")
    price_input.click()
    price_input.send_keys(price)

    # locate link input
    link_input = driver.find_element(By.CSS_SELECTOR,
                                     value="[role] [role='listitem']:nth-of-type(3) .AgroKb [jscontroller] input")
    link_input.click()
    link_input.send_keys(address_link)

    # Click submit button
    submit_button = driver.find_element(By.CSS_SELECTOR, value=".lRwqcd .snByac")
    submit_button.click()

driver.quit()
