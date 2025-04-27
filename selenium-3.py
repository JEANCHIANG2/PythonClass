from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = 'https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
driver = webdriver.Chrome()
driver.get(url)

# n = 0
# while n < 3:
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight-1000)')
#     time.sleep(5)
#     n +=1


info = driver.find_elements(By.CLASS_NAME, 'product-card__info')
# titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__title')
time.sleep(3)


for item in info:
    title = item.find_element(By.CLASS_NAME,'product-card__title').text
    price = item.find_element(By.CLASS_NAME, 'product-card__price').text
    print(f'{title}:{price}')