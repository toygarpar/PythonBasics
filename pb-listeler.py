#List

msg = "Hello There. My name is Toygar Par"

msg1 = msg.split()
print(msg1[0])
print(msg[0])


mylist = [1, 2, 3]
print(mylist)
mylist = ["bir", 2, True, 5.6]
print(mylist)
print(type(mylist[0]))

list1 = ["one", "two", "three"]
list2 = ["four", "five", "six"]
list = list1 + list2
print(list)
print(len(list))

userA = ["Toygar", 49]
userB = ["Selçuk", 40]

users = userA +userB
print(users)
#yeni bir liste oluşturmak - liste içerisinde liste
users2 = [userA, userB]
print(users2)
print(users2[1])
print(users2[1][0])


cars = ["Bmw", "Mercedes", "Opel", "Mazda"]
print(cars)
print(len(cars))
print(cars[0])
print(cars[-1])
cars[3] = "Toyota"
print(cars)
print("Mercedes" in cars)
print(cars[-2])
print(cars[:3])
cars.append("Renault")
cars.extend(["Audi", "Nissan"])
print(cars)
cars += ["Chevrolet"]
print(cars)
del cars[-1]
print(cars)
print(cars[::-1])



studentA = ["Yiğit Bilgi", 2010, (70,60,70)]
studentB = ["Sena Turan", 1999, (80,80,70)]
studentC = ["Ahmet Turan", 1998, (80,70,90)]
students = [studentA, studentB, studentC]
print(students)
print(students[2][1])
notortalamasi = (students[2][2][0] + students[2][2][1] + students[2][2][2])/len(students[2][2])
print(notortalamasi)




numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
print(val)
val = max(numbers)
print(val)
minval = min(letters)
print(minval)
maxval = max(letters)
print(maxval)

val = numbers[3:6]
print(val)
val = numbers[:3]
print(val)
val =  numbers[4:]
print(val)

numbers[4] = 40 
print(numbers)

numbers.append(49)
print(numbers)

numbers.insert(3, 78)
numbers.insert(-1, 52)
print(numbers)


numbers.pop() 
print(numbers)
numbers.pop(-1)
print(numbers)
numbers.remove(10)
print(numbers)


numbers.sort()
print(numbers)

letters.sort()
print(letters)

numbers.reverse()
print(numbers)

letters.reverse()
print(letters)


print(len(numbers))
print(len(letters))

print(numbers.count(78))
print(letters.count("a"), letters.count("s"))

numbers2 = numbers
print(numbers2)
numbers2.clear()
print(numbers2)


names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

names.append("Cenk")
print(names)

names.pop()
print(names)
names.extend(["Cenk"])
print(names)
names.insert(0, "Sena")
print(names)
print(names.index("Deniz"))
del names[4]
print(names)

print("Ali" in names)
print(names[::-1])
#print(names.reverse())

names.sort()
print(names)
years.sort()
print(years)

str = "Chevrolet, Dacia"
liste = str.split(",")
print(liste)

print(max(years))
print(min(years))
print(years.count(1998))

years.clear()
print(years)

marka1 = input("1.Markayı Giriniz: ")
marka2 = input("2.Markayı Giriniz: ")
marka3 = input("3.Markayı Giriniz: ")

marka = list([marka1, marka2, marka3])

print(marka)

names.insert(len(names), "Mehmet")
print(names)
names.remove("Mehmet")
print(names)

markalar = []

marka = input("Marka Giriniz: ")
markalar.append(marka)
marka = input("Marka Giriniz: ")
markalar.append(marka)
marka = input("Marka Giriniz: ")
markalar.append(marka)
print(markalar)




























