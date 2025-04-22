import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

html = requests.get(url, headers=headers).content

soup = BeautifulSoup(html, "html.parser")


liste = soup.find("ul", {"class": "ipc-metadata-list" })


print(liste)


liste1 = soup.find("ul", {"class": "ipc-metadata-list" }).find_all("li") #bize burada döngü ile ulaşabileceğimiz bir liste elemanı geliyor
print(liste1)

lis1 = soup.find("ul", {"class": "ipc-metadata-list" }).find_all("li", limit = 1)
print(lis1)

for item in lis1:
    filmadi = item.find("h3", {"class": "ipc-title__text"})
    print(filmadi)
    
for item in liste1:
    filmadi1 = item.find("h3", {"class": "ipc-title__text"})
    print(filmadi1)    
    
for item in liste1:
    filmadi1 = item.find("h3", {"class": "ipc-title__text"}).string
    print(filmadi1)    
        
    
for item in liste1:
    filmadi1 = item.find("h3", {"class": "ipc-title__text"}).text
    print(filmadi1)  
    puan = item.find("span", {"class": "ipc-rating-star"}).text
    print(puan)


for item in liste1:
    filmadi1 = item.find("h3", {"class": "ipc-title__text"}).text
     
    puan = item.find("span", {"class": "ipc-rating-star"}).text
    print(filmadi1, puan)
  