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
student = talebe(ogrno)



print(f"Aradığınız {ogrno} nolu öğrencinin adı: {student["ad"]} , soyadı : {student["soyad"]} ve telefon nosu {student["telefon"]} ")