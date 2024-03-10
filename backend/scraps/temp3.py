import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import numpy as np

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

def scrape_flipkart_search():
    products=[]
    query = input("Enter the search query: ")
    base_url = "https://www.flipkart.com/search"
    params = {"q": query}

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    print(response)

    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)
    search_results = soup.find_all("div", {"class": "_1AtVbE"})

    counter = 0  # Counter to keep track of non-advertisement products
    results = []

    for result in search_results:
        print(result)
        if counter >= 10:
            break  # Stop iterating once 5 non-advertisement products are found

        # if result.find("div", class_=["_1xHGtK _373qXS", "_4ddWXP"]):
        inner_products = result.find_all("div", class_=["_1xHGtK _373qXS", "_4ddWXP"])
        print(inner_products)

        for inner_product in inner_products:
            
            ad_flag_inner = inner_product.find("div", class_=["_2I5qvP", "_4HTuuX"])

            if not ad_flag_inner:  # Check if the inner product is an advertisement
                title_element_inner = inner_product.find("a", class_=["IRpwTa", "s1Q9rs"])
                if not title_element_inner:
                    continue
                href_element_inner = inner_product.find("a", class_=["_2UzuFa", "s1Q9rs"])
                if not href_element_inner:
                    continue
                print("href")
                href_inner = urljoin("https://www.flipkart.com", href_element_inner["href"])

                temp = inner_page_details(href_inner)

                rating_element = result.find("div", class_=["_3LWZlK _1rdVr6 _1BLPMq", "_3LWZlK _1BLPMq", "_3LWZlK _32lA32 _1BLPMq", "_3LWZlK"])
                if rating_element:
                    rating = rating_element.text.strip()
                else:
                    continue

                temp['rating']=rating
                print(temp)
                products.append(temp)

                counter += 1

    df = pd.DataFrame(products)
    print(df)


def inner_page_details(base_url):

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response = requests.get(base_url, headers=user_agent)
    soup = BeautifulSoup(response.content, "html.parser")
    print(response)

    product={}
    product['website']="flipkart"
    # print(product["website"])

    product["title"] = soup.find("span", attrs={"class":'B_NuCI'}).text.strip()
    # print(product["title"])

    price_list = []
    price_element = soup.find("div", {"class": "_30jeq3"})
    product["price"] = price_element.text.strip()
    # print(product["price"])


    discount_element = soup.find("div", attrs={"class": "_3Ay6Sb _31Dcoz"})
    for i in discount_element:
        product["discount"] = i.text.strip()
    # print(product["discount"])


    cut_price_element = soup.find("div", {"class": "_3I9_wc _2p6lqe"})
    if cut_price_element:
        product["cut_price"] = cut_price_element.text.strip()
    # print(product["cut_price"])

    product_images = []
    product_imgs = soup.find_all("li", attrs={"class": "_20Gt85 _1Y_A6W"})
    for i in product_imgs:
        for j in i:
            for k in j:
                for l in k:
                    product_images.append(l['src'])
    product["images"] = product_images
    # print(product["images"])

    titles = []
    title_elements = soup.find_all("div", attrs={"class": "flxcaE"})
    for div in title_elements:
        titles.append(div.text.strip())
    product["description_titles"] = titles
    # print(product["description_titles"])

    tables = soup.find_all("table", class_="_14cfVK")
    table_data_list = []
    for table in tables:
        table_data = {}
        rows = table.find_all("tr")
        for row in rows:
            headers = row.find_all("td", class_="_1hKmbr")
            values = row.find_all("li", class_="_21lJbe")
            if headers and values:
                table_data[headers[0].text.strip()] = values[0].text.strip()
        table_data_list.append(table_data)
    product["description_info"] = json.dumps(table_data_list, indent=2)
    # print(product["description_info"])

    desc_div = soup.find("div", {"class":"_1mXcCf RmoJUa"})
    for i in desc_div:
        product["about"] = i.text.strip()


    product["rating"] = soup.find("div", attrs={"class":'_2d4LTz'}).text.strip()
    # print(product["rating"])

    product["link"] = base_url
    # print(product["link"])

    product["variations"] = [li.text.strip() for li in soup.find_all('li', {'class': 'a-spacing-small item'})]

    product["options"] = [img['src'] for img in soup.find_all('img', {'class': 'imgSwatch'})]

    # print(product)
    return product


scrape_flipkart_search()