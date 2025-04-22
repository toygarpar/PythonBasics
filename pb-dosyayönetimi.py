#dosya yönetimi 

# w - write - yazma modu, dosyayı konumda oluşturur
# **Dosyayı konumda oluşturur **Eğer dosya halihazırda varsa Dosya içeriğini siler ve yeniden ekleme yapar
file  = open("newfile.txt", "w")

file.close()


file = open("C:/Users/90530/Documents/ComputerScience/python/newdeneme.txt" , "w")
print(file)

#w ile yeniden aynı dosyayı açtığımızda daha önceki bilgiler silinecek yeniden oluşturulacak
file  = open("newfile.txt", "w", encoding="utf-8")
# file.write("Toygar Par amına koyar")
file.close()

# a - append - ekleme, dosya yoksa konumda oluşturur


file  = open("newfile.txt", "a", encoding="utf-8")
file.write("\nBöcüş Par kırtlar")
file.close()



# x - create - oluşturma, dosya zaten varsa hata verir
#işimiz sadece bir dosya oluşturmaksa

file  = open("newfile2.txt", "x", encoding="utf-8")


# r -read - okuma, varsayılan, dosya konumda yoksa hata verir
#Python'da Reading Files - Dosya Okuma

try:
    file = open("newfile3.txt", "r")
    print(file)
except Exception as ex:
    print("Dosya Okuma Hatası : Dosya Bulunamadı : ", ex)
finally:
    print("Dosya kapandı")
    file.close()





#*************

file =  open("newfile.txt", "r", encoding="utf-8")

#for döngüsü ile içeriği ekrana yazıdrma

for i in file:
    print(i , end= "")
    
 
    
#read() fonksiyonu ile ekrana yazırma

content = file.read()


print("içerik1")
print(content) 

file =  open("newfile.txt", "r", encoding="utf-8")    
content2 = file.read()
print("içerik2")
print(content2) 
    
 
file.close()    




#***********
file =  open("newfile.txt", "r", encoding="utf-8")

content3 = file.read(5)
content3 = file.read(3)
content3 = file.read(3)

print(content3)

file.close()




#readline fonksiyonu


file =  open("newfile.txt", "r", encoding="utf-8")

content4 = file.readline()

print(content4)

file.close()




#############


file =  open("newfile.txt", "r", encoding="utf-8")

print(file.readline(), end = "")

print(file.readline())

file.close()




#readlines fonsiyonu - her bir satırı bir liste elemanı olarak karşımıza çıkarır

file =  open("newfile.txt", "r", encoding="utf-8")

liste = file.readlines()

print(liste)

file.close()




#D>osya Okurken Kullandığımız Fonksiyonların Kullanımları


with open("newfile.txt", "r", encoding = "utf-8") as file:

    content = file.read()
    
    print(content)
    
    file.seek(0)  #cursor nereye gitsin? hangi konuma gitsin?
    
    print(file.tell()) #◘cursorun nerede olduğunu söylüyor
    
    content2 = file.read()
    
    print(content2)
    
    
    

#Dosyada Güncelleme Yapma

with open ("newfile.txt", "r+", encoding = "utf-8") as file:   # r+ hem açma hem okuma hem yazma modunu temsil ediyor

    print(file.read())
    

with open ("newfile.txt", "r+", encoding = "utf-8") as file: 
    #file.seek(20) #☻ 20. konumdan itibaren deneme yazar
    file.write("deneme")  



#append - var olan içeriğe dokunulmuyor sonuna ekleniyor, sayfa sonunda güncelleme
#append ile eğer dosya yok ise de oluşturulur
with open ("newfile.txt", "a", encoding = "utf-8") as file:  

    file.write("\nZeytin Par")



with open ("newfile.txt", "r", encoding = "utf-8") as file:  

    print(file.read())


#sayfa başında güncelleme

with open ("newfile.txt", "r+", encoding = "utf-8") as file: 
    content = file.read()
    content =  "Şehmuz Par\n" + content   #şu an hala dosya içerisinde değil sadece ekrana yazdırabilir
    
    file.seek(0)
    file.write(content)
    print(content) 
    





with open ("newfile.txt", "r", encoding = "utf-8") as file:  

    print(file.read())
    
    
    
    
#sayfa ortasında güncelleme    

with open ("newfile.txt", "r+", encoding = "utf-8") as file: 
    list = file.readlines()
    print(list)
    
    # list.insert(1, "Nataşa Par\n") #insert object before the index , bunu ekrana yazırabiliriz ancak
    list.insert(2, "Kocaoğlan Par\n")
    #sayfa/dosya içine yazdırmak için
    file.seek(0)
    #for loop ile yazdırma
    # for i in list:
    #     file.write(i)
    
    #for döngüsü ile tek tek dolaşmadan yazdırma
    file.writelines(list)
    print(list)


with open ("newfile.txt", "r", encoding = "utf-8") as file:  

    print(file.read())








#dosya yönetimi uygulama


def not_hesapla(line):
    line = line[ :-1]
    liste = line.split(":")
    
    grades = liste[1]
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")
    
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1 + not2 +not3)/3
    
    if ortalama >= 90 and ortalama <=100:
        harf = "AA"
    elif ortalama>=80 and ortalama <=89:
        harf = "BB"
    elif ortalama>=60 and ortalama <=80:
        harf = "CC"
    else:
        harf = "FF"
        
    return ogrenciAdi + ": " + grades + " ==> " + harf + "\n"




def ortalamalari_oku():
    with open("sinav_notlari.txt", "r", encoding = "utf-8") as file:
        for line in file:
            print(not_hesapla(line))
        




def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("Not 1 Gir: ")
    not2 = input("Not 2 Gir: ")
    not3 = input("Not 3 Gir: ")
    
    with open("sinav_notlari.txt", "a", encoding = "utf-8") as file:
        file.write(ad + " " + soyad + ": " + not1 + ", " + not2 + ", " + not3+ "\n")


def not_kaydet():
    with open("sinav_notlari.txt", "r", encoding = "utf-8") as file:
        liste1 = []
        
        for i in file:
            liste1.append(not_hesapla(i))
            
        with open("sonuclar.txt", "w", encoding = "utf-8") as file2:
            
            for i in liste1:
                file2.write(i)



while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt et\n4- Çıkış\n==>")
    
    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        not_kaydet()
    else:
        break
    
    
    






































































