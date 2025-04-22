
a = int(input("bir sayi girin: "))
b = int(input("ikinci bir sayi girin: "))

if a > b:
    print("fuck yeah")
    print(f"a: {a} b: {b}'den buyuktur")




c = int(input("1.vize puani : "))
d = int(input("ikinci vize puani : "))

final = int(input("final puani : "))

ort =  ((((c + d)/2)*0.6) + (final * 0.4)) 
if ort >= 50:
    print(f"Gecti{ort}, {ort>=50}")
elif ort < 50:
    print(f"Kaldi {ort >=50}")
  
    
  
    
    
e = int(input("bir sayi girin: "))
if e % 2 == 0:
    print("Cift")
else:
    print("Tek")
    


    
f = int(input("bir sayi girin: "))
if f < 0:
    print("negatif")
elif f > 0:
    print("pozitif")
else:
    print("sifir")
 
    
 
    
 
   
email = "abc123" 
password = "toygar.par@gmail.com"
   
    
g = input("parola: ").lower().strip()
h = input("email: ").lower().strip()

isEmail = (email == h)
isPassword = (password == g)

if g == password and h == email:
    
    
    
    print(f"email {isEmail} ve parola {isPassword}")
else:
    print(f"email {isEmail} ve parola {isPassword}")
    
    
    
#mantýksal operatörler 
    
x = 6

result  = 5 < x < 10
print(result)

#and True, True => True

result = x > 5 and x < 10
print(result)

hak = 5
devam  = "e"

r = (hak > 0) and (devam == "e")
print(r)



#or True, False => True
r = (x > 0) or (x < 10) and  (x % 2 == 0)
print(r)





#denemeler



a = float(input("Bir sayý giriniz: "))
isDogru = 0 <= a <=100

if 0 <= a <=100:
    print(f"Girdiðiniz rakam: {a} {isDogru} sifir ile yuz arasýndadýr")
else:
    
    print("no way")
    quit
  
    
#alternatif çözüm

sayi = float(input("sayi:"))
sonuc = (sayi > 0) and (sayi <=100)
print(f"{sayi},  0 ile 100 arasında mı? {sonuc}")






  
    
num = int(input("Bir sayý giriniz: "))

result = num > 0 and num % 2 == 0

print(f" Girdiðiniz rakam {num} bir pozitif çift sayýdýr {result}")





parola = "abc123"
email = "t@p.com"

p = input("Parola girin: ")
e = input("Email girin: ")

result = (p == "abc123" and e == "t@p.com")
isPassword = (p == "abc123")
isEmail = (e == "t@p.com")
print(f" Parola : {isPassword} ve Email : {isEmail}")






x = int(input("1.sayýyý giriniz: "))
y = int(input("2.sayýyý giriniz: "))
z = int(input("3.sayýyý giriniz: "))

liste = [x , y, z]
maxi = max(liste)
mini = min(liste)
liste.sort()
orta = liste[1]

print(f"{maxi} > {orta} > {mini}")

#alternatif çözüm

a = int(input("1.sayýyý giriniz: "))
b = int(input("2.sayýyý giriniz: "))
c = int(input("3.sayýyý giriniz: "))

result = (a > b) and (a > c)
print(f" a en buyuk sayidir : {result}")

result = (b > a) and (b > c)
print(f" b en buyuk sayidir : {result}")

result = (c > b) and (c > a)
print(f" c en buyuk sayidir : {result}")









c = int(input("1.vize puani : "))
d = int(input("ikinci vize puani : "))
final = int(input("final puani : "))

ort =  ((((c + d)/2)*0.6) + (final * 0.4)) 
if ort >= 50 and final>=50:
    print(f"Gecti {ort}, {ort>=50}")
elif final >= 70:
    print(f"Gecti{final}, Ortalama  {ort>=50}")
elif ort < 50:
    print(f"Kaldi {ort >=50}")
    
   
#alternatif 
   
c = int(input("1.vize puani : "))
d = int(input("ikinci vize puani : "))
final = int(input("final puani : "))


ort =  ((((c + d)/2)*0.6) + (final * 0.4)) 
result = (ort >= 50 or final>=70) and final>=50


print(f" öğrenci ortalaması:{ort} ve geçme durumu:{result}")
   

   
    
   
    
   
    
    
    
    
ad = input("Isim giriniz: ")
kilo = float(input("kilonuzu girin: "))
boy = float(input("boyunuzu giriniz: "))

formula = kilo / (boy ** 2)
print(formula)

match formula:
    case x if  0 <= x <= 18.4:
        print(f"Sevgili {ad} , Zayifsin")
    case x if 18.5 <= x <=24.5: 
        print(f"Sevgili {ad} , Normalsin")
    case x if  25.0 <= x <=29.9: 
        print(f"Sevgili {ad} , Fazla Kilolusun")
    case x if 30.0 <= x <=34.9: 
        print(f"Sevgili {ad} , You are an obese fat fuck!")
              
        
        
"""
By assigning the value of formula to x in each case,
 you can compare it with the specified ranges. 
 This way, the match statement will correctly evaluate
 the value of formula within each specified range 
 and print the corresponding message.
"""



x =  y = [1, 2, 3]

z = [1, 2, 3]
              
print(x == y)  
print(x == z)  
print(x is y)  
print(x is z)



x  = [1, 2, 3]
y = [2, 4]
print(x is y)

del x[2]
y[1] = 1 
y.reverse()

print( x == y )
print(x is y)
print(x is not y)


x = ["apple" , "banana"]
print("banana" in x)




















































































