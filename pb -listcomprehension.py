# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:22:13 2023

@author: 90530
"""

#list comprehension

# n for each n in nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

liste = []

for n in nums:
    liste.append(n)
    
print(liste)


liste = [n for n in nums]
print(liste)
print([n for n in nums])

# n*n for each n in nums

liste1 = []
for n in nums:
    liste1.append(n*n)

print(liste1)

print([n*n for n in nums])
# listemap = (lambda n: n*n, nums)
# print(listemap)
# print((lambda n: n*n, nums))


# n for each n in nums if n % 2 == 0

liste2 = []
for n in nums:
    if n % 2 == 0:
        liste2.append(n)
        
print(liste2)

print([n for n in nums if n % 2 ==0])

#filter and lambda

# listefilt = filter(lambda n: n%2==0, nums)
# print(listefilt)



#(letter, num) pair for each letter in 'abcd'  and each number in '0123'

liste3 = []
for letter in "abcd":
    for num in range(4):
        liste3.append((letter, num))
              
print(liste3)

listetup = [(letter, num) for letter in 'abcd' for num in range(4)]
print(listetup)



#dict comprehension { name :hero} for each name, hero in zip(names,hero)

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

mydict = {}

for name, hero in zip(names,heros):
    mydict[name] = hero
    
print(mydict)


mydict2 = { name: hero for name,hero in zip(names,heros)}
print(mydict2)

#set comprehension

numz = [ 1, 1, 2, 1, 3, 4 ,3, 4, 3, 4, 5, 5, 6, 7, 8, 9, 7, 9, 9]

myset = set()
for n in nums:
    myset.add(n)
    
print(myset)

print({n for n in nums})



#generator expressions yiled n*n for each n in nums

def genfonk(nums):
    for n in nums:
        yield n*n
        
mygen = genfonk(nums)
for i in mygen:
    print(i)
    
mygen2 = (n*n for n in nums)
for i in mygen2:
    print(i)



































