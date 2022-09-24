from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up selenium webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(
    "https://orteil.dashnet.org/cookieclicker/"
)
time.sleep(5)
got_it = driver.find_element("link text", "Got it!")
got_it.click()

english = driver.find_element("id", "langSelect-EN")
english.click()
time.sleep(3)

# Get hold of cookie element
cookie = driver.find_element("id", "bigCookie")

# Get hold of items ids
items = driver.find_elements("css selector", "#products div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

# Check time and end game time
timeout = time.time() + 5
five_min = time.time() + 20  # 5minutes

# Game loop
while True:
    cookie.click()

    if time.time() > timeout:
        for id in item_ids:
            pass

    if time.time() > five_min:
        per_second = driver.find_element("id", "cookiesPerSecond")
        print(per_second.text)
        break
