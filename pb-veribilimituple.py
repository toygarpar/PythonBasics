t = ("ali", "veli", 1, 2, 3.2, [1, 2, 3 ,4])
print(t)
len(t)

t1 = "ali", "mehmet", 5.2, 8, 9, [1, 2, 3, 4]

#sona virgül atmazsak tek elemanlı tuple'ı sistem str görür, o yüzden sona virgül atılır.
t2 = tuple("eleman1",)
type(t2)

#erişim - listelerle aynı şekilde gerçekleşir

t[1]
t[0:3]
#t[2] = 99 #değiştirilemez

#dictionaries

d  = {
      "REG" : "Regresyon Modeli",
      "LOJ" : "Lojistik Regresyon",
      "CART" : "Classification and Reg"
           
      }
d
len(d)

e = {
     "REG" : 10,
     "LOJ" : 20,
     "CART" : 30
     }


f = {
     "REG" : ["RMSE", 0],
     "LOJ" : ["MSE", 20],
     "CART" : ["SSE", 30]
     }

dir(f)
"""
 'clear',
 'copy',
 'fromkeys',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values'
 
""" 

#eleman seçme işlemleri

d["REG"]
f["CART"]

g = {
     "REG" : {"RMSE": 10,
              "mse" : 20,
              "sse" : 30           
              
              },
     
     "LOJ" : ["MSE", 20],
     "CART" : ["SSE", 30]
     }

g["REG"]["sse"]





d  = {
      "REG" : "Regresyon Modeli",
      "LOJ" : "Lojistik Regresyon",
      "CART" : "Classification and Reg"
           
      }

#ekleme işlemleri
d["GBM"] = "Gradient Boosting Mac"
d

#eleman değiştirme
d["REG"] = "Çoklu Doğrusal Regresyon"
d
d[1] = "Yapay Sinir Ağları"
d

tu = ("tuple",)
d[tu] = "yeni bir şey"
d


#sets

#set oluşturma

s = set()

l = [1, "a", "ali", 123]
s =set(l)
s
l

e =("a", "ali")
k = set(e)
e
k

ali = "lutfen_ata_bakma_uazaya_git"
type(ali)

al = set(ali)
al

w =ali.split("_")
w
q = set(w)
q
len(q)
q[0]




#eleman ekleme ve çıkarma

l = ["geleceği", "yazanlar"]

s =set(l)

dir(s)
"""
'add',
'clear',
'copy',
'difference',
'difference_update',
'discard',
'intersection',
'intersection_update',
'isdisjoint',
'issubset',
'issuperset',
'pop',
'remove',
'symmetric_difference',
'symmetric_difference_update',
'union',
'update'

"""
s.add("ile")
s

s.add("geleceğe_git")
s

s.add("ile")
s

s.remove("ile")
s

s.add("ali")
s
#eleman olmasa bile hata vermeden silmek için discard
s.discard("ali")
s


#difference and symmetric difference

set1 = set([1 , 3, 5])
set2 = set([1, 2, 3])

set1.difference(set2)

set2.difference(set1)

set1.intersection(set2)

set1.symmetric_difference(set2)

set1 - set2
set2 -set1

set1.union(set2)
set1
set2
#kesişim
set1 & set2


set1.intersection_update(set2)
set1



#set sorgu işlemleri
set3 = ([7, 8, 9])
set4 = ([5, 6, 7, 8, 9, 10])

#iki küme kesişiminin boş olup olmadığı

set1.isdisjoint(set2)

#bir kümenin bütün elemanları başka bir küme içeresinde yer alıp almadığı

set1.issubset(set2)

#bir küme diğer bir kümeyi kapsıyor mu

set2.issuperset(set1)















































































