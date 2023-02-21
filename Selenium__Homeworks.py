from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
header_element = driver.find_element(By.XPATH, '//div[@class="navbar-collapse"]')
try:
    if header_element:
        print("Element is located")
    else:
        print("No Such Element")
except:
    print("Check your code again")
time.sleep(3)
categories = driver.find_element(By.CSS_SELECTOR, "a[class='list-group-item']")
try:
    if categories:
        print("Element is located")
    else:
        print("No Such Element")
except:
    print("Check your code again")

product_elements = driver.find_elements(By.XPATH, '//a[@class="hrefch"]')
price_elements = driver.find_elements(By.TAG_NAME, "h5")
list1 = []
list2 = []
for product in product_elements:
    list1.append(product.text)
print(list1[1])
for price in price_elements:
    list2.append(price.text)
print(max(list2))


driver.quit()
git add .
git commit -m "Add Python homework code"