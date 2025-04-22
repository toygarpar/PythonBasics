import datetime

result = dir(datetime)
print(result)




x = datetime.datetime.now() #2024-01-18 16:18:10.768875  zaman ve tarihi veriyor
print(x)

print(x.year)
print(x.strftime("%A"))



y  = datetime.datetime(2020, 5, 17) #2020-05-17 00:00:00

print(y)


# strftime( ) method formats datetime objects into readable strings

z = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))






# from datetime import  date
# from datetime import  time
from datetime import datetime

res =  dir(datetime)
print(res)

simdi = datetime.now()
eee = datetime.now()
eee = simdi.year
print(eee)
eee = simdi.month
print(eee)
eee = simdi.day 
print(eee)
print(simdi.hour)
print(simdi.minute)
print(simdi.second)

print(datetime.today())

www = datetime.ctime(simdi) #Thu Jan 18 16:38:06 2024 bu string biçimlendirilebiliyor
print(www)

www = datetime.strftime(simdi, "%Y")
print(www)


www = datetime.strftime(simdi, "%X")
print(www)

www = datetime.strftime(simdi, "%d")
print(www)

www = datetime.strftime(simdi, "%A")
print(www)

www = datetime.strftime(simdi, "%B")
print(www)

www = datetime.strftime(simdi, "%Y %B %A %d")
print(www)



t = "21 Nisan 2019"

gun, ay, yil = t.split()

print(gun)
print(ay)
print(yil)



import datetime

ti = "15 April 2019 hour 10:12:30"
dt = datetime.strptime(ti, "%d %B %Y hour %H:%M:%S")

print(dt)

ye = dt.year
print(ye)



birthday = datetime(1974, 3, 19, 10, 30, 53)
print(birthday) # 1974-03-19 10:30:53

sonuc = datetime.timestamp(birthday)
print(sonuc) #saniye bilgisini verir

tt = datetime.fromtimestamp(sonuc)
print(tt) # tekrar datetime bilgisini verir  seconds to datetime


son = datetime.fromtimestamp(0)
            
print(son)

fark = simdi - birthday #timedelta objesi

print(fark)


fa = fark.days
print(fa)



fars = fark.seconds
print(fars)


from datetime import timedelta

sonuc = simdi + timedelta(days=10)

print(sonuc)


sonuc = simdi + timedelta(days=1130, minutes=10)

print(sonuc)


sonuc = simdi - timedelta(days=10)

print(sonuc)




##########################################################################


from datetime import datetime


an = datetime.now()
a= an.year  # an.year, month, day, hour, minute, second, 
print(an)
print(a)


bugun = datetime.today()
print(bugun)
b = bugun.hour
print(b)

#ctime methodu param olarak time object veriliyor
sonuc = datetime.ctime(an)
print(sonuc) # Sat Jan 20 17:07:53 2024

sonuc1 = datetime.strftime(an, "%Y") #datetime objesi vererek format değişkeni veriyoruz
print(sonuc1)

sonuc2 = datetime.strftime(an, "%X") # %X saat zamanı bilgisi %d gün, %A gün bilgisi string olarak (ör: monday), %B Ay bilgisi string olarak
print(sonuc2) #17:07:53

sonuc3 = datetime.strftime(an, "%d %A %B %S %X %Y")
print(sonuc3)



t = "20 Ocak 2024"

gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)


#strptime() methodu
z = "20 January 2024 17:39:30"
dt = datetime.strptime(z, "%d %B %Y %X") #stringden time objesi yaratma
print(dt)  # 2024-01-20 17:39:30
print(type(dt)) # <class 'datetime.datetime'>

yil = dt.year
print(yil)



birthday = datetime(1974 , 3, 19, 22,30, 30 )
print(birthday)

r = datetime.timestamp(birthday) #saniye cinsinden
print(r)

s = datetime.fromtimestamp(r) # saniye to datetime
print(s)

#iki tarih arasındaki fark
q = an - birthday #timedelta objesi gelir
print(q)


u = datetime.fromtimestamp(0) #1970-01-01 03:00:00 bilgisayarlar için kullanılan milat bilgisi
print(u)



q = q.days #seconds, microseconds
print(q)


from datetime import timedelta

sonuc4 = an +timedelta(days=10) #şu anki gün bilgisinin üzerine 10 gün ekler
print(sonuc4)

sonuc5 = an + timedelta(days=730, minutes=10)
print(sonuc5)

sonuc6 = an - timedelta(days=10)
print(sonuc6)











































