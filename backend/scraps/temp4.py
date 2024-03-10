import requests
from bs4 import BeautifulSoup
import pandas as pd

def inner_page_details(base_url):
    base_url = 'https://www.amazon.in/Motorola-Turbocharging-UltraPixel-Technology-Water-Repellent/dp/B0CKLRV6X9/ref=sr_1_3?sr=8-3'
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response = requests.get(base_url, headers=user_agent)
    soup = BeautifulSoup(response.content, "html.parser")
    print(response)

    product={}
    product['website']="amazon"

    desc = []
    temp = soup.find("table", attrs={"id": "productDetails_detailBullets_sections1"})
    for tbody in temp:
        for tr in tbody:
            data = {}
            count = 0
            th = ''
            td = ''
            for i in tr:
                if count == 0:
                    th = i
                else:
                    td = i
                count+=1
            data[th] = td
            desc.append(data)
                
    print(desc)


    product["title"] = soup.find("span", attrs={"id":'productTitle'}).text.strip()
    print(product["title"])
    temp = soup.find("span", attrs={"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'})
    count = 1
    for i in temp:
        for j in i:
            print(j)
            if count == 3:
                product["price"]=j.text.strip()
            count+=1
    print(product["price"])



    

    # temp = soup.find_all("div", attrs={"class":"a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"})
    # print(temp)


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
                print(temp)
                df = pd.DataFrame([temp])
                # Append the DataFrame to the CSV file
                # df.to_csv("output.csv", mode='a', header=False, index=False)

                
                
        page += 1
        # print(temp[-1])

    # return temp


scrape_amazon_search(input("enter search query"))

# df = pd.DataFrame(newnew)

# Save the DataFrame as a CSV file
# If the file does not exist, it will be created. If it does exist, the new data will be appended without the header.
# df.to_csv("output.csv", mode='a', header=False, index=False)

