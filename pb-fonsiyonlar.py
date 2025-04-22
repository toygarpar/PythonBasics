#matematiksel işlemler

def kareal(x):
    print(x**2)
    
kareal(5)    



def kareal(x):
    print("Girilen Sayının Karesi:", x**2)
    print("Girilen Sayının Karesi:" + str( x**2 ))
    print("Girilen Sayı: " + str(x) + ", Karesi: " + str( x**2 ))
    
kareal(5)    


def carpma(x, y):
    print(f" {x} çarpı {y} eşittir {x*y}")
    
carpma(3, 5)    
    
#ısı , nem, şarj

def direkhesap(isi, nem, sarj):
   print( (isi+nem)/sarj)
   
direkhesap(25,40,70)


#gçıktıyı girdi olarak kullanmak


def direkhesap(isi, nem, sarj):
   return (isi+nem)/sarj
   
çikti = direkhesap(25,40,70)



#local and global variables


x = 10

y = 20

def carpma(x, y):
    return x*y


carpma(2,3)

#local etki alanından global etki alanını değiştirmek

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    
eleman_ekle("ali")    


#method

list = [1, 2, 3]

list.append(4)

print(list)
print(type(list))

myString = "Hello"

myString.upper()

print(myString)
print(type(myString))


#fonsiyonlar

def sayHello():
    print("Hello")
    
sayHello()   



def sayHello(name="user"):
    print("Hello " + name )
    
sayHello("ali")   
sayHello()


def sayHello(name="user"):
    return ("Hello " + name )

msg = sayHello("Toygar")
print(msg)



def total(num1, num2):
    return num1 + num2

result = total(10,20)
print(result)


def yasHesapla(dogumYili):
    return 2023 -dogumYili

ageMolly = yasHesapla(1989)
print(ageMolly)
ageHolly = yasHesapla(1999)
ageJolly = yasHesapla(2009)
print(ageMolly, ageHolly,ageJolly)



def yearsToRetirement(dogumYili, isim):
    '''
    DOCSTRING: doğum yılınıza göre emekliliğinize kaç yıl kaldı.
                  

    INPUT: Parameters
    ----------
    dogumYili : int
    isim : str

    OUTPUT:
    -------
    hesaplanan yıl bilgisi

    '''
    age = yasHesapla(dogumYili)
    retirementYearsLeft = 65 - age
    
    if retirementYearsLeft > 0:
        print(f"Sevgili {isim} Emekliliğinize {retirementYearsLeft} yıl kaldı")
    else:
        print(f"Hey Bunak {isim}, zaten emeklisin!")
        
yearsToRetirement(1983, "ali")    
yearsToRetirement(1950, "ahmet")
yearsToRetirement(1974, "Yağmur")    


print(help(yearsToRetirement))


#True or False
border = 5000


print(border == 4000)


#fonkparametreler

def changeName(n):
    n = "Toygar"
    
name = "ali"

changeName(name)
print(name)    


def change(n):
    n[0] = "istanbul"
    
sehirler = ["ankara", "izmir"]

n = sehirler[:]

    

print(sehirler)
print(n)

change(sehirler[:])
print(sehirler)



def add(a,b, c = 0, d=0, e=0):
    return sum((a,b,c))

print(add(10,20))
print(add(10,20, 30))

def add(a,b, c = 0, d=0, e=0):
    return sum([a,b,c])

print(add(10,20))
print(add(10,20, 30))



def add(*params):
    print(params)
    return sum((params))

print(add(10,20))
print(add(10,20, 30))



def add(*params):
    print(params[0])
    print(params[2])
    return sum((params))

print(add(10,20, 30))
print(add(10,20, 30, 40, 50, 60))



def add(*params):
    sum  = 0
    
    for n in params:
        sum += n
    return sum


print(add(10,20, 30, 40, 50, 60))







def displayUser(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key,value))

displayUser(name = "ali", age = 2, city = "istanbul")
displayUser(name = "veli", age = 12, city = "karabük", phone= "1234567")
displayUser(name = "deli", age = 22, city = "ypzgat", phone= "1234568", email="deli@mad.com")




def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
myfunc(10 ,20 ,30, 40 ,50, key1="value1", key2 = "value2")    






kelime = input("Göndermek istediğiniz kelime: ")
howmany = int(input("Kaç kez ekranda gösterilsin? "))
 


def repeat():
   
    print((kelime + " ") * howmany )



repeat()



listem = []

def cevir(a, b, c, *args,**kwargs):
    listem.append(a)
    listem.append(b)
    listem.append(c)
    listem.append(args)
    listem.append(kwargs)
    print(listem)
    
cevir(1, 2, 3, 50, 60, 70, action="fuck", who="you")    





def listeyeCevir(*params):
    
    liste = []
    
    for param in params:
        liste.append(param)
        
    return liste

result = listeyeCevir(10, 30 ,20 , "merhaba")
print(result)





#asal sayıların bulan custom fonksiypnlar



