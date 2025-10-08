import requests 
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/index.html"
response = requests.get(url)
# print(response.text)

status_code = response.status_code
if status_code == 200:
    print('Ok')
elif status_code == 404:
    print('Not Found')
elif status_code == 403:
    print("Forbidden")
else:
    print('Internal Server Error')


# for i in range(1, 51):
#     a = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
#     with open(f'Page-{i}.html', 'w', encoding='utf-8') as f:
#         f.write(a.text)
#         print(f"Page {i} Downloded!")

with open('Page-1.html', 'r') as f:
    content = f.read()
    
soup = BeautifulSoup(content, 'html.parser')

articles = soup.select("article.product_pod")

items = []
for article in articles:
    title = article.find('h3').find('a')['title']
    price = article.select_one('p.price_color').text.split('Â')[1]
    rating = article.select_one('p.star-rating')['class'][1]
    items.append([title, price, rating])

import pandas as pd

data = pd.DataFrame(items, columns=['Title', 'Price', 'Rating'])

data.to_csv('data.csv', index=False)