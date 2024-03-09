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


# restaurant_names = ["HnH Salad Co.", "Govinda's Bistro", "Blabber All Day", "Grandmama's Cafe","The Barn @ Food Square","The Homemade Cafe & Bar","Zoca Cafe","Bayleaf Cafe","Toco","Prithvi Cafe"
#                         "Coco Cafe"]
# dict = {"Names": restaurant_names, "overall rating": overall_review, "individual review": indiv_review, "comments": comments}

# create a Pandas DataFrame from the dictionary
# max_len = max(len(v) for v in dict.values())
# save the DataFrame as a CSV file
# dict = {k: np.pad(v, (0, max_len - len(v)), mode="constant") for k, v in dict.items()}

# create a Pandas DataFrame from the padded dictionary
# df = pd.DataFrame(dict)

# save the DataFrame as a CSV file
# df.to_csv("output.csv", header=True, index=False)