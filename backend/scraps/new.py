import requests
from bs4 import BeautifulSoup
import csv

# URL of the product page
# url = "https://www.flipkart.com/search?q=product"
url = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRW8IBDX&marketplace=FLIPKART&q=apple+iphone+xs+max+space+grey+64+gb&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_32_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_32_na_na_na&fm=SEARCH&iid=fcd6a03b-0177-4f77-94d5-780aa44f40e8.MOBF944E5FTGHNCR.SEARCH&ppt=pp&ppn=pp&ssid=a1fttejke80000001709968284693&qH=4fe363f19e7238a6"

# Send a GET request
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Open the CSV file in write mode
with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write the headers to the CSV file
    writer.writerow(["Title", "Price", "Image", "Discount", "About", "Rating", "Link", "Reviews", "Description", "Table"])

    # Find all product elements on the page
    products = soup.find_all("div", {"class": "_2kHMtA"})

    # Loop over each product element
    for product in products:
        # Extract the product details
        title = product.find("a", {"class": "_16Jk6d"}).text
        price = product.find("div", {"class": "_30jeq3 _1_WHN1"}).text
        img = product.find("img", {"class": "_396cs4 _3exPp9"}).get("src")
        discount = product.find("div", {"class": "_3Ay6Sb"}).text
        about = product.find("a", {"class": "IRpwTa"}).get("title")
        rating = product.find("div", {"class": "_3LWZlK"}).text
        link = product.find("a", {"class": "IRpwTa"}).get("href")
        reviews = product.find("span", {"class": "_2_R_DZ"}).text
        description = product.find("ul", {"class": "_1xgFaf"}).text
        table = product.find("div", {"class": "_3k-BhJ"}).text
        
        

        # Write the product details to the CSV file
        writer.writerow([title, price, img, discount, about, rating, link, reviews, description, table])
        
def get_title(soup):
    try:
        title = soup.find("a", {"class": "_16Jk6d"}).text.strip()
    except AttributeError:
        title = ""
    return title

def get_price(soup):
    try:
        price = soup.find("div", {"class": "_30jeq3 _1_WHN1"}).text.strip()
    except AttributeError:
        price = ""
    return price

def get_img(soup):
    try:
        img = soup.find("img", {"class": "_396cs4 _3exPp9"}).get("src")
    except AttributeError:
        img = ""
    return img

def get_discount(soup):
    try:
        discount = soup.find("div", {"class": "_3Ay6Sb"}).text.strip()
    except AttributeError:
        discount = ""
    return discount

def get_about(soup):
    try:
        about = soup.find("a", {"class": "IRpwTa"}).get("title")
    except AttributeError:
        about = ""
    return about

def get_rating(soup):
    try:
        rating = soup.find("div", {"class": "_3LWZlK"}).text.strip()
    except AttributeError:
        rating = ""
    return rating

def get_link(soup):
    try:
        link = soup.find("a", {"class": "IRpwTa"}).get("href")
    except AttributeError:
        link = ""
    return link

def get_reviews(soup):
    try:
        reviews = soup.find("span", {"class": "_2_R_DZ"}).text.strip()
    except AttributeError:
        reviews = ""
    return reviews

def get_description(soup):
    try:
        description = soup.find("ul", {"class": "_1xgFaf"}).text.strip()
    except AttributeError:
        description = ""
    return description

def get_table(soup):
    try:
        table = soup.find("div", {"class": "_3k-BhJ"}).text.strip()
    except AttributeError:
        table = ""
    return table


    print(title)