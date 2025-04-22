
lst = [1,2,3]

result = (type(lst))

print(result)


#class

class Person:
    
    #class attributes
    address = "no info"
    
    #constructor (yapıcı method)
    def __init__(self, name, year):
    
        #object attributes
        self.name = name
        self.year = year
        print("__init__ metotu çalıştı")
        
        
    #methods
    
    #instance method
    def intro(self):
        print("hello there. I am "+ self.name)

    def calculate_age(self):
        return 2024 - self.year

#object, instance

p1 = Person("Toygar", 1974)

p2 = Person("Selçuk", 1983)

p3 = Person(name="Sabriye", year = 1994)


print(p1)
print(p2)
print(type(p1))
print(type(p2))

print(p1 == p2)

#updating
p1.name= "Özdemir"
p1.address = "İstanbul"
p1.year  = 1946


#accessing object attributes
print(f"name: {p1.name} , birthyear: {p1.year}, address: {p1.address}")

print(f"name: {p2.name} , birthyear: {p2.year},  address: {p2.address}")

print(f"name: {p3.name}, birthyear: {p3.year}, address: {p3.address}")



#call class method

p1.intro()

p2.intro()

p3.intro()

print(f'adım : {p1.name} ve yaşım: {p1.calculate_age()}')

print(f'adım : {p2.name} ve yaşım: {p2.calculate_age()}')

print(f'adım : {p3.name} ve yaşım: {p3.calculate_age()}')








class Circle:
    
    #class object attribute
    pi  = 3.14
    
    
    def __init__(self, yaricap = 1 ):
        self.yaricap = yaricap
        
    #methods
    
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2) 
    
c1 = Circle()  
c2 = Circle(5)  

c1.cevre_hesapla()
c1.alan_hesapla()   

print(f"c1: alan = {c1.alan_hesapla()}, cevre = {c1.cevre_hesapla()}")

print(f"c2: alan = {c2.alan_hesapla()}, cevre = {c2.cevre_hesapla()}")




# Inheritance (kalıtım) : Miras ALma

# Person => name, lastname, age , age, eat(), run(), drink(), fuck(), rock()
# Student(Person), Teacher(Person)




#Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        
        self.firstname = fname
        self.lastname = lname
        print("Person Created!!!")
        
        
    def ben_kimim(self):
        print("I am a person")
        
    def eat(self):
        print("I am eating")
        
class Student(Person): #person classına sahip olan özelliklere student classıda sahip olmuş oluyor
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created!!!")
        
    
        
    
    #override
    def ben_kimim(self): #person ben_kimim metotunu ezmek için
        print("I am student")

    def sayHello(self):
        print("Hello, I am a student") #sadece student üzerinden çağırabiliriz, Persona özgün olan bir metot değil
        
        
class Teacher(Person):
    def __init__(self, fname, lname, branch ):
        super(). __init__(fname,lname)
        self.branch  = branch   
        
    def ben_kimim(self):
        print(f"I am a {self.branch} teacher")
        
        

p1 = Person("Toygar", "Par")
s1 = Student("Böçüş", "Par", 1453) #studentda bir person olduğundan dolayı Person init metotuda çalıştı
t1 = Teacher("Perihan", "Pehlivan", "Math")


print(p1.firstname + " " + p1.lastname)

print(s1.firstname + " " + s1.lastname + " " + str(s1.studentNumber))

print(t1.firstname + " " + t1.lastname + " " + t1.branch)



p1.ben_kimim()
s1.ben_kimim()
t1.ben_kimim()

p1.eat()
s1.eat()
t1.eat()



s1.sayHello()






#special Methods


listem = [1, 2, 3]

print(len(listem))

mystring = "My String"

print(len(mystring))

print("</>".center(50, "*"))

print(type(listem))
print(type(mystring))

print("</>".center(50, "*"))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie Objesi oluşturuldu")
        
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Movie silindi")

m = Movie("Jaws", "Steven Spielberg", 129)

