import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])




import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



#dict

person  = {"name": "Ali", "languages": ["python", "C#"]}

result = person["name"]
result1  = person["languages"]
result2 = person["languages"][0]
print(result)
print(result1)  
print(result2)                  



#********************************************
#uygulama json

import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        
        #load userrs from .json file
        self.loadUser()
        
    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding = "utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    print(user["username"])
                    newUser = User(username= user["username"], password = user["password"], email =  user["email"])
                    self.users.append(newUser)
            print(self.users)
        
        
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı Oluşturuldu.")
        
    
    
    
    def login(self, username, password):
        if self.isLoggedIn:
            print("zaten login oldunuz")
            
        else: 
            
            for user in self.users:
                if user.username == username and user.password == password:
                    self.isLoggedIn =  True
                    self.currentUser  = user
                    print("login yapıldı.")
                    break 
            
    def logout(self):
        self.isLoggedIn = False
        self.currentUserrentUser = {}
        print("Çıkış Yapıldı")
                
    def identity(self):
        if self.isLoggedIn:
            print(f" username: {self.currentUser.username}")
        else:
            print("Giriş Yapılmadı")
        
    def savetoFile(self):
        with open("users.json", "w") as file:
            list = []
            
            for user in self.users:
                
                list.append(json.dumps(user.__dict__)) #user classına dict haline çeviriyor
            
            json.dump(list, file)
    
    
repository = UserRepository()    
    
while True:
    print("Menü".center(50,"*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ")
    if secim == "5":
        break
    else: 
        if secim == "1":
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            
            user = User(username=username, password = password, email = email)
            repository.register(user)
            
            print(repository.users)
        elif secim == "2":
            if repository.isLoggedIn:
                print("zaten login oldunuz")
            else:
                username = input("username: ")
                password = input("password: ")
                
                repository.login(username, password)
        elif secim == "3":
            repository.logout()
        elif secim == "4":
            repository.identity()
        else:
            print("Yanlış Seçim!")
            
            



#requests modülü
import json

print(json.__file__)   

import requests
result = requests.get("https://jsonplaceholder.typicode.com/todos")
print(result)

            


#json stringini dictionarye çevirmek
            
import json

p_str = '{"name": "Toygar", "languages": ["python", "c"]}'
            
strtodict = json.loads(p_str)            

print(type(strtodict))     

str1 = strtodict["name"]       
print(str1)            

str2 = strtodict["languages"]            
print(str2)            



#json dosyasını açma

with open("person.json") as f:
    data = json.load(f)
    print(data)
            
            
print(data["name"])            
print(data["languages"])            
            

#dict'i json stringine çevirmek

person_dict = {
    "name": "Toygar",
    "languages": ["Python", "C"]
    }

res2 = json.dumps(person_dict)
print(res2)
print(type(res2))


#json olarak dosyaya yazma işlemi

with open("person.json", "w") as f:
    json.dump(person_dict, f)
    
    
person_dict1 = json.loads(p_str)    

res3 = json.dumps(person_dict1, indent = 4, sort_keys=True)


print(person_dict1)

print(res3)


#☻ Requests Modülü

import requests

result = requests.get("https://jsonplaceholder.typicode.com/todos")

print(result)

result2 = result.text
print(result2)

print(type(result2))

print(result[0]["title"]) #string üzerinden bir dict gibi bir işlem yapamıyoruz



#exchange rate APİ


import requests
import json

api_key = "e3088cf0dc75d3c9ebe430f7"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"


bozulan_doviz = input("Bozulan Döviz Türü: ").upper()  #USD
alinan_doviz = input("Alınan Döviz Türü: ").upper()   #TRY
miktar = input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz? ")  #ne kadar USD bozdurmak istiyorsunuz

sonuc = requests.get(api_url + bozulan_doviz)  #bozulan döviz cinsi api_url'in sonuna yazdırılacaK
print(sonuc)
print(sonuc.text)

#json modülü aracılığı ile okunabilir bir duruma getirmemiz lazım
#python arafında jsondan gelen datayı bir python objesine dönüştürelimki alt elemanlarına ulaşabilelim

































































































            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    