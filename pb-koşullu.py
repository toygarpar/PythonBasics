if 3>2:
    print("Welcome")

if True:
    print("Welcome")
    

username = "toygarpar"
password = "1234"


if username == "toygarpar":
    if password == "1234":
        print("welcome")
    else:
        print("Parola Yanlış")
else:
    print("username  yanlış")
    
    
    
    
x = int(input("x gir: "))

y = int(input("y gir "))

if x > y:
    print("x y'den büyük")
elif y == x:
    print(" x y eşit")
else:
    print("y x'den büyük")
    
    
    
    
num = int(input("Sayı: "))

if num > 0:
    print("Sayı pozitif")
elif num < 0:
    print("sayı negatif")
else:
    print("sayı sıfır")



#5-3-1 ehliyet uygulaması


isim = input("Adınızı girin: ")
edu = input("Eğitim Durumunuz: ")
age = int(input("yaşınızı girin: "))


if age >= 18:
    if edu == "lise" or edu=="üniversite":
        print(f"Sevgili {isim}, Ehliyet alma koşullarını karşışıyorsunuz.")
    else:
        print("Eğitim durumunuz ehliyet almaya uygun değil!")
else:
    print("Yaşınız küçük")
    
    
    
    
    
    

c = float(input("1.vize puani : "))
d = float(input("ikinci vize puani : "))
final = float(input("final puani : "))


ort =  ((((c + d)/2)*0.6) + (final * 0.4)) 



result = (ort >= 50 or final>=70) and final>=50


match ort:
    case x if  0 <= x <= 24:
        print(f"Not: 0, Geçme Durumu: {result}")
    case x if 25 <= x <=44: 
        print(f"Not: 1, Geçme Durumu: {result}")
    case x if  45 <= x <=54: 
        print(f"Not: 2, Geçme Durumu: {result}")
    case x if 55 <= x <=69: 
        print(f"Not: 3, Geçme Durumu: {result}")
    case x if 70 <= x <=84: 
        print(f"Not: 4, Geçme Durumu: {result}")
    case x if 85 <= x <=100: 
        print(f"Not: 5, Geçme Durumu: {result}")
    case _: 
        print("Yanlış bilgi girdiniz!")

print(f" öğrenci ortalaması:{ort} ve geçme durumu:{result}")


#araç bakım zamanları


import datetime
from datetime import date
ilk = input("Trafiği çıkış tarihi giriniz(örnek: '20200322'): ")
trafik = date.fromisoformat(ilk)


simdi = date.today()
print(f"bugün {simdi}")

fark = datetime.timedelta(days=365)
fark2 = datetime.timedelta(days=730)
fark3 = datetime.timedelta(days=1095)

if simdi >= trafik + fark3 :
    print("3. yıl Bakımı")
elif simdi >= trafik + fark2:
    print("2. yıl Bakımı")
elif simdi >= trafik + fark :
    print("1. yıl Bakımı")
else:
    print("hatalı süre bilgisi")
    

#alternatif

days  = int(input("aracınız kaç gündür trafikte: "))

if days <=365:
    print("1.servis aralığı")
elif 365 < days <= 365*2:
    print("2. servis aralığı")
elif 365*2 < days < 365 *3:
    print("3. servis aralığı")
else:
    print("hatalı süre bilgisi")
    
  
#alternatif 2    
    
    
import datetime

tarih  = input("aracınız kaç gündür trafikte ör:(2019/8/9): ")
tarih = tarih.split("/")
print(tarih[0])
print(tarih[1])
print(tarih[2])


trafigeCıkıs = datetime.datetime(int(tarih[0]), int(tarih[1]),int(tarih[2]))
print(f"Trafiğe çıkış zamanı: {trafigeCıkıs}")
simdik = datetime.datetime.now()
print(f"şu anki zaman: {simdik}")
fark = simdik - trafigeCıkıs
print(f"zaman farkı {fark}")
dayz = fark.days
print(dayz)

if dayz <=365:
    print("1.servis aralığı")
elif 365 < dayz <= 365*2:
    print("2. servis aralığı")
elif 365*2 < dayz < 365 *3:
    print("3. servis aralığı")
else:
    print("hatalı süre bilgisi")
    
    
    
    
    
#girilen bir sayının 0-100 arasında olup olmadığı

a = float(input("Bir sayý giriniz: "))
isDogru = 0 <= a <=100

if 0 <= a <=100:
    print(f"Girdiðiniz rakam: {a} {isDogru} sifir ile yuz arasýndadýr")
    
else:
    
    print("no way, sayı 0-100 arasında değildir")
    quit
    
    
    
#girilen sayının pozitif çift sayı olup olmadığı

num = int(input("Bir sayý giriniz: "))

if num > 0:
    print(f"Girilen sayı pozitif: {num}")
    if num % 2 == 0:
        print(f" Girdiðiniz rakam {num} bir pozitif çift sayýdýr ")
    else:
        print(f"Girdiğiniz sayı çift sayı değil: {num}")
else:
    print(f"Girdiğiniz sayı pozitif sayı değil, negatif: {num}")
    
    
    
    
#girilen email ve parola bilgilerini kontrol ediniz

u = input("Email giriniz: ")
p = input("password giriniz: ")
usermail = "toygar@par"
password = "1234"


if usermail == u:
    if password == p:
        print("welcome")
    else:
        print("Parola Yanlış")
else:
    print("usermail  yanlış")
    
    
    
#girilen 3 sayıyı büyüklük olarak karşılaştırınız



a = int(input("1.sayýyý giriniz: "))
b = int(input("2.sayýyý giriniz: "))
c = int(input("3.sayýyý giriniz: "))

result1 = (a > b) and (a > c)


result2 = (b > a) and (b > c)


result3 = (c > b) and (c > a)





if (a > b) and (a > c):
    print(f" a en buyuk sayidir : {result1}")

elif (b > a) and (b > c):
    print(f" b en buyuk sayidir : {result2}")

elif (c > b) and (c > a):
    print(f" c en buyuk sayidir : {result3}")
else: 
    print("Hep sıfır mı girdin mofo?")
    


liste = [a , b, c]
maxi = max(liste)
mini = min(liste)
liste.sort()
orta = liste[1]

print(f"{maxi} > {orta} > {mini}")





#body mass index

ad = input("Isim giriniz: ")
kilo = float(input("kilonuzu girin: "))
boy = float(input("boyunuzu giriniz: "))

formula = kilo / (boy ** 2)
print(formula)

match formula:
    case x if  0 <= x <= 18.4:
        print(f"Sevgili {ad} , Zayifsin: {formula:.2f}")
    case x if 18.5 <= x <=24.5: 
        print(f"Sevgili {ad} , Normalsin: {formula:.2f}")
    case x if  25.0 <= x <=29.9: 
        print(f"Sevgili {ad} , Fazla Kilolusun: {formula:.2f}")
    case x if 30.0 <= x <=34.9: 
        print(f"Sevgili {ad} , You are an obese fat fuck!: {formula:.2f}")
    case _:
        print("Pufuduksun")
        
        
        