#error => hata



# print(a) #name error

# int("1a2") #☻value error

# print(10/0)#zero division error

# print("denem"e) #syntax error






#error handling => hata yönetimi

try:
    
    x = int(input("x : "))
    y = int(input("y:  "))
    
    
    
    print(x / y)
    
except ZeroDivisionError:
    print("y için 0 girilemez!")
    
except ValueError:
    print("x ve y için sayısal değer girmelisiniz")    





try:
    
    x = int(input("x : "))
    y = int(input("y:  "))
    
    
    
    print(x / y)
    
except (ZeroDivisionError, ValueError):
    print("yanlış bilgi girdiniz!")
    
    
    
    
    
    
try:
    
    x = int(input("x : "))
    y = int(input("y:  "))
    
    
    
    print(x / y)
    
except (ZeroDivisionError, ValueError) as e:
    print("yanlış bilgi girdiniz!")  
    print(e)
  
    
    
    
    
try:
    
    x = int(input("x : "))
    y = int(input("y:  "))
    
    
    
    print(x / y)
    
except:
    print("yanlış bilgi girdiniz!")  
     





try:
    
    x = int(input("x : "))
    y = int(input("y:  "))
    
    
    
    print(x / y)
    
except:
    print("yanlış bilgi girdiniz!")  
    
else:
    print("her şey yolunda")    






while True:
    try:
        
        x = int(input("x : "))
        y = int(input("y:  "))
        
        
        
        print(x / y)
        
    except Exception as exc:
        print("yanlış bilgi girdiniz!", exc)  
        
    else:
        print("her şey yolunda gitti")
        break   

    finally:
        print("try except bloğu finito")






while True:
    try:
        
        x = int(input("x : "))
        y = int(input("y:  "))
        
        
        
        print(x / y)
        
    except:
        print("yanlış bilgi girdiniz!")  
        
    else:
        print("her şey yolunda gitti")
        break   






#♣raising an exception

x = 10

if x > 5:
    raise Exception("x 5'den büyük değer alamaz")




def check_password(pswd):
    import re
    if len(pswd)< 8:
        raise Exception("Parola en az sekiz karakter olmalıdır")
    elif not re.search("[a-z]", pswd):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]", pswd):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]", pswd):
        raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]", pswd):
        raise Exception("parola alfanumerik karakter içermelidir")
    elif  re.search("\s", pswd):
        raise Exception("parola boşluk içermemelidir")
    else:
        print("Geçerli parola")
        

password = "12A4a_78"

try: 
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola : try except else bloğundan")
finally:
    print("validation tamamlandı")    



class Person:
    def __init__(self, name , year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name = name


p = Person("Aliiiiiiiiiiiiii", 1989)




#********************************

liste = ["1", "2", "5a", "10b","abc", "10", "50"]

import re
sayisal = []
for i in liste:
    if re.search("[0-9]", i) and not re.search("[a-z]", i):
        sayisal.append(i)

            
print(sayisal)

#alternatif çözüm

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

    

#*************************


while True:
    x = input("Sayı değer giriniz: ")  
    try:
        if x == "q":
            break
        elif x.isdigit() and re.search("[0-9]", x):
            print("Başarılı")
        else:   
            raise Exception("input rakam içermelidir")
        
            
    except Exception as exc:
        print("Sayısal değer girmediniz", exc)
    
#alternatif çözüm

while True:
    num = input("Sayı: ")
    if num == "q":
        break
    
    try:
        result = float(num)
        print("Başarılı değer girildi")
    except ValueError:
        print("Geçersiz input")
        continue







        
#*****************************

def check_password(pswd):
    import re
    if len(pswd)< 8:
        raise Exception("Parola en az sekiz karakter olmalıdır")
    elif not re.search("[a-z]", pswd):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]", pswd):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]", pswd):
        raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]", pswd):
        raise Exception("parola alfanumerik karakter içermelidir")
    elif  re.search("([ıöüğşçI])", pswd):
        raise Exception("parola Türkçe karakter içermemelidir")
    else:
        print("Geçerli parola")
        

password = "1ıA4a_78"

try: 
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola : try except else bloğundan")
finally:
    print("validation tamamlandı")        
    



#alternatif çözüm

def parola_kontrol(parola):




    turkce = "ıöüğşçI"
    
    
    
    for i in parola:
        if i in turkce:
            raise TypeError("Parola Türkçe karakter içeremez")
        else:
            pass
    
    print("Geçerli parola")

parola = input("Parola: ")

try:
    parola_kontrol(parola)
except TypeError as err:
    print(err)    
    
#******************************************    
    
try:
    import math
    x = int(input("x : "))
    
    if x < 0:
        raise ValueError("Negatif Değer")
    
    
    print(math.factorial(x))
    

    
except ValueError:
    print("x  için sayısal değer girmelisiniz")     
    
    
#alternatif çözüm

def faktoriyel(x):
    x = int(x)    
    
    if x < 0:
        raise ValueError("Negatif Değer")
        
        
    result = 1
    
    for i in range(1, x+1):
        result *= i
        
    return result




for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
        
    except ValueError as err:
        print(err)
        continue
    print(y)    