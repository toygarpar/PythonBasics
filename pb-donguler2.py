
#while

listem = []

x = 0

while x < 100:
    listem.append(x)
    x += 1
    
print("bitti", listem)


#sadece çift sayılar

y = 0

while y < 100:
    if y % 2 == 0:
        print(f" sayı çift : {y}")
    else:
        print(f"sayı tek: {y}")
    y += 1
    
print("bitti")



name  = ""

while not name.strip():
    name = input("İsminizi girin: ")
    
print(f"Merhaba {name}")




#alıştırmalar

#while loop ile listeyi yazdır
numbers= [1, 3, 5, 7, 9, 12, 19, 21]

x = 0

while x < 22:
    print(x) if x in numbers else print("failed")
    x += 1
    
    
x = 0
while x < 22:
    if x in numbers:
        print(x)
    else:
        pass
    x +=1
    
#alternatif çözümler

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
    
for i in numbers:
    print(i)
        
    
    
    
    
#başlangıç ve bitiş değerleri kullanıcıdan alıp ekrana yazıdırn   
    
    
a = int(input("Bir sayı girin: "))
b = int(input("İkinci bir sayı girin: "))

# while a < b:
#     for x in range(a,b):
#         print(x) if x % 2 == 1 else print("çift")
#         a += 1
        
        
while a < b:
    for x in range(a,b):
        if x % 2 == 1:
            print(x)  
        a += 1
        
#alternatif çözüm


ba = int(input("Bir sayı girin: "))
bi = int(input("İkinci bir sayı girin: "))

i = ba
while i < bi:
    i +=1
    if i % 2 == 1:
        print(i)  

    





#1-100 arasında sayılarak azalarak yazdrın     
        
        
z = 100

while z > 0:
    print(z)
    z -=1
    
    
#kullanıcıdan aldığınız 5 sayıyı ekrana sıralı yazdırın  
x = 0    
y = list()  
while x < 5:
    user = int(input("Sayı giriniz:"))
    y.append(user)
    x += 1
 
y.sort()
print(y)    
print([num for num in y])
    

#alternatif ama burada while loop yok
x1 = int(input("Sayı 1: "))
x2 = int(input("Sayı 2: "))
x3 = int(input("Sayı 3: "))
x4 = int(input("Sayı 4: "))
x5 = int(input("Sayı 5: "))

listem1 = [ x1, x2, x3, x4, x5]
listem1 = sorted(listem1)

print(listem1)






#kullanıcıdan aldığınız urun bilgilerini urunler listesinde saklayın
#urun sayısını kulanıcı belirlesin
#dict yapısı (name,price) olsun
#while ile urun listesini yazdırın

urunler = []
toplammiktar = 0
miktar = int(input("Ürün sayısı girin: "))

products = []
fiyatlar = []




while toplammiktar in range( miktar):
    name = input("Ürün adı girin: ")
    price = int(input("fiyat girin: "))
    products.append(name)
    fiyatlar.append(price)

         
        

        
    toplammiktar += 1

print(products)
print(fiyatlar)
    
urunler = {}  
for name, price in zip(products,fiyatlar):
    urunler[name] = price
    
    
print(f"ürün - fiyat listesi: {urunler}")

print(urunler)

for name, price in urunler.items():
    print(name)
    
k = 1
    
while k > 0:

    for name in urunler.keys():
        print(name)

    k -= 1




#alternatif çözüm

urunler = []

adet = input("kaç ürün eklemek istiyorsunuz? ")
adet =int(adet)

i=0

while i < adet:
    name = input("ürün ismi: ")
    price = input("ürün fiyatı: ")
    urunler.append({
        "name" : name,
        "price" : price
        
        
        })
    i += 1
    
    
for urun in urunler:
    print(f'ürün adı : {urun["name"]} , ürün fiyatı : {urun["price"]}')
    















    