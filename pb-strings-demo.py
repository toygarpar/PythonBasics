website = "http://www.toygarpar.com"

course = " Pythton Kursu: Baştan sona Python Programlama Rehberiniz (40 Saat)"

# course karakter dizisindekaç karakter bulunmaktadır?

result = len(course)
print(result)

#website için www karakterlerini alın
lenght = len(website)
result= website[7:10]
print (result)

# website için com karakterlerini alın
result= website[22:25]
result = website[lenght-3:lenght]
print (result)

#course ifadesindeki ilk 15 ve son 15 karakterleri alın tersten yazdırın
result = course[0:15]
result = course[:15]
result = course[-15:]
#course ifadesindeki karakterleri  tersten yazdırın
result = course[::]
result = course[::2]
result = course[::-1]

s = "12345" * 5
print(s[::5])

name, surname, age, job = "Toygar", "Par", 32, "finans"
#yukarda verilen değişkenler ile ekrana aşağadaki ifadeyi yazıdırın
# "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis"

#result = "Benim adım " + name + " "+surname+", Yaşım " + str(age)+ " mesleğim " + job
#result = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}" .format(name, surname, age, job)
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}" 


# Hello world ifadeside w harfini W ile değiştirin

s = "Hello world"
s = s[0:6] + "W" + s[-4:]
s.replace("w","W")
print(s)

# abc ifadesini yan yana 3 defa yazdırın
result = "abc" * 3


print (result)