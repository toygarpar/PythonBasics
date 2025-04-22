"""

Müşteri adı
Müşteri soyadı
Müşteri ad +soyad
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı
"""

musteriAdi= "Toygar"
musteriSoyad="Par"
musteriAdSoyad= musteriAdi+ "  " +musteriSoyad
musteriCinsiyet= True #Erkek
musteriTcKimlik= "123456789"
musteriDogumYili= 1947
musteriAdres="Seferihisar İzmir"
musteriyasi= 2024- musteriDogumYili

print (musteriAdSoyad)
print(musteriyasi)


"""
Sipariş 1 => 110        TL
Sipariş 2 => 11000.5    TL
Sipariş 3 => 356.95     TL
"""

order1 = 110
order2 = 1100.5
order3 = 356.95

print (order1 + order2 + order3)
total = order1 + order2 + order3
print ("Total:", total)
