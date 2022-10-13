from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

driverPath = 'C:\Program Files (x86)\chromedriver.exe'
searchString = 'iphone+13'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=driverPath)
driver.get("https://www.amazon.in/s?k=" + searchString)

htmlData = driver.page_source
l_soup = BeautifulSoup(htmlData,'lxml')
driver.quit()

entries = l_soup.find_all('div',class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right')

print('---------------------------')

for entry in entries:
    title = entry.find('span',class_='a-size-medium a-color-base a-text-normal').text
    price = entry.find('span',class_='a-price-whole').text

    print (f''' 
    Product Name: {title}
    Price: {price}
    ''')
    print('---------------------------')