def main():
    num1 = int(input("1. Sayıyı giriniz: "))
    num2 = int(input("2. Sayıyı giriniz: "))
    asalbul(num1, num2)
    print(asalbul(num1, num2))
    
   


def asalbul(num1, num2):
    
    asallist = []
    


    for i in range (num1, num2+1):
        
        if i > 1:
            for j in range(2, i):# 2'den itibaren döngümüzdeki sayıya kadar böleni var mı?
                if i % j == 0:
                    break
            else: 
                asallist.append(i)
                
    
    return asallist


main()




#asal sayı bul

num1 = int(input("1. Sayıyı giriniz: "))
num2 = int(input("2. Sayıyı giriniz: "))

#list comprehension ile çözüm
for i in range(num1, num2+1):
    if all([(i % j) for j in range(2, i)]):
        print(i,"is a prime number")
#*************************************************

for i in range(num1, num2+1):
    
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else: 
            print(i)
                
    
    

#sadıkturan asalsayı bul örneği

def asalSayılariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

asalSayılariBul(sayi1, sayi2)




#tam bölenleri bul ve listele


def tambolen(num):
    tambolenler = []

    for i in range(2, num):
        if num % i == 0:
            tambolenler.append(i)
            
    return tambolenler


print(tambolen(20))






def main():
    num1 = int(input("1. Sayıyı giriniz: "))
    num2 = int(input("2. Sayıyı giriniz: "))
    
    #check for every number from num1 to num2
    for i in range(num1,num2+1):
      #check if current number is prime
        if(isPrime(i)):
            print(i,end=" ")
    



#function to check if a given number is prime
def isPrime(n):
  #since 0 and 1 is not prime return false.
    if(n==1 or n==0):  return False
   
  #Run a loop from 2 to n-1
    for i in range(2,n):
    #if the number is divisible by i, then n is not a prime number.
        if(n%i==0):
            return False
   
  #otherwise, n is prime number.
    return True
 
main()
 
 
 
 

        
        


for i in range(2, 101):
    if i > 1: # Prime numbers are greater than 1
        for j in range(2, i):
            if (i % j) == 0:
                print(i,"is a composite number")
                break
        else:
            print(i,"is a prime number")
            
            
for i in range(2, 101):
    if all([(i % j) for j in range(2, i)]):
        print(i,"is a prime number")      
        
        
        
        
   #lambda 

     
        
 
def square(num):  return num ** 2        

numbers  =[1, 3, 5, 9]

result =  square(2)
print(result)
        
        


result = list(map( square, numbers))
print(result)
        
        
for item in map(square, numbers):
    print(item)
    
    
result = list(map( lambda num: num ** 2, numbers))
print(result)    



#belirli bir serideki değerleri fonsiyonu gönderip belirli bir koşulu sağlayanları FİLTER edelim


numbers  =[1, 3, 5, 9, 10, 4, 6, 8]

def checkeven(num):
    return num % 2 == 0

result = list(filter(checkeven, numbers))
print(result)

print(list(filter(lambda num : num % 2 ==0, numbers)))




#global scope
x = "global x"

def fonk():
    #local scope
    x = "local x"
    print(x)
    
fonk()
print(x)

 ####################

#global
name = "Toygar"

def changeName(new_name):
    #local
    name = new_name
    print(name)
    
    
changeName("Selcuk") 
print(name)   
  


##################


name = "global string"

def greeting():
    name = "Selcuk"
    
    def hello():
        name = "Mülo"
        print("Hello " + name)
        
    hello()
    
    
greeting()    





######################


x = 50

def test(x):
    print(f"x: {x}")
    
    
    x = 100
    print(f"changed x to {x}" )
  
test(x)
print(x)




#bankamatik uygulaması


toygarHesap = {
    "ad" : "Toygar Par",
    "hesapNo" : "12345678",
    "bakiye" : 3000,
    "ekhesap" : 2000
    
    }
  

selcukHesap = {
    "ad" : "Selçuk Dönmez",
    "hesapNo" : "12345679",
    "bakiye" : 2000,
    "ekhesap" : 1000
    
    }



def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] +  hesap["ekhesap"]
        
        if toplam >= miktar:
            ekHesapKullan = input("Ek hesap kullanılsın mı?  (e/h)")
            
            if ekHesapKullan == "e":
                
                ekhesapNeeded = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekhesap"] -= ekhesapNeeded
                
                print("Paranızı alabilirsiniz")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} numaralı hesabınızda {hesap['bakiye']} bulunmaktadır.")
                
                
        else: 
            print("Üzgünüz ,bakiyeniz yetersiz")
                
    
def bakiyeSorgula(hesap):
    print(f" {hesap['hesapNo']} numaralı hesabınızda {hesap['bakiye']} TL bulunmaktadır")   
    print(f" Ek hesap limitinizde {hesap['ekhesap']}  TL bulunmaktadır") 
    
    
paraCek(toygarHesap, 3000)  

print("*************************************")

paraCek(toygarHesap, 2000)     



















































    