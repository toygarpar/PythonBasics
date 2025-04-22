html_doc = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfası</title>
</head>
<body>
<h1 id ="header">
        Python Kursu

    </h1>
        <div class="grup1">
            <h2>Programlama</h2>
            
            <ul>
                <li>Menu 1    </li>
                <li>Menu 2    </li>
                <li>Menu 3    </li>
            </ul>
        </div>

        <div class="grup2">
            <h2>Modüller</h2>
            
            <ul>
                <li>Menu 1    </li>
                <li>Menu 2    </li>
                <li>Menu 3    </li>
            </ul>
        </div>
        
        <div class="grup3">
           <h2>Django</h2>
           
           <ul>
               <li>Menu 1    </li>
               <li>Menu 2    </li>
               <li>Menu 3    </li>
           </ul>
       </div>

        <img src="deneme.jpg" alt="">
</body>
</html>

"""

from bs4 import BeautifulSoup


soup = BeautifulSoup(html_doc, "html.parser")


#html'yi düzeltir düzenler güzelleştirir
result = soup.prettify()

result = soup.title

print(result)


result1 = soup.head
print(result1)


result2 = soup.body
print(result2)



res1 = soup.title.name
print(res1)

res2 =  soup.title.string
print(res2)

res3 = soup.h1
print(res3)

res4 = soup.h2.name
print(res4)

res5 = soup.h2.string
print(res5)


res6 = soup.find_all("h2")
print(res6)

res7 = soup.find_all("h2")[0] # sıfırıncı indexteki elemanı almak istesem
print(res7)


res8 = soup.find_all("h2")[1]
print(res8)



res9 = soup.div #○ilk divi bulur
print(res9)


res10 = soup.find_all("div") #bütün divlere erişim
print(res10)

res11 = soup.find_all("div")[1]
print(res11)


res12 = soup.find_all("div")[1].ul  #divin alt etiketi ul'e erişim için
print(res12)

res13 = soup.find_all("div")[1].ul.li #ul etiketinin içerisindeki li'ye ulaşmak
print(res13)


res14 = soup.find_all("div")[1].ul.find_all("li")  #bütünli'lere erişim
print(res14)


#findChildren
res15 = soup.div.findChildren() #bütün elemanlar gelsin istiyorsak
print(res15)


res9 = soup.div #○ilk divi bulur
print(res9)


res16 = soup.div.next
print(res16)







































































































