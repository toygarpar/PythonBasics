

#Yöntem 1

import math
import math as islem


value =  dir(math)
value = help(math)
value  =help(math.factorial)

print(value)

print(math.sqrt(49))
print(math.factorial(5))


print(math.floor(5.9))

print(math.ceil(5.9))

print(islem.factorial(7))



#Yöntem2

from math import * #hepsini import eder

from math import factorial, sqrt #☻sadece fonksiyonları import etmek için

def sqrt(x):
    print("x :" + str(x))

print(factorial(5))
print(sqrt(25))



#random modulu

import random

result = dir(random)

print(result)

print(help(random))


sonuc = random.random()
sonuc = random.random() * 100
sonuc = random.uniform(10, 100)
sonuc = int(random.uniform(10, 100))

print(sonuc)

tamnum = random.randint(1, 100)
print(tamnum)



names = ["ali", "yağmur", "deniz", "cenk", "ahmet", "efe"]

son = names[random.randint(0,len(names)-1)]

print(son)


result = random.choice(names)

print(result)


greeting = "hello there"

selam = random.choice(greeting)

print(selam)




liste = list(range(0,10))
print(liste)
random.shuffle(liste)
print(liste)


liste1 = range(100)

e = random.sample(liste1, 3 ) #♥verdiğim listeden bana random sample 3 sayı getir
print(e)


f= random.sample(names, 2)
print(f)




