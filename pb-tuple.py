#tuple

list = [1, 2, 3]
tuple = (1, "iki", 3)

print(list)
print(tuple)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))



liste = ["ali","veli"]
demet = ("damla", "ayşe", "ayşe")
print(liste)
print(demet)



liste[0] = "Ahmet"

print(demet.count("ayşe"))
print(demet.index("ayşe"))

names = ("demet", "emel", "kezban") + demet
print(names)

names2 = list(names)
print(names2)

names2[4] = "nalan"
print(names2)
demet = tuple(names2)
print(demet)


a = ("banana", "grape", "cherry")
b = list(a)
b[0] = "apple"
a = tuple(b)

print(a)


#dictionary

#key - value


sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("kocaeli")])
print(plakalar[sehirler.index("istanbul")])



plakalar = { "kocaeli" : 41, "istanbul": 34}
print(plakalar)
print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"] = 6
print(plakalar)
plakalar["kocaeli"] ="new value"
print(plakalar)



users = {
    "toygarpar" : {
        "age" : 49,
        "roles" :["user"],
        "email" : "toygar.par@gmail.com",
        "adres" : "izmir",
        "phone" : "5555555"
        },
    "mustafaselcuk" :{
        "age" : 40,
        "roles" :["admin", "user"],
        "email" : "mselcukdonmez@gmail.com",
        "adres" : "bursa",
        "phone" : "6666666"
        }
    
      
    
    }


print(users["toygarpar"])
print(users["mustafaselcuk"])



print(users["toygarpar"]["age"])
print(users["toygarpar"]["email"])
print(users["toygarpar"]["adres"])
print(users["toygarpar"]["phone"])
print(users["mustafaselcuk"]["roles"][0])



students = {
    "120" : {
        "ad" : "Ali",
        "soyad" : "Yılmaz",
        "telefon" : "5555555"
        },
    "125" : {
        "ad" : "Can",
        "soyad" : "Korkmaz",
        "telefon" : "5555556"
        },
    "128" : {
        "ad" : "Volkan",
        "soyad" : "Yükselen",
        "telefon" : "5555557"
        }
    }


talebe = {}

number = input("öğrenci no girin: ")
name = input("öğrenci ad girin: ")
surname = input("öğrenci soyad girin: ")
phone = input("öğrenci telefon girin: ")

# talebe[number] = {
#     "ad" : name,
#     "soyad": surname,
#     "telefon" : phone
    
#     }


talebe.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
        
        }
    })

number = input("öğrenci no girin: ")
name = input("öğrenci ad girin: ")
surname = input("öğrenci soyad girin: ")
phone = input("öğrenci telefon girin: ")

talebe.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
        
        }
    })



number = input("öğrenci no girin: ")
name = input("öğrenci ad girin: ")
surname = input("öğrenci soyad girin: ")
phone = input("öğrenci telefon girin: ")

talebe.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
        
        }
    })

print(talebe)


ogrno = input("öğrenci no: ?")
student = talebe[ogrno]
print(student)


print(f'Aradığınız  nolu öğrencinin adı: {student["ad"]} , soyadı : {student["soyad"]} ve telefon nosu {student["telefon"]}')



#sets

fruits = {"orange", "apple", "banana"}

print(fruits)

#setler indekslenemez

for x in fruits:
    print(x)
    
#add ve update methodları
fruits.add("cherry")
fruits.update(["mango", "grape", "apple"])
print(fruits)


#set te duplicatelar olamaz
mylist = [1, 2, 5, 4, 4, 2, 1]
print(set(mylist))

#remove and discard
fruits.remove("mango")
fruits.discard("apple")
print(fruits)

#pop methodu
fruits.pop()
print(fruits)

#clear
fruits.clear()
print(fruits)

































