def greeting(name):
    print("hello", name)
    
print(greeting("ali"))
print(greeting)    


sayHello = greeting 

print(sayHello)
print(greeting)

del sayHello
print(greeting)
#print(sayHello)



def loud(text):
   return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)




#encapsulation
def outer(num1):
    print("outer")
    
    def inner_increment(num1):
        print("inner")
        return num1 + 1 
    
    num2 = inner_increment(num1) #◙ inner fonksiyonun çalışması için outer fonksiyounu içinden inner'i çağırmamız gerekir
    print(num1, num2)
    
outer(10)    
print("****************")
print(outer(10))    

#inner_increment(10)  name error verir, sadece outer kapsamında çalışır



def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
        
    if not number >=0:
        raise ValueError("number must be zero or positive")
    
    
    def inner_factorial(number):
        if number <= 1:
            return 1 
        
        return number * inner_factorial(number - 1)
    
    return inner_factorial(number)



try:
    print(factorial(5))
    
except Exception as ex:
    print(ex)







# fonksiyondan fonsiyon döndürme


def power(number):
    
    
    
    def inner(us):
        return number**us
    
    return inner


two = power(2)
print(two(3))
three = power(3)
print(three(3))
print(power(3))




def yetki_sorgula(page):
    
    def inner(role):
        if role == "admin":
            return"{0} rolü {1} sayfasına ulaşabilir".format(role, page)
        else:
            return"{0} rolü {1} sayfasına ulaşamaz".format(role, page)
        
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("admin"))






def islem(islem_adı):
    
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
            
        return toplam
    
    def carpma(*args):
       
        carpim = 1
        for i in args:
            carpim *=i
            
        return carpim
    
    
    if islem_adı == "toplama":
        return toplam 
    else:
        return carpma


toplama = islem("toplama")
toplama(1,3,5,6,7)
print(toplama(1,3,5,6,7))


carpma = islem("carpma")
print(carpma(1,2,3,6,4))





def divisor(x):
    
    def dividend(y):
        return y / x
    
    return dividend 

divide = divisor(2)
print(divide(3))
         







#parametre olarak fonsiyomlara fonksşyon gönderelim

def topl( a, b):
    return a + b

def cikarma(a,b):
    return a-b

def carp(a,b):
    return a * b

def bolme(a, b):
    return a/ b

def isl(f1, f2, f3, f4, islem_adi):
    
    if islem_adi == "topl":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))
    elif islem_adi == "carp":
        print(f3(2,3))
    elif islem_adi == "bolme":
        print(f4(4,2))
    else:
        print("geçersiz işlem")
        
        
isl(topl, cikarma, carp , bolme, "topl")        
isl(topl, cikarma, carp , bolme, "cikarma")   
isl(topl, cikarma, carp , bolme, "carp")   
isl(topl, cikarma, carp , bolme, "bolme")          

    
# decorator fonsiyonlar - bir özelliği bir kaç yerde kullanmak istiyorsak bir fonku bir çok yerde kullanabiliyoruz
#belli bir fonko belli özellikleri ekleme

def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önce işlemler")
        func(name)
        print("fonsiyondan sonraki işlemler")
        
    return wrapper 

@my_decorator
def sayHello(name):
    print("hello", name)

@my_decorator    
def sayGreeting(name):
    print("greeting", name)
    


sayHello = my_decorator(sayHello)

sayHello("ali")


sayGreeting = my_decorator(sayGreeting)
sayGreeting("ali")




import math
import time


def zaman(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        
        func(*args, **kwargs)
        
        finish =  time.time()
        
        print("fonksiyon "
              +" "
              + func.__name__
              + str(finish-start) 
              + " saniye sürdü")
        
    return wrapper


@zaman
def usalma(a, b):
    
    
    
    print(math.pow(a,b))
    
    
@zaman   
def faktoriyel(num):
    
    
    
    
    print(math.factorial(num))
    
@zaman   
def toplama(a,b):
    print(a+b)





usalma(2,3)

faktoriyel(5)

toplama(5,6)






#ıterator



liste = [1, 2, 3, 4, 5]

for i in liste:  #liste bir iterable obje
    print(i)

print(dir(liste))


iterator = iter(liste)


print(iterator)


print(next(iterator))



#for loopın arka planı
iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break


class MyNumbers:
    def __init__(self, start, stop):
        self.start =  start
        self.stop =   stop
    
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.start <= self.stop:
            x =  self.start
            self.start += 1 
            return x
        
        else:
            raise StopIteration
            
            
list = MyNumbers(10, 20)


for x in list:
    print(x)


myiter = iter(list)
print(next(myiter))


while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break


#generator

#bellekte yer işgal etmeyen bir iteratör inşa ediyor


def cube():
    result = [] # bu liste bellekte yer tutacak
    
    
    for i in range(5):
        result.append(i**3)
        
    return result


print(cube())








def kup():  #üzerinde dolaşabileceğimiz bir iterator objesii gönderiyor
    
    
    for i in range(5): #50kYe bile gitseydi bellekte yer tahsis edilmeyecekti 
        yield i ** 3 #liste içerinde saklamıyoruz, bellekte tutmuyor, üretiliyor ve kullanılıyor

generator = cube()
print(kup())



iterator = iter(generator)

print(next(iterator))


#veya 


iterator = cube()

for i in iterator:
    print(i)


#veya 

for i in cube(): #bilgiyi ne zaman istersek o zaman generator çalıştırılır
    print(i)



liste = [ i**3 for i in range(5)]
print(liste)

#eğer bunu generator yapmak istiyorsak tek yapmamız gereken köşeli parantezleri parenteze çevirmek:
    
    
generator = (i**3 for i in range(5))
print(liste)

print(next(generator))

#veya yazdırmak için
for i in generator:
    print(i)










