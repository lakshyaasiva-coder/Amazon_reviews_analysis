import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
response = requests.get(url)
print(response.status_code)
print(response.text[:300])
soup = BeautifulSoup(response.text,"html.parser")
books = soup.find_all("article", class_="product_pod")
print ("Books Found:\n")
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print("Title:",title)
    print("Price:",price)
    print("----------------")