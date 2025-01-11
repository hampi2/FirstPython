import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://dometopia.com/goods/search?sort=newlist"
url = "https://dometopia.com/goods/search?sort=all"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

goods_scode = []
goods_name = []
goods_url = []

goods_list = soup.find_all(class_="goodsDisplayItemWrap")


preurl = "https://dometopia.com"
for good in goods_list:
    # print(good.find(class_="goods_scode").text)
    # print(good.find("h6").text)
    # print(preurl + good.find("a")["href"])
    
    goods_scode.append(good.find(class_="goods_scode").text.strip())
    goods_name.append(good.find("h6").text.strip())
    goods_url.append(preurl + good.find("a")["href"].strip())
    
raw_data = {"상품코드":goods_scode, "상품명":goods_name, "상품주소":goods_url}
raw_data = pd.DataFrame(raw_data)
raw_data.to_excel(excel_writer="cobol.xlsx")

print("hello world")





"""
url = "https://dometopia.com/goods/view?no=196901&code=0097"
response = requests.get(url)

# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

name = soup.find(class_ = "pl_name").find("h2").text
# print(name)

price = soup.find(class_ = "price_red").text
price = price.replace(",","").replace("원","")
# print(price)

detailImages = soup.find(class_="detail-img").find("img")["src"]
preurl = "https://dometopia.com"
detailImages = preurl + detailImages
# print(preurl + detailImages)

rawData = {"상품명" : [name],
           "매입가" : [price],
           "상세이미지" : [detailImages]}

rawData = pd.DataFrame(rawData)
rawData.to_excel(excel_writer="sample.xlsx")
"""