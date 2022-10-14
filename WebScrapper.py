import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

searchString = ""

def getHtmlSource(prmSearchString,prmStoreType):

    driverPath = 'C:\Program Files (x86)\chromedriver.exe'
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    l_URL = ""

    #Prepare search String
    if prmStoreType == "AMAZON":
        prmSearchString = prmSearchString.replace(" ","+")
        l_URL= "https://www.amazon.in/s?k="
    elif prmSearchString == "FLIPKART":
        prmSearchString = prmSearchString.replace(" ","%20")
        l_URL = "https://www.flipkart.com/search?q="

    driver = webdriver.Chrome(options=options, executable_path=driverPath)
    driver.get(l_URL + prmSearchString.replace(" ","+"))
    htmlData = driver.page_source
    l_soup = BeautifulSoup(htmlData,'lxml')
    driver.quit()
    return l_soup

def getAmazonData(prmSearchString):
    productData = ()
    productList = []
    
    #ToDo Page Counter for checking next pages
    pageCounter = 0

    htmlSourceData = getHtmlSource(prmSearchString,"AMAZON")
    productEntries = htmlSourceData.find_all('div',class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right')   
    productCounter = 0
    for entry in productEntries:
        productCounter = productCounter + 1
        price = "None"
        title = entry.find('span',class_='a-size-medium a-color-base a-text-normal').text
        if entry.find('span',class_='a-price-whole') is not None:
            price = entry.find('span',class_='a-price-whole').text
        productData =  {"product"+str(productCounter):str(title),"price":str(price)}
        productList.append(productData)
    return productList

searchString = input("Enter Search String to Compare: ")
amaProductList = getAmazonData(searchString)
for product in amaProductList:
    print("\n")
    print(product)