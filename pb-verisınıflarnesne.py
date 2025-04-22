class VeriBilimci():
    plang = ["R", "Python"]
    bolum = ""
    experience = 0
    sql = ""
    
    def __init__(self, bolum, sql,  experience, plang ):
            self.bolum = bolum
            self.sql = sql
            self.experience = experience
            self.plang = plang
    


   

class VB():
    bildigi_diller = ["R", "Python"]
    plang = ["R", "Python"]
    bolum = ""
    experience = 0
    sql = ""
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
        
ali = VB()
ali.bildigi_diller

veli = VB()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller


veli.bildigi_diller.append("R")
veli.bildigi_diller

VB.bildigi_diller

ali.bolum
ali.bolum = "istatistik"
ali.bolum
veli.bolum = "tarih"
veli.bolum



#örnek metodları

class VB():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""

    def dil_ekle(self, plang):
        self.bildigi_diller.append(plang)

ali = VB()
veli = VB()

dir(VB())
veli.dil_ekle("C#")
veli.bildigi_diller
ali.dil_ekle("R")
ali.bildigi_diller

#miras yapıları

class Employees():
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.address = ""
        
class DataScience(Employees):
    def __init__(self):
        super().__init__()
        self.programming = ""
        
dataguy1 = DataScience()
dataguy1.programming = "C++"
dataguy1.firstname
        
class Marketing(Employees):
    def __init__(self):
        Employees.__init__(self)
        self.storytelling = ""        
               

mar1 = Marketing()




#▬fonksiyonlart
#bağımlılık
A = 5

def impuresum(b): #fonk'in dışardan bir bağımlılığı var, etkiler ortaya çıkabiliyor, yan etki
    return b + A
impuresum(6)
A = 9

impuresum(6)



def puresum(a,b):#yanetkisiz
    return a + b

puresum(3, 4)



#lambdas

liste1 = [("b", 3), ("a", 8), ("d", 12), ("c", 1)]
print(liste1)
print("?".center(100,"*"))

sorted(liste1, key = lambda x: x[1])

print(liste1)
    
    




#vektörel operasyonlar




#iki tane vektörü çarpmak OOP

a = [ 1, 2 , 3 , 4]

b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])
print("?".center(100,"*"))
print(ab)
print("?".center(100,"*"))
print([a[i]*b[i] for i in range(0, len(a))])
print("?".center(100,"*"))





#FP

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a*b
print(a*b)
 


#map, filter, reduce

liste = [1, 2, 3, 4, 5]

for i in liste:
    print(i + 10)
print("?".center(100,"*"))   

list(map(lambda x : x + 10, liste)) #verilen bir nesnenin üzerinde tanımlanacak bir fonku çalıştırma imkanı, isimsiz fonk

print("?".center(100,"*"))   
list(map(lambda x : x * 10, liste))


#filter -  benzer bir fonk iteratif bir nesne alır ve iteratif nesne oluşturulur, ve uygun olanlar listeye alınır

liste2 = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]

list(filter(lambda x : x%2 == 0, liste2))


#reduce

#indirgeme işlemi

from functools import reduce

liste3 = [1, 2, 3, 4]

reduce(lambda a, b: a+b, liste3)




#modüller

#modul oluşturmak

import veriHesapModulu as hm

hm.yeni_maas(1000)



hm.maaslar


from veriHesapModulu import yeni_maas


import veriHesapModulu as hm
hm.maaslar








































































