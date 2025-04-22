#break and continue

name = "Toygar Par"

for letter in name:
    if letter == "a":
        break
    print(letter)
    
for letter in name:
    if letter == "a":
        continue
    print(letter)
    
print([letter for letter in name ])



x = 0

while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)



# 1 -100 kadar tek sayıları olmaadan toplamı

x = 0
result = 0

while x <= 100:
    x += 1
    if x % 2 ==1:
        continue
    result += x
    
print(f"toplam: {result}")






#↨range

liste = [1, 2, 3]

for item in liste:
    print(item)
    
for item in range(50,100, 20):
    print(item)
    
print(list(range(50,100, 20)))


#♣enumurate

index = 0
greeting = "Hello There"

for letter in greeting:
    print(f"index : {index}, letter: {letter} or {greeting[index]}")
    index += 1
 
index = 0    
greeting = "Hello There"
for item in enumerate(greeting):
    print(item)
    print(f"index : {index}, letter: {item}")
    index += 1
    
for item in enumerate(greeting, 3):
    print(item)  
    
    
 #zip   
    
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = [100, 200, 300 ,400 , 500]


print(list(zip(list1, list2, list3)))
    
print([ (a, b, c) for a,b,c in (zip(list1, list2, list3))])

for item in zip(list1, list2, list3):
    print(item)
    
for a, b, c in zip(list1, list2, list3):
    print(a, b, c) 
    print([(a, b, c)]) 
    
#list comprehension    
    
numberz = []    
for x in range(10):
    numberz.append(x)
print(f"regular for loop : {numberz}")
    
numbers = [x for x in range(10)]
print(f"list comprehension: {numbers}")



for x in range(10):
    print(x**2)

print([x**2 for x in range(10)])    


print([x*x for x in range(10) if x % 3==0])





mystring = "Hello"
mylist = []

for letter in mystring:
    mylist.append(letter)
    
print(mylist)


years =  [1983, 1999, 2008, 1956, 1986]

ages = [ 2023-year for year in years]

print(ages)
    


print([x if x%2==0 else "Tek" for x in range(1, 10)])    

sonuc = []
for x in range(3):
    for y in range(3):
        sonuc.append((x, y))
print(sonuc)
        
        

print([ (x, y) for x in range(3) for y in range(3)])




import random

number  = random.randint(1, 10)
life = int(input("kaç hak istiyorsunuz? "))
hak = life
count = 0


while hak > 0:
    hak -= 1
    count += 1
    tahmin = int(input("Tahmininiz ne? "))
    
    
    if tahmin == number:
        print(f"Doğru sayıyı {count}. defada bildiniz: {tahmin}, Toplam puanınız: {100 - (100/life) * (count-1) }")
        break
    elif tahmin > number:
        print("aşağı")
    else:
        print("yukarı")
        
        
    if hak == 0:
        print(f"haklarınız bitti, tutulan sayı : {number}")
        
        
        
        
        
num = int(input("Sayı giriniz: "))

asalmi = True

if num  == 1:
    asalmi = False
    
for i in range (2, num):
    if num % i == 0:
        asalmi = False
        break
        
if asalmi:
    print("asal sayıdır")
else: 
    print("asal sayı değildir")
    
    
    
    
    
student = ["ali", "veli", "kırkdokuz", "elli"]

print([ x for x in student])

for i in student:
    print(i)
    


#maaş zamları    
    
salary = [1000 , 2000, 3000, 4000, 5000]

def  new_wage():
    for x in salary:
        if x >= 3000:
            print(x*10/100 + x)
        else: 
            if x < 3000:
                print(x*20/100 +x)
                
new_wage()                
        
    
def harfsay(x):
    return len(x)
    5*5

    
harfsay("merhaba")   


    
    
    
    

    