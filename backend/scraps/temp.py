from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import time
import pandas as pd
import numpy as np


review_url = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70"
indiv_review = []
service = Service(executable_path='C:/Users/omtan/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=service,options=options)
driver.get(review_url)


# elements = driver.find_elements(By.CSS_SELECTOR, '.sc-1hez2tp-0.sc-ibxvc.IrFyy')
overall_review = [4.2,4.5,4.3,4.1,4.0,3.9,4.4,4.4,4.2,4.5,4.0,4.0]




# review_url_list = [
#     "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70",
#     "https://www.amazon.in/Apple-iPhone-Xs-Max-64GB/dp/B07J3CJM4N/ref=sr_1_4?dchild=1&keywords=Apple+iPhone+XS+%28Space+Grey%2C+64+GB%29&qid=1584873760&s=electronics&sr=1-4",
#     "https://www.croma.com/apple-iphone-xs-space-grey-64-gb-4-gb-ram-/p/214062"
# ]

dining_rating = []
elements_price = [] # define elements as an empty list
elements_title = [] # define elements as an empty list
page_names = ["Flipkart", "Amazon", "Croma"]


comments = []


driver.get(review_url)

elements_price = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'B_NuCI')))

# elements_title = WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.CLASS_NAME, '_30jeq3 _16Jk6d')))
print("\n\n\n")
# print(elements_title)
print(elements_price)
# temp =[]
# for i in elements:
#     if i !="":
#         temp.append(i.text)
# indiv_review.append(temp)

# try:  
#     elements = WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]/p'))
#         )
# except:
#     elements.extend(["not found"]) # append "not found" to a list, not to a string

# finally:    
#     for element in elements:
#         comments.append(element.get_attribute("innerHTML").encode('utf-8'))






# for  i in review_url_list:
#     driver.get(i)
    
#     elements = WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.sc-1q7bklc-1.cILgox')))
#     temp =[]
#     for i in elements:
#         if i !="":
#             temp.append(i.text)
#     indiv_review.append(temp)
    
#     try:  
#         elements = WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]/p'))
#             )
#     except:
#         elements.extend(["not found"]) # append "not found" to a list, not to a string

#     finally:    
#         for element in elements:
#             comments.append(element.get_attribute("innerHTML").encode('utf-8'))


# elements = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/main/div/section[4]/div/div/section/div[2]/p'))
#     )

# driver.get(review_url)
# print(indiv_review)

products=[
    {'website': 'amazon', 'title': 'Apple iPhone 13 (256GB) - (Product) RED', 'price': '61,900', 'img': ['https://m.media-amazon.com/images/I/315oQlfQ6WL._SY445_SX342_QL70_ML2_.jpg'], 'discount': '-11%', 'about': ['', '', '', '', '', ''], 'rating': '4.6 out of 5 stars', 'link': 'https://www.amazon.in/Apple-iPhone-13-128GB-Green/dp/B09G9HDN4Q/ref=sr_1_1?crid=1EA3SCHCHDZF2&dib=eyJ2IjoiMSJ9.lylV35R4vlcik0aaO6wOgUefKEwUaeYWK_OuM494a4M2jxaiHGLt-9jMmKFSoG5Orh4Y7OSuWxfkGXRCMvTHdohYmhkhicOTJnl7Pyk2HcGupNeJu_-_GgEuV6Se1pwcIUJZUsGXv1xb_Cp60U71vNzMMC9J0ZWPhbQSVsIzCqUjIv4xGv3AdFxIeiubIVLa.FP_WPgel0NsZggtK-G1O5U14rn_TxPwGLAHspRzOp7w&dib_tag=se&keywords=Apple%2BiPhone%2BXS%2B(Space%2BGrey%2C%2B64%2BGB)&qid=1709968267&sprefix=apple%2Biphone%2Bxs%2Bspace%2Bgrey%2C%2B64%2Bgb%2B%2Caps%2C322&sr=8-1&th=1', 'variations': ['', '', '', '', '', ''], 'options': ['https://m.media-amazon.com/images/I/11VmJVS7yrL._SS36_.jpg', 'https://m.media-amazon.com/images/I/11F1Hxzw6qL._SS36_.jpg', 'https://m.media-amazon.com/images/I/11POY6uLQUL._SS36_.jpg', 'https://m.media-amazon.com/images/I/11+wm+cM1LL._SS36_.jpg', 'https://m.media-amazon.com/images/I/01ytk+eqYTL._SS36_.jpg']},
    {'website': 'amazon', 'title': 'Apple iPhone 13 (256GB) - (Product) RED', 'price': '61,900', 'img': ['https://m.media-amazon.com/images/I/315oQlfQ6WL._SY445_SX342_QL70_ML2_.jpg'], 'discount': '-11%', 'about': ['', '', '', '', '', ''], 'rating': '4.6 out of 5 stars', 'link': 'https://www.amazon.in/Apple-iPhone-13-128GB-Green/dp/B09G9HDN4Q/ref=sr_1_1?crid=1EA3SCHCHDZF2&dib=eyJ2IjoiMSJ9.lylV35R4vlcik0aaO6wOgUefKEwUaeYWK_OuM494a4M2jxaiHGLt-9jMmKFSoG5Orh4Y7OSuWxfkGXRCMvTHdohYmhkhicOTJnl7Pyk2HcGupNeJu_-_GgEuV6Se1pwcIUJZUsGXv1xb_Cp60U71vNzMMC9J0ZWPhbQSVsIzCqUjIv4xGv3AdFxIeiubIVLa.FP_WPgel0NsZggtK-G1O5U14rn_TxPwGLAHspRzOp7w&dib_tag=se&keywords=Apple%2BiPhone%2BXS%2B(Space%2BGrey%2C%2B64%2BGB)&qid=1709968267&sprefix=apple%2Biphone%2Bxs%2Bspace%2Bgrey%2C%2B64%2Bgb%2B%2Caps%2C322&sr=8-1&th=1', 'variations': ['', '', '', '', '', ''], 'options': ['https://m.media-amazon.com/images/I/11VmJVS7yrL._SS36_.jpg', 'https://m.media-amazon.com/images/I/11F1Hxzw6qL._SS36_.jpg', 'https://m.media-amazon.com/images/I/11POY6uLQUL._SS36_.jpg', 'https://m.media-amazon.com/images/I/11+wm+cM1LL._SS36_.jpg', 'https://m.media-amazon.com/images/I/01ytk+eqYTL._SS36_.jpg']}
    ]
# Pad the lists in the dictionary so they all have the same length
df = pd.DataFrame(products)

# Save the DataFrame as a CSV file
# If the file does not exist, it will be created. If it does exist, the new data will be appended without the header.
df.to_csv("output.csv", mode='a', header=False, index=False)
