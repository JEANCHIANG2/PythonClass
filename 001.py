from selenium import webdriver

from bs4 import BeautifulSoup
url = 'https://www.nike.com/tw'
driver = webdriver.Chrome()
driver.get(url)
htmlfile = driver.page_source
soup = BeautifulSoup(htmlfile,'html.parser')
imgs = soup.find_all('img')

print(imgs)
