from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import time

# Set up selenium webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

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
products = driver.find_elements("css selector", "#products .product")
# item_ids = [item.get_attribute("id") for item in items]
products.reverse()

# Check time and end game time
timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

# Game loop
while True:
    cookie.click()

    # Do a action every 5 seconds
    if time.time() > timeout:
        # Buy a product
        for product in products:
            if product.get_attribute("class") == "product unlocked enabled":
                product.click()
                break

        # Buy an upgrade
        upgrade = driver.find_element("css selector", "#upgrades .upgrade")
        if upgrade:
            try:
                upgrade.click()
            except WebDriverException:
                pass

        timeout = time.time() + 5  # Reset timer

    # If 5 mins are passed, end game
    if time.time() > five_min:
        break

per_second = driver.find_element("css selector", "#cookies div")
print(per_second.text)

driver.quit()
