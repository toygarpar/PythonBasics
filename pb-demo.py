x = input("1.sayÄ±: ")
y = input("2.sayÄ±: ")

print(type(x))
print(type(y))
toplam = int(x) + int(y)
print(toplam)



x = 5

y = 2.5

name = "Ã‡Ä±nar"

isOnline =  True

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

x = float(x)
print(type(x))
print(x)

y = int(y)
print(type(y))
print(y)

result = x + y
print(type(result))
print(result)


result = str(x) + str(y)
print(type(result))
print(result)

isOnline =str(isOnline)
print(type(isOnline))
print(isOnline)

isOnline = False
isOnline = int(isOnline)
print(type(isOnline))
print(isOnline)


pi = 3.14
r = float(input("input r: "))
alan = pi*r**2
cevre = 2*(pi*r)
print(f"Alan: {alan:.2f}")
print(f"Ã‡evre: {cevre:.2f}") 



name = "Toygar"

lastname = "Par"

age = 49

print("My name is " + name + " " + lastname + ". And \n I am " + str(age) + " years old.")

greeting = ("My name is " + name + " " + lastname + ". And \n I am " + str(age) + " years old.")

print(greeting)

length = len(greeting)


print(len(greeting))
print(greeting[0])
print(greeting[length-1])
print(greeting[-1])
print(greeting[2:5])
print(greeting[3:7])
print(greeting[2:40:2])


v = "toygar"
print(v[1:5])


#string formatlama

print("My name is {} {}.".format(name, lastname))
print("My name is {0} {1}.".format(name, lastname))
print("My name is {1} {0}.".format(name, lastname))
print("My name is {l} {n}, and I'm {a} years old".format(n=name, l=lastname, a=age))


result = 200/700
print("the result is {:.2f}".format(result))
print("the result is {r:2.3}".format(r=result))


print(f"My name is {name} {lastname}, and I'm {age} years old")


website= "http://www.sadikturan.com"

course = "Python Kursu: Baþtan Sona Python Programlama Rehberiniz (40 saat)"

print(len(course))
print(website[7:10])
print(website[-3:])
print(course[50:])
print(course[:15])
print(course[::])
print(course[::-1])
print(course[::5])

s = "Hello, world".title()
print(s)

t = "abc" * 3
print(t)


message = "Hello There. My name is Toygar Par"

#message = message.upper()
#message = message.lower()
#message = message.title()
#message = message.capitalize()
print(message)



m = " Hello There. My name is Toygar Par"
# m = m.strip()
# print(m)
# m = m.split()
# print(m)
# print(m[1])

# m = "*".join(m)
# print(m)





# index = m.find("Toygar")
# print(index)

# isFound = message.startswith("H")
# isFound = message.endswith("H")
# print(isFound)

# m = m.replace("Toygar", "Tiger")
# print(m)

m = m.center(50, "*")
print(m)

q = " Hello World "
q = q.strip()
print(q)

w = "http://www.sadikturan.com"
# w = w.replace("http://www.","").replace(".com","")
# print(w)
# w = w.lstrip("/:pth")
# print(w)
# w =w.strip("w.moc")
# print(w)

co = "Python Kursu: Baþtan Sona Python Programlama Rehberiniz (40 saat)"

# d= co.rfind("Python")
# e = co.index("Python")
# print(d, e)
# co = co.lower()
# print(co)

# index = w.find("a")
# print(w.count("a"))
result = w.count("a")
sonuc = w.count("www", 0, 10)

print(result)
print(sonuc)


p = w.startswith("www")
print(p)


r = w.endswith("com")
print(r)

l = "Contents"
l= l.center(50, "*")
print(l)

l = "Contents"
l= l.ljust(50, "*")
print(l)

l = "Contents"
l= l.rjust(50, "*")
print(l)




cop = co.replace(" ", "-")
print(cop)


q = " Hello World "
q =q.replace()


co = "Python Kursu: Baþtan Sona Python Programlama Rehberiniz (40 saat)"
a = co.isalpha()
b = co.isdigit()
n = "123".isdigit()
mn = "Hello".isalpha()

print(a)
print(b)
print(n , mn)

co = "Python Kursu: Baþtan Sona Python Programlama Rehberiniz (40 saat)"
co = co.split(" ")
print(co)
print(co[5])























