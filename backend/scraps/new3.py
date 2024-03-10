import requests
from bs4 import BeautifulSoup
import json

results=[]
# base_url = "https://www.flipkart.com/motorola-g34-5g-ocean-green-128-gb/p/itm6b1a33b9d9191?pid=MOBGUFK4TZ2CJYHJ&lid=LSTMOBGUFK4TZ2CJYHJPBUF6M&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_2&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=organic&iid=3228bb11-1177-409c-b140-fefd824d94b9.MOBGUFK4TZ2CJYHJ.SEARCH&ppt=hp&ppn=homepage&ssid=obk18jlji80000001710028372170&qH=eb4af0bf07c16429"

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
        # print(product["about"])

    # review_format = soup.find_all("div", attrs={"class": "col _2wzgFH"})
    # count = 0
    # for i in review_format:
    #     if count == 0:
    #         print(i)
    #     one_review = {}
    #     one_div = i.find("div", attrs={"class": "row"})
    #     for content in one_div:
    #         rating = content.find("div", attrs={"class": "_3LWZlK _1BLPMq"})
    #         if count == 0:
    #             print("\n\n")
    #             print(rating)
    #     count+=1

    product["rating"] = soup.find("div", attrs={"class":'_2d4LTz'}).text.strip()
    # print(product["rating"])

    product["link"] = base_url
    # print(product["link"])

    product["variations"] = [li.text.strip() for li in soup.find_all('li', {'class': 'a-spacing-small item'})]

    product["options"] = [img['src'] for img in soup.find_all('img', {'class': 'imgSwatch'})]

    print(product)
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


    