#print(len(m))
print(type(m))

print("</>".center(50, "*"))

print(listem)
print(m)

print("</>".center(50, "*"))

print(str(listem))
print(str(m))

print("</>".center(50, "*"))

print(len(listem))
print(len(m))


print("</>".center(50, "*"))


del m

#print(m)



















# uygulama json
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
        self.isLoggedIn =  False
        self.currentUser = {}
        
        #load users from .json file
        self.loadUser()
        
    #json dosyasından user bilgilerini alacak
    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding = "utf-8") as file:
                users = json.load(file)
                for user in users:
                    print(user)
                    user = json.loads(user)
                    print(user["username"])
                    newUser = User(username = user["username"], password = user["password"], email = user["email"])
                    self.users.append(newUser)
            print(self.users)
        
    
    #kullanıcı oluşturma işlemi
    def register(self, user : User):
        self.users.append(user)
        self.savetoFile() #eklenen user bilgisini kaydetmek için
        print("Kullanıcı oluşturuldu!")
    
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
        list = []
        
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open("users.json", "w") as file:
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




# visit exchangerate-api.com






#class ve enum exercise

from enum import Enum

class Quality(Enum):
    LOW: int = 480
    MEDIUM: int = 1080
    HIGH: int = 1440
    
class Privacy(Enum):
    PRIVATE: str = "Private"
    UNLISTED: str = "Unlisted"
    PUBLIC: str = "Public"
    
def upload(file: str, *, quality: Quality, privacy: Privacy) -> None:   #*'dan sonra paramlar mutlaka girilmeli
    print(f'Uploading: "{file}" in {quality.value}p ({privacy.value})')
    
def main() -> None:
    upload("cat.mp4", Quality.LOW, Privacy.PRIVATE)
    
    
if __name__ == "__main__":
    main()
    
    
    
#class exercise for format

from typing import Any

class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages




    def __format__(self, format_spec: Any) -> str:
        match format_spec:
            case "time":
                return f"{self.pages /60:.2f}h"
            case "caps":
                return self.title.upper()
            case _:
                raise ValueError(f"Unknown specifier for Book()")
            
            
def main() -> None:
    harry_potter: Book = Book("Harry Potter", 300)
    python_learn: Book = Book("Python Learn", 20)
    
    #print(f"{harry_potter: caps}")
    print(f"Read time: {harry_potter:time}")
    
    
if __name__ == "__main__":
    main()
    
            
            
            

# fruit class, pickle and json, pickled data can be extremely dangereous, they can pass shell command
#internetten emin olmadan sakın pickled dosyalar indirip çalıştırmayın, çok çok tehlikeli

import json
import pickle



class Fruit:
    def __init__(self, name : str, calories: float):
        self.name = name
        self.calories = calories
        
    def describe_fruit(self):
        print(self.name, self.calories, sep =": ")
        
        
if __name__ == "__main__":
    
    with open("data.pickle", "rb") as file:
        #pickle.dump(fruit, file)
        fruit: Fruit= pickle.load(file)
    
    
    fruit.describe_fruit()
    
    #now we can edit anyway we want easily
    fruit.calories += 200
    fruit.describe_fruit()
    
    with open("data.pickle", "wb") as file:
        pickle.dump(fruit, file)
    
    # fruit: Fruit = Fruit("Banana", 100)
    # fruit.describe_fruit()
        
    # fruit.calories = 150
    
    
    # with open("data.pickle", "wb") as file:
    #     pickle.dump(fruit, file)
        
    
    
    # with open("banana.json", "w") as file: #dict'i json  string olarak json dosyasına kaydedelim
    #     data = { "name": fruit.name, "calories": fruit.calories}
    #     json.dump(data, file)
        
        
    # with open("banana.json", "r") as file: #json dosyasındaki bilgiyi dict olarak açıp yükleyelim
    #     data = json.load(file)
    #     print(data)



# print(type(data))

























































