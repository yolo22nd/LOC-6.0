flipkart_price_class='_30jeq3 _16Jk6d'
flipkart_title_class='B_NuCI'
sample_url='https://www.flipkart.com/laptops-store?otracker=nmenu_sub_Electronics_0_Laptops'
# URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np

source1 = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70"
source2 = "https://www.amazon.in/Apple-iPhone-Xs-Max-64GB/dp/B07J3CJM4N/ref=sr_1_4?dchild=1&keywords=Apple+iPhone+XS+%28Space+Grey%2C+64+GB%29&qid=1584873760&s=electronics&sr=1-4"
source3 = "https://www.croma.com/apple-iphone-xs-space-grey-64-gb-4-gb-ram-/p/214062"

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
# wd = webdriver.Chrome(r'C:/Users/omtan/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe',OPTIONS=CO)
wd = webdriver.Chrome(options=CO)
# wd = webdriver.Chrome()
print ("*************************************************************************** \n")
print("                     Starting Program, Please wait ..... \n")

print ("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
# f_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
f_price = wd.find_element_by_class_name("_30jeq3 _16Jk6d")
# pr_name = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
pr_name = wd.find_element_by_class_name("B_NuCI")
product = pr_name.text
r_price = f_price.text
print (r_price)
print (" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

print("Connecting to Amazon")
wd.get(source2)
wd.implicitly_wait(wait_imp)
# a_price = wd.find_element_by_id("priceblock_ourprice")
# a_price = wd.find_element_by_xpath("/html/body/div[4]/div[2]/div[4]/div[10]/div[12]/div/table/tbody/tr[2]/td[2]/span[1]")
a_price = wd.find_element_by_id("a-price-whole")
raw_p = a_price.text
print (raw_p)
print (" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)

print("Connecting to Croma")
wd.get(source3)
wd.implicitly_wait(wait_imp)
# c_price = wd.find_element_by_xpath("/html/body/main/div[5]/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/div/div/span")
c_price = wd.find_element_by_id("pdp-product-price")
raw_c = c_price.text
print (raw_c)
print (" ---> Successfully retrieved the price from Croma\n")
time.sleep(2)

# Final display
print ("#------------------------------------------------------------------------#")
print ("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: "+r_price[1:])
print("  Price available at Amazon is: "+raw_p[2:8])
print("   Price available at Croma is: "+raw_c[1:7])

