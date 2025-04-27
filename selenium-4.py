from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = 'https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
link = driver.find_element(By.LINK_TEXT,'男款')
link.click()
link2 = driver.find_element(By.LINK_TEXT,'鞋款')
link2.click()
time.sleep(2)
info = driver.find_elements(By.CLASS_NAME, 'product-card__info')
# titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__title')
time.sleep(3)

for item in info:
    title = item.find_element(By.CLASS_NAME,'product-card__title').text
    price = item.find_element(By.CLASS_NAME, 'product-card__price').text
    print(f'{title}:{price}')
