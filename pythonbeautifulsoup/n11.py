import requests
from bs4 import BeautifulSoup


url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}


html = requests.get(url, headers = headers).content
soup = BeautifulSoup(html, "html.parser")


liste = soup.find_all("li", {"class": "column"}, limit = 1)

print(liste)

for li in liste:
    pname = li.a.get("title")
    print(pname)



liste = soup.find_all("li", {"class": "column"})

for li in liste:
    link = li.a.get("href")
    print(link)


for li in liste:
    p_name = li.a.h3.text
    
    print(p_name)
    
count = 1
for li in liste:
    link = li.a.get("href")
    p_name = li.a.h3.text
    images = li.find("img", {"class": "cardImage"}).get("data-images").split(",")[::-1]
    fiyat =  li.find("div", {"class": "priceContainer"}).find_all("span")[-1].ins.text.strip("TL")

    
    print(f'{count}. ***{link}***\n\n+++{p_name}+++\n\n*****{images}*****\n\n------{fiyat}-------\n\n\n')
    count += 1
    

print(liste)
