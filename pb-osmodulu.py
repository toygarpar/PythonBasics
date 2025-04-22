import os

result = dir(os)
print(result)

#işletim sistemi ismi
result = os.name
print(result)

#current working directory - etkin dizini öğrenme
result = os.getcwd()
print(result)

#klasör oluşturma
os.mkdir("deneme")

#klasör değiştirme
os.chdir("C:\\")
os.chdir("C:\\Users\90530\Documents\ComputerScience\python\python_temelleri")
os.chdir("..") #bir üst klasöre
os.chdir("../..") #iki üst klasöre


#oluşturulan yeni deneme klasörü içinde klasör oluşturma
os.makedirs("C:\\Users\90530\Documents\ComputerScience\python\python_temelleri\deneme\deneme1")

#listeleme

result = os.listdir()
print(result)

result = os.listdir("C:\\Users\90530\Documents\ComputerScience\python")
print(result)

for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
        
# bir dosya hakkında bilgi sahibi olma        
bilgi = os.stat("format.py")        
print(bilgi)        

import datetime

size_bilgi= bilgi.st_size/1024
print(size_bilgi)

crea_bilgi= datetime.datetime.fromtimestamp(bilgi.st_ctime)  #dosyanın oluşturula zamanı
print(crea_bilgi)

mtime = datetime.datetime.fromtimestamp(bilgi.st_mtime) #dosyanın en son modify edildiği zaman
print(mtime)

atime = datetime.datetime.fromtimestamp(bilgi.st_atime) #dosyanın en son access edildiği zaman
print(atime)



os.system("notepad.exe") #windows programı açma örnek: notepad

os.rename("deneme/deneme1", "deneme/denemerenamed") #rename a folder

os.rmdir("deneme/bunusil") #klasör silme

os.removedirs("deneme/denemerenamed") #alt klasör olduğunda klasör silme eğer klasör boşsa

os.remove("deneme/bunusil/bunudasil") #remove a file
#then
os.rmdir("deneme/bunusil")


import os
import datetime

#path

result = os.path.abspath("deneme.py")

print(result)

result1 = os.path.dirname("C:/Users/90530/Documents/ComputerScience/python/python_temelleri/deneme.py") #dizin isimini alma
print(result1)


result2 = os.path.dirname(os.path.abspath("deneme.py")) #☻dizini bilmiyorsunuz sadece dosya ismiyle dizini bulma
print(result2)

result3 = os.path.exists("deneme.py") #böyle bir dosya var mı? ya da klasör sorgulayabiliriz
print(result3) #True


result4 = os.path.isdir("C:/Users/90530/Documents/ComputerScience/python/python_temelleri/")
print(result4)


result5 = os.path.isfile("C:/Users/90530/Documents/ComputerScience/python/python_temelleri/deneme.py")
print(result5)


result6 = os.path.join("C:\\","deneme","deneme1") #dizin oluşturma, eğer klasörler yoksa sadece dizini oluşturur klaösrleri değil
print(result6) #C:\deneme\deneme1

result7 = os.path.split("C:\\deneme") #dizini bölme
print(result7)

result8 = os.path.splitext("deneme.py") #◘dosya ismini bölme, dosya ismi değiştireceksek ilk önce ayırıp ismi değiştirip sonra birleştirmek gerekiyor
print(result8)
result8[0]
result8[1]




































































