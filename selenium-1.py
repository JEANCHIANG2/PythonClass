from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://drug.bibian.co.jp/'
driver.get(url)

titles = driver.find_elements(By.CLASS_NAME,'styled__ProductName-sc-1tvxax2-2 dSAsiw')
# time.sleep(3)
# search.send_keys('韓')
# time.sleep(2)
# search.send_keys('劇')
# time.sleep(1)
# search.send_keys('網')
# time.sleep(5)
# search.send_keys(Keys.ENTER)
# time.sleep(20)
# print(titles)
for title in titles:
    print(title)