
#oluşturma
notlar = [90, 80 ,70 ,50]

print(type(notlar))

liste = ["a", 19.3, 90]

liste2 = ["a", 19.3, 90, notlar]
print(len(liste2))
print(type(liste2[0]))
print(liste2[3])
combined = [liste, liste2]
print(combined)


liste3 = [10, 20, 30, 40, 50]

print(liste3[1])

#erişim
print(liste3[0:2])
print(liste3[:2])
print(liste3[2:])

yeniliste = ["a", 10, [20, 30, 40, 50 ]]
print(yeniliste)
print(yeniliste[2][3])

#eleman değiştirme

liste4 = ["ali", "veli", "berkcan", "ayşe"]

liste4[1] = "velinin_babası"
print(liste4)
liste4[1] = "veli" 

liste4[0:3] = "alininbabasi", "velininbabasi", "berkcanınbabasi"

print(liste4)


liste4 = ["ali", "veli", "berkcan", "ayşe"]

liste4 += ["kemal"]
print(liste4)


#del silme işlemi
del liste4[2]
liste4


#liste metotları

liste5 = ["ali", "veli", "deli"]

dir(liste5)
"""

 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort'
 
"""

liste5.append("amcık")
liste5
liste5.extend(["cunt","pussy"])
liste5
liste5.remove("amcık")
liste5.insert(2, "ayşe")
liste5.insert(len(liste5), "fuckyeah")
liste5
liste5.pop(5)
liste5

#count

liste5.count("ali")

#copy

listeyedek = liste5.copy()

#extend - iki listeyi birleştirmek amacıyla

liste5.extend([1, 2, 3])
liste5

#index

liste5.index("fuckyeah")

#reverse
liste5.reverse()
liste5
#sort
liste5.sort()
liste3.sort()
liste3
#clear
liste3.clear()
liste3










