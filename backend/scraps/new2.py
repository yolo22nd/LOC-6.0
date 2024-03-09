import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

results=[]
# base_url = "https://www.flipkart.com/search"
# base_url = "https://www.amazon.in/Campus-11G-677-Black-North-Running/dp/B08PSGW8H9/ref=sr_1_4_sspa?crid=256VHHTCGXB4&dib=eyJ2IjoiMSJ9.tE5mNLJoSjmwDC0qCnukyIQWR4HKCMnh5qiaGmmKznWqyjbx_yaFaqQIwmdX8oprDDhHmeseVOnCQTrdIFBcXKXfx-LEGhKR82Wbj-G0XGyhknQKCkF5QzhYt9rid_XLlh386_EvE0f0YmpL5xKeNp5OI1F99NhT2IPyThRyd6jSdM4x_BPXzJzNHheqOy7jutMA7rLUdVgt1PVU0-uhTXjNQs_S82vGWEl2NduahXLmjRimg14933z7G-CciE-7tO4XQwDEDwukQmjNcudIVDeMTjw9jD2FzNLBB05sw2s.jkxGk9tTFZeqjLxZN2oI4B0kNlMfhJIxDm97S1RS6t0&dib_tag=se&keywords=shoes&qid=1709999845&sprefix=shoes%2Caps%2C223&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1"
base_url = "https://www.amazon.in/Apple-iPhone-13-128GB-Green/dp/B09G9HDN4Q/ref=sr_1_1?crid=1EA3SCHCHDZF2&dib=eyJ2IjoiMSJ9.lylV35R4vlcik0aaO6wOgUefKEwUaeYWK_OuM494a4M2jxaiHGLt-9jMmKFSoG5Orh4Y7OSuWxfkGXRCMvTHdohYmhkhicOTJnl7Pyk2HcGupNeJu_-_GgEuV6Se1pwcIUJZUsGXv1xb_Cp60U71vNzMMC9J0ZWPhbQSVsIzCqUjIv4xGv3AdFxIeiubIVLa.FP_WPgel0NsZggtK-G1O5U14rn_TxPwGLAHspRzOp7w&dib_tag=se&keywords=Apple%2BiPhone%2BXS%2B(Space%2BGrey%2C%2B64%2BGB)&qid=1709968267&sprefix=apple%2Biphone%2Bxs%2Bspace%2Bgrey%2C%2B64%2Bgb%2B%2Caps%2C322&sr=8-1&th=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(base_url, headers=user_agent)
soup = BeautifulSoup(response.content, "html.parser")
print(response)


# params = {"q": query}

# response = requests.get(base_url)
# response.raise_for_status()

# soup = BeautifulSoup(response.content, "html.parser")
# print(response)



# print(new_soup)
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
        # print(j.text.strip()+"    efsaf")
# product["price"] = soup.find("span", attrs={"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'})

# product["price"] = soup.find('span', class_ = 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay').text
print(product["price"])

# product["desc_table_list"] = []
# description = soup.find('table', {'id': 'productDetails_detailBullets_sections1'})
# for row in description.find_all('tr'):
#     key = row.find('th').text.strip()
#     value = row.find('td').text.strip()
#     product["desc_table_list"].append({key: value})




temp = soup.find("div", attrs={"class":"a-expander-content a-expander-partial-collapse-content"})
print(temp)
# for i in temp:
#     print(i)
# product["discount"] = 


product["img"] = [img['src'] for img in soup.find_all('img', {'class': 'a-dynamic-image'})]
# print(product["img"])

product["discount"] = soup.find("span", attrs={"class":'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).text.strip()
print(product["discount"])

product["about"] = [li.text.strip() for li in soup.find_all('li', {'class': 'a-spacing-small item'})]

product["rating"] = soup.find("span", attrs={"class":'a-icon-alt'}).text.strip()

product["link"] = base_url

product["variations"] = [li.text.strip() for li in soup.find_all('li', {'class': 'a-spacing-small item'})]

product["options"] = [img['src'] for img in soup.find_all('img', {'class': 'imgSwatch'})]

results.append(product)

# print(results)


# # counter += 1


# print(results)

# # Fetching offers from the URL
# # response_inner = requests.get(href_inner)
# # soup_inner = BeautifulSoup(response_inner.content, "html.parser")
# # offers = soup_inner.find_all("li", {"class": "_16eBzU col"})
# # for offer in offers:
# #     results[-1].setdefault("offers", []).append(offer.text.strip())
# # reviews = soup_inner.find("span", {"class": "_2_R_DZ"})
# # if reviews:
# #     reviews_text = reviews.text.strip()
# #     reviews_number = reviews_text.split("&")[-1].strip()
# #     results[-1]["reviews"] = reviews_number
# # cut_price_element = soup_inner.find("div", {"class": "_3I9_wc _2p6lqe"})
# # if cut_price_element:
# #     cut_price = cut_price_element.text.strip()
# #     results[-1]["cut_price"] = cut_price

# #coupons
# # coupon_price_list = []
# # for prices in price_list:
# #     without_special_symbol = prices.removeprefix("₹").replace(",", "")
# #     price_int = int(without_special_symbol)
# #     coupon_price_float = price_int * 0.05
# #     coupon_price_list.append(str(round(coupon_price_float)))

# # coupon_price_singal_digit = []
# # for i in coupon_price_list:
# #     for char in i:
# #         coupon_price_singal_digit.append(char)
# # coupon_price_val = coupon_price(coupon_price_singal_digit)

# # results[-1]['after 5%'] = coupon_price_list
# # results[-1]['coupon_val'] = coupon_price_val
