import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import numpy as np
import time




def inner_page_details(base_url):
    results=[]
    # base_url = "https://www.amazon.in/Campus-11G-677-Black-North-Running/dp/B08PSGW8H9/ref=sr_1_4_sspa?crid=256VHHTCGXB4&dib=eyJ2IjoiMSJ9.tE5mNLJoSjmwDC0qCnukyIQWR4HKCMnh5qiaGmmKznWqyjbx_yaFaqQIwmdX8oprDDhHmeseVOnCQTrdIFBcXKXfx-LEGhKR82Wbj-G0XGyhknQKCkF5QzhYt9rid_XLlh386_EvE0f0YmpL5xKeNp5OI1F99NhT2IPyThRyd6jSdM4x_BPXzJzNHheqOy7jutMA7rLUdVgt1PVU0-uhTXjNQs_S82vGWEl2NduahXLmjRimg14933z7G-CciE-7tO4XQwDEDwukQmjNcudIVDeMTjw9jD2FzNLBB05sw2s.jkxGk9tTFZeqjLxZN2oI4B0kNlMfhJIxDm97S1RS6t0&dib_tag=se&keywords=shoes&qid=1709999845&sprefix=shoes%2Caps%2C223&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1"
    # base_url = "https://www.amazon.in/Apple-iPhone-13-128GB-Green/dp/B09G9HDN4Q/ref=sr_1_1?crid=1EA3SCHCHDZF2&dib=eyJ2IjoiMSJ9.lylV35R4vlcik0aaO6wOgUefKEwUaeYWK_OuM494a4M2jxaiHGLt-9jMmKFSoG5Orh4Y7OSuWxfkGXRCMvTHdohYmhkhicOTJnl7Pyk2HcGupNeJu_-_GgEuV6Se1pwcIUJZUsGXv1xb_Cp60U71vNzMMC9J0ZWPhbQSVsIzCqUjIv4xGv3AdFxIeiubIVLa.FP_WPgel0NsZggtK-G1O5U14rn_TxPwGLAHspRzOp7w&dib_tag=se&keywords=Apple%2BiPhone%2BXS%2B(Space%2BGrey%2C%2B64%2BGB)&qid=1709968267&sprefix=apple%2Biphone%2Bxs%2Bspace%2Bgrey%2C%2B64%2Bgb%2B%2Caps%2C322&sr=8-1&th=1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response = requests.get(base_url, headers=user_agent)
    soup = BeautifulSoup(response.content, "html.parser")
    print(response)

    product={}
    product['website']="amazon"

    product["title"] = soup.find("span", attrs={"id":'productTitle'}).text.strip()
    print(product["title"])
    temp = soup.find("span", attrs={"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'})
    count = 1
    for i in temp:
        for j in i:
            if count == 3:
                product["price"]=j.text.strip()
            count+=1
    print(product["price"])




    temp = soup.find_all("div", attrs={"class":"a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"})
    print(temp)
    # for i in temp:
    #     print(i)
    # product["discount"] = 
    # temp = soup.get_elent



    xpath='/html/body/div[2]/div/div[5]/div[8]/div[7]/div/div[1]/ul/li[1]/span/span[1]/text()'

    product["img"] = [img['src'] for img in soup.find_all('img', {'class': 'a-dynamic-image'})]
    # print(product["img"])

    product["discount"] = soup.find("span", attrs={"class":'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).text.strip()
    print(product["discount"])

    product["about"] = [li.text.strip() for li in soup.find_all('li', {'class': 'a-spacing-small item'})]

    product["rating"] = soup.find("span", attrs={"class":'a-icon-alt'}).text.strip()

    product["link"] = base_url

    product["variations"] = [li.text.strip() for li in soup.find_all('li', {'class': 'a-spacing-small item'})]

    product["options"] = [img['src'] for img in soup.find_all('img', {'class': 'imgSwatch'})]

    return product





def coupon_price(coupon_price_singal_digit):
    modified_coupon_list = coupon_price_singal_digit.copy()
    if len(modified_coupon_list) < 2:
        return None  # or some other value that makes sense in your context

    if modified_coupon_list[-1] != '0':
        modified_coupon_list[-1] = '0'

    if modified_coupon_list[-2] in ['6', '7', '8']:
        modified_coupon_list[-2] = '5'

    if modified_coupon_list[-2] in ['4', '3', '2', '1']:
        modified_coupon_list[-2] = '0'
        
    coupon_price = int("".join(modified_coupon_list))

    if modified_coupon_list[-2] == '9':
        convert_to_int = int("".join(modified_coupon_list))
        ten = convert_to_int + 10
        coupon_price = ten

    return coupon_price


def scrape_amazon_search(query):
    page = 1
    temp = []
    counter = 0

    while page != 2 and counter <= 6:
        base_url = f'https://www.amazon.in/s?k={query}&page={page}'
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

        web_page = requests.get(base_url, headers=user_agent)
        web_page.raise_for_status()
        soup = BeautifulSoup(web_page.content, 'html.parser')

        product_urls = soup.find_all('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

        if product_urls is None:
            print('Product URLs Not Found!')
        else:
            for url in product_urls:
                #url
                link = 'https://www.amazon.in' + url.get('href')


                temp = inner_page_details(link)


                #asin
                splitting_asin = link.split('dp')
                a = splitting_asin[1]
                slicing = a[1:13:1]
                modifying1 = slicing.removeprefix("2F")
                asin = modifying1.removesuffix('/r')


                reviews_element = soup.find('a', attrs={'id':'askATFLink'})
                if reviews_element is not None:
                    reviews = soup.find('a', attrs={'id':'askATFLink'}).text.strip().split(" ")[0]
                else:
                    reviews = 'No reviews'
                temp['reviews']=reviews
                

                # bank_offer_num = soup.find('div', attrs={'id': 'itembox-InstantBankDiscount'})
                # if bank_offer_num is not None:
                #     bank_offer_num_txt = bank_offer_num.find('a', attrs={'class': 'a-size-base a-link-emphasis vsx-offers-count'}).string.strip().split(" ")[1]
                # else:
                #     bank_offer_num_txt = ""

                # bank_offer_url = f"https://www.amazon.in/hctp/vsxoffer?asin={asin}&deviceType=web&offerType=InstantBankDiscount&buyingOptionIndex"
                # time.sleep(2)
                # result=[]
                # try:
                #     request_bank_offer = requests.get(bank_offer_url, headers=user_agent)
                #     request_bank_offer.raise_for_status()
                #     soup_bank_offer = BeautifulSoup(request_bank_offer.content, 'html.parser')
                    
                #     if bank_offer_num_txt == 'offers':
                #         bank_offers = soup_bank_offer.find_all('p', attrs={'class': 'a-spacing-mini a-size-base-plus'})
                #         result["offers"] = [offer.get_text() for offer in bank_offers]
                #     else:
                #         bank_offer = soup_bank_offer.find_all('h1', attrs={'class': 'a-size-medium-plus a-spacing-medium a-spacing-top-small'})
                #         result["offers"] = [offer.get_text().strip() for offer in bank_offer]

                #     temp['offers']=result

                #     counter += 1
                #     if counter >= 5:
                #         break

                # except requests.exceptions.HTTPError as e:
                #     print(f"Error fetching bank offers for URL: {bank_offer_url}")
                #     print(f"Exception: {str(e)}")
                
        page += 1
        print(temp[-1])

    return temp


newnew=scrape_amazon_search(input("enter search query"))

df = pd.DataFrame(newnew)

    # Save the DataFrame as a CSV file
    # If the file does not exist, it will be created. If it does exist, the new data will be appended without the header.
    # df.to_csv("output.csv", mode='a', header=False, index=False)

