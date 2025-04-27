from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://drug.bibian.co.jp/'
driver.get(url)
time.sleep(5)
titles = driver.find_elements(By.CLASS_NAME,'styled__ProductName-sc-1tvxax2-2')

for title in titles:
    print(title.text)