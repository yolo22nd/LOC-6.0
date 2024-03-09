import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

results=[]
# base_url = "https://www.flipkart.com/search"
base_url = "https://www.amazon.in/Campus-11G-677-Black-North-Running/dp/B08PSGW8H9/ref=sr_1_4_sspa?crid=256VHHTCGXB4&dib=eyJ2IjoiMSJ9.tE5mNLJoSjmwDC0qCnukyIQWR4HKCMnh5qiaGmmKznWqyjbx_yaFaqQIwmdX8oprDDhHmeseVOnCQTrdIFBcXKXfx-LEGhKR82Wbj-G0XGyhknQKCkF5QzhYt9rid_XLlh386_EvE0f0YmpL5xKeNp5OI1F99NhT2IPyThRyd6jSdM4x_BPXzJzNHheqOy7jutMA7rLUdVgt1PVU0-uhTXjNQs_S82vGWEl2NduahXLmjRimg14933z7G-CciE-7tO4XQwDEDwukQmjNcudIVDeMTjw9jD2FzNLBB05sw2s.jkxGk9tTFZeqjLxZN2oI4B0kNlMfhJIxDm97S1RS6t0&dib_tag=se&keywords=shoes&qid=1709999845&sprefix=shoes%2Caps%2C223&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1"
# base_url = "https://www.amazon.in/Apple-iPhone-13-128GB-Green/dp/B09G9HDN4Q/ref=sr_1_1?crid=1EA3SCHCHDZF2&dib=eyJ2IjoiMSJ9.lylV35R4vlcik0aaO6wOgUefKEwUaeYWK_OuM494a4M2jxaiHGLt-9jMmKFSoG5Orh4Y7OSuWxfkGXRCMvTHdohYmhkhicOTJnl7Pyk2HcGupNeJu_-_GgEuV6Se1pwcIUJZUsGXv1xb_Cp60U71vNzMMC9J0ZWPhbQSVsIzCqUjIv4xGv3AdFxIeiubIVLa.FP_WPgel0NsZggtK-G1O5U14rn_TxPwGLAHspRzOp7w&dib_tag=se&keywords=Apple%2BiPhone%2BXS%2B(Space%2BGrey%2C%2B64%2BGB)&qid=1709968267&sprefix=apple%2Biphone%2Bxs%2Bspace%2Bgrey%2C%2B64%2Bgb%2B%2Caps%2C322&sr=8-1&th=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(base_url, headers=headers)
new_soup = BeautifulSoup(response.content, "html.parser")
print(response)


# params = {"q": query}

# response = requests.get(base_url)
# response.raise_for_status()

# soup = BeautifulSoup(response.content, "html.parser")
# print(response)



# print(new_soup)

website="amazon"
title=new_soup.find("span", attrs={"id":'productTitle'}).text.strip()
print(title)
price = new_soup.find('span', class_ = ['a-size-extra-large inemi-amount'])

print(price)


desc_table_list = []
description= new_soup.find('ul', class_ = ['a-bordered'])
for desc_data in description.find_all('tbody'):
    rows = desc_data.find_all('tr')
    for row in rows:
        key = row.find_all('td')[0].text
        value = row.find_all('td')[1].text

        desc_table_list.append({
            "key":key,
            "value":value
        })

print(desc_table_list)


specs_table = new_soup.find('table', class_ = 'a-normal a-spacing-micro')
for specs_data in specs_table.find_all('tbody'):
    rows = new_soup.find_all('tr')
    for row in rows:
        key = row.find_all('td')[0].text
        value = row.find_all('td')[1].text
        specs_table_list = []
        specs_table_list.append({
            "key":key,
            "value":value
        })


url_list=[]
img_all = new_soup.find_all("li", class_=["a-spacing-small item imageThumbnail a-declarative"])
for img in img_all:
    url_list.append(img.get("src"))


discount=new_soup.find("span", attrs={"class":'a-size-medium a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'}).text[1,-2]

about=[]
about_all = new_soup.find_all("li", class_=["a-spacing-mini"])
for i in about_all:
    url_list.append(i.get("span"))

rating=new_soup.find("span", attrs={"class":'a-size-base a-color-base'}).text
link=base_url

variations=[]
variations_all = new_soup.find_all('p', class_ = 'a-text-left a-size-base')
for i in variations_all:
    variations.append(i.text)

options=[]
options_all = new_soup.find_all('img', class_ = 'imgSwatch')
for i in options_all:
    options.append(i.get("src"))


results.append({
    "website":website,
    "title":title,
    "price":price,
    "img":url_list,
    "desc_table_list":desc_table_list,
    "discount":discount,
    "about":about,
    "rating":rating,
    "link":link,
    # "offers":offers,
    "variations":variations,
    "options":options,
    # "reviews":reviews,

    # 'id': counter,
    # "platform": "Flipkart",
    # "title": title_inner,
    # "price": price_inner,
    # "href": href_inner,
    # "img_url": img_url_inner,
    # "rating": rating_inner
})

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
