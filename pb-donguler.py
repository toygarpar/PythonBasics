# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:02:58 2023

@author: 90530
"""

numbers = [1, 2, 3, 4, 5]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

for num in numbers:
    print(num)
    print("hello")
    
print([num for num in numbers])



names = [ "toygar", "selçuk", "aslı"]

for name in names:
    print(f"my name is {name}")
    #print(name)
    
    
    
name = "toygar par"

for n in name:
    print(n)
    
    
tuple = (1, 2, 3, 4, 5)

for n in tuple:
    print(n)
    
    
tuple2 = [(1, 2), (1, 3),(3, 5), (5, 7)]

for t in tuple2:
    print(t)
    
for a, b in tuple2:
    print(a,b)
    print(a)
    print(b)
    print("***")
    
    
    
dic = { "k1": 1,  "k2" : 2, "k3": 3}

for item in dic:
    print(item)
print("?".center(100, "*"))
   
for item in dic.items():
    print(item)
print("?".center(100, "*"))
    
for key, value in dic.items():
    print(value)
    print(key)
print("?".center(100, "*"))
   
for v in dic.values():
    print(v)
print("?".center(100, "*"))
    
for k in dic.keys():
    print(k)
    
    
#1.alıştırma    
    
numberz = [1, 3, 5, 7 ,9, 12, 19, 21]

#3'ün katları
numberz3 = []
for num in numberz:
    if num % 3 == 0:
        numberz3.append(num)
print(numberz3)

print(numberz)
print([num % 3 ==0 for num in numberz])
print([num for num in numberz if num % 3 ==0])

#alternatif çözüm

for num in numberz:
    if num % 3 == 0:
        print(f"alternatifçözüm: {num}")

#hoca alternatif çözümü
i=0
while i < len(numberz):
    print(numberz[i])
    i += 1









#numberz daki sayıların toplamı
toplam = 0
for num in numberz:
    toplam += num
print(toplam)

toplam = sum(num for num in numberz)
print(toplam)
print(sum(num for num in numberz))




#numberzdaki tek sayıların karesi
teknumberz = []
for num in numberz:
    if num % 2 == 1:
        teknumberz.append(num**2)
        
print(teknumberz)
print([ num**2 for num in numberz if num % 2 == 1])











#sehirler hangileri en fazla 5 karakterli

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

for c in sehirler:
    if len(c) <= 5:
        print(c)
        






#ürün fiyatları toplamı   
        
urunler = [
    { "name" : "samsung s6", "price" : "3000"},
    { "name" : "samsung s7", "price" : "4000"},
    { "name" : "samsung s8", "price" : "5000"},
    { "name" : "samsung s9", "price" : "6000"},
    { "name" : "samsung s10", "price" : "7000"}
    
    ]

toplam = 0

pricevalue=[]
keyz = []

#fiyatları oluşturulan pricevalue listesine ekle
for value in urunler:
   pricevalue.append(value['price'])

print(f"Pricevalue : {pricevalue}")
   
#pricevalue listesindeki fiyatların toplamını al
for num in pricevalue:
    toplam += int(num)
print(f"Listedeki tel fiyatlarının toplamı: {toplam}")
 
#pricevalue listesinde fiyatların 5000 ve aşağısı olanlar   
for value in pricevalue:
    value = int(value)
    if value <= 5000:
        print(value)

#telefon modellerini oluşturulan keyz listesine ekle
keyz = []

for key in urunler:
   keyz.append(key['name'])  
   
print(f"Keyz : {keyz}")
print(f"Pricevalue : {pricevalue}")

#yeni bir dict oluştur ve model ve fiyatları pair yap  
phonepricedict = {}

for key, price in zip(keyz,pricevalue):
    phonepricedict[key] = price
    
    
print(f"Phone-price pair: {phonepricedict}")

#5000 ve asağısı olan modelleri listele
print("5000 ve asağısı olan modeller: ")

for k, v in phonepricedict.items():
    if int(v) <= 5000:
        print(k)

    

#alternatif çözüm
toplamalt = 0
for urun in urunler:
    print(urun["price"])
    
for urun in urunler:
    fiyat = int(urun["price"])
    toplamalt += fiyat
    
print("toplam ürün fiyatları:", toplamalt)

for urun in urunler:
    if int(urun["price"]) <= 5000:
        print(urun["name"])