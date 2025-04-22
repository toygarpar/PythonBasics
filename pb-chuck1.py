#constants
from asyncio.base_futures import _FINISHED


print(123)

print(98.6)

print("Hello World")

#variables
a = 35.0
b = 12.50
c = a * b
print(c)


#variables using mnemonic names
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

#sentences or lines -  variable operator constant reserved word
x = 2
x = x + 2
print(x)

#Assignment Statement
x=0.6
x = 3.9 * x *(1 -x)
print(x)

#numeric expressions
print("numeric expressions")
xx = 2
xx = xx + 2 
print(xx)

yy = 440 * 12
print(yy)

zz = yy /1000
print (zz)

jj = 23
kk = jj % 5
print(kk) 

print (4 ** 3)

x = 1 + 2 ** 3 /4 * 5
print (x)

ddd = 1 + 4
print(ddd)

#concatenate
eee = "hello " + "there"
print (eee)

#type conversions
print(float(99) + 100)

i = 42
print (type(i))
f = float(i)
print(f)

#integer division
print()
print("integer division")
print(10/2)
print(9/2)
print(99/100)
print(10.0/2.0)
print(99.0/100.0)

#string conversions
print()
print("string conversions")
sval = "123"
print(type(sval))
ival  = int(sval)
print(type(ival))
print (ival + 1)


# #user input
# print()
# print("user input")
# nam = input("who are you? ")
# print("welcome", nam)


# #converting using input - converting string to a number using a type conversion function

# inp = input("europe floor?") #input gives you a string so it has to converted to integer
# usf = int(inp) + 1 #conversion to integer
# print ("US floor", usf)


# #get the name of the file and open it

# name = input("Enter the file: ")
# handle = open( name, "r")

# #count word frequency

# counts  = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts [words] = counts.get(word ,0) + 1

        
# #find the most common word

# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count


# #All done
# print(bigword, bigcount)


#conditional steps
print()
print("conditional steps")
x = 5
if x < 10:
    print("smaller")
if x > 20:
    print("bigger")

print("FINISHED")       

#comparison operators
print()
print("comparison operators")

x = 5

if x == 5:
    print("equals 5")

if x >= 4 :
    print ("greater than 4")

if x >= 5:
    print("greater then or equals to 5")

if x < 6:
    print("less than 6")

if x <= 5:
    print("less than or equals 5")

if x != 6:
    print("not equal 6")            

#one way decisions
print()
print("one way decisions")
x = 5
print("before 5")
if x ==5:
    print("is 5") 
    print("is still 5") 
    print("Third 5")

print("Afterwards 5")
print("before 6")
if x == 6:
    print("is 6") 
    print("is still 6") 
    print("Third 6")

print("Afterwards 6")        


#indentation

print()
print("indentation example")

x = 5
if x > 2:
    print("bigger than 2") #increase the indent
    print("still bigger")   #maintain the indent
print("done with 2")    #decrease the indent


for i in range(5):
    print(i)
    if i > 2:
        print("bigger than 2")  #block within a block
    print("done with i", i)
print("all done")        


#nested decisions
print()
print("nested decisions")

x = 42
if x > 1:
    print("More than 1")
    if x < 100:
        print("less than 100")
print("all done")       


#two-way decisions with else
print()
print("2 way decisions with else")

x = 4
if x > 2:
    print("bigger")
else:
    print("smaller")

print("all done")    

#multi-way decisions
print()
print("multi-way decisions with else/elif")
if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("large")
print("all done!")

#multiway many elifs

x = 5
if x < 2:
    print("small")
elif x < 10:
    print("medium")
elif x < 20:
    print("big")
elif x < 40:
    print("large")
elif x < 100:
    print("huge")
else:
    print("ginormous")

#multiway puzzles

if x < 2:
    print("below 2")
elif x>=2:
    print("two or more")
else: 
    print("something else") #would neever run this code
        

if x < 2:
    print("below 2")
elif x < 20:
    print("below 20")
elif x < 10:
    print("below 10") #would neever run this code
else:
    print("something else") #would neever run this code

#try and except structure

astr = "Bob"
try:
    print("Hello")
    istr = int(astr)
    print("There")

except:
    istr = -1

print("Done", istr)

#sample try/except

# rawstr = input('enter a number:')
# try:
#     ival = int(rawstr)
# except:
#     ival = -1

# if ival > 0:
#     print("nice work")
# else:
#     print("not a number")


#FUNCTIONS : stored and reused steps
print()

def thing():  #definition of a function
    print("hello")
    print("fun")

thing() #invoking a function
print("zip")
thing()

#example built in function

big = max("Hello world")
print(big)

tiny = min("Hello world")
print(tiny)

#type conversions

print (float(99/100))
i = 42
print(type(i))
f = float(i)
print(float(i))
print(type(float(i)))
print(f)
print(type(f))
print(1 + 2 *float(3) / 4 -5 )

#string conversions

sval = "123"
print(type(sval))
ival= int(sval)
print(type(ival))
print(ival + 1)


#building our own functions

def print_lyrics():
    print(" I am a lumberjack and I'm Okay.")
    print(" I sleep all night and I work all day.")

x = 5
print("Hello")

print("Yo")
x = x + 2
print(x)
print_lyrics()


#parameters

def greet(lang):
    if lang == 'es':
        print("hola")
    elif lang == 'fr':
        print("bonjour")
    else:
        print("hello")


greet('es')
greet('fr')
greet('en')


#return value

def greet(lang):

    if lang == 'es':
        return "hola"
    elif lang == 'fr':
        return "bonjour"
    else:
        return "Hello"



print(greet('es') , 'Sally')
print(greet('fr'), 'Michael')
print(greet('en'), 'Glenn')

#multiple parameters/arguments

def addtwo(a, b):
    added = a + b
    return added

x= addtwo(3, 5)
print(x)


#Loops and Iteration



#Repeated Steps

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!!")
print(n)


#breaking out of a loop

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('DOne!')


#finishing an Iteration with continue

# while True:
#     line = input("> ")
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print("Done")



#A simple definite loop
xxx = [ 5, 4, 3, 2, 1]
for s in xxx :
    print(int(s))
print("Blastoff!!")


#a definite loop with strings

friends = ["Joseph", "Glenn","Sally"]
for friend in friends:
    print("Happy New Year:", friend)
print("finito")

#looping through a set - basic loop

print("Before")
for thing in [9, 41, 12, 3 , 74 , 15]:
    print(thing)
print("After")

#find the largest number

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3 , 74 , 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(largest_so_far, the_num)

print("After", largest_so_far)


#counting in a loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3 , 74 , 15]:
    zork = zork + 1
    print(zork , thing)
print("After", zork)

#summing in a loop

zork = 0
print("Before" , zork)
for thing in [9, 41, 12, 3 , 74 , 15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)

#finding the average in a loop

count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3 , 74 , 15]:
    count = count + 1
    sum = sum + value
    print( count, sum , value)
print("After", count, sum, sum / count )

#filtering in a loop - we use an if statement in the loop to catch/fiter the values we are looking for
print("Before")
for value in [9, 41, 12, 3 , 74 , 15]:
    if value > 20:
        print("Large Number", value)
print("After")


#search using a boolean variable -just want to search and know if a value is found, use a variable starts 
# at False amd is set to True as soon as we find what we are looking for

found =  False
print("Before", found)
for value in [9, 41, 12, 3 , 74 , 15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)

#how to find the smallest value - the first time thru the loop smallest is None, so we take the first value to be the smallest

smallest = None #none is used to indicate emptiness, non-existence
print("Before")
for value in [9, 41, 12, 3 , 74 , 15]:
    if smallest is None: #python has an "is" operator that can be used in logical expressions, implies" is the same as" stonger than ==
        smallest = value # "is" demands sames type and value, use it on true or flase or none
    elif value < smallest:
        smallest = value
    print(smallest, value)

print("After", smallest)


#string data type

str1 = "Hello" #concatenate
str2 = 'there'
bob = str1 + str2
print(bob) 
str3= "123"
print(int(str3) + 1) #conversion to integer
x = int(str3) + 1
print(x +1)

#reading and converting

# name = input("Enter Name: ")
# print(name)
# apple = input("Enter: ")
# x = int(apple) - 10
# print(x)

#looking inside strings

fruit ="banana"
letter = fruit[1]
print(letter)

x = 3
w =fruit[x - 1]
print(w)

#length of a string using len function

fruit = "avocado"
print(len(fruit))

#looping thru strings - while loop
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

#for loop - the iteration variable is completely taken care of by the for loop
fruit = "banana"
for letter in fruit:
    print(letter)

#looping and counting
word = "banana"
count = 0 #set the counter to 0
for letter in word:
    if letter == "a":
        count +=1
    print(count)

#Slicing Strings

s = "Monty Python"
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])


#string concatenation
a = "Hello"
b = a + "There"
print(b)
c= a + " " + "There"
print(c)

# in operator

fruit = "banana"
if "a" in fruit:
    print("Found it")

#strin comparison

if word == "banana":
    print("all right, bananas")

if word < "banana":
    print("your word" + word + "comes before bananas")
elif word > "banana":
    print("your word" + word + "comes after bananas")
else:
    print("all right, bananas")

#string library

#lowercase function - lower()
greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print("Hi There".lower())

stuff = " Hello World"
print(dir(stuff))

#searching a string

fruit = "banana"
pos = fruit.find("na")
print(pos)
aa = fruit.find("z")
print(aa)

#uppercase
greet = "Hello Bob"
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

#search and replace

greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)

#Stripping Whitespace

greet = "   Hello Bob   "
greet.lstrip()
print(greet.lstrip())
greet.rstrip()
print(greet.rstrip())
print(greet.strip())

line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("p"))

#parsing and extracting

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos =  data.find("@")
print(atpos)
sppos = data.find(" ", atpos)
print(sppos)
host = data[atpos+1 :sppos]
print(host)


#newline character

stuff = "Hello\nWorld"
print (stuff)
print(len(stuff))


#counting lines in a file

fhand = open("mbox.txt")
count = 0 #set variable count to 0
for line in fhand:
    count = count + 1
print("line count:", count)

#reading the whole file
fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])

#searching thru a file
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From:"):
        print(line)

#searching thru a file -gets rid of the blank lines from the lines that start with "from:"
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

#or skipping with continue
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)

#using in to select lines
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not "uct.ac.za" in line:
        continue
    print(line)


#prompt for a file name

# fname = input("Enter the file name: ")
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith("Subject:"):
#         count = count + 1
# print("there were", count, "subject lines in", fname)

#bad file names

# fname = input("Enter the file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("file can not be opened", fname)
#     quit()
# count = 0
# for line in fhand:
#     if line.startswith("Subject:"):
#         count = count + 1
# print("there were", count, "subject lines in", fname)


#LISTS

#example

arkadas = ["Holly", "Molly","Dolly"]
print(arkadas)
print(type(arkadas))
#examples

print([1, 24, 76])
print(["red", "white", "blue"])
print(["red", 24, 98.6])
print([1, [5 , 6], 7])
print([])

#Lists and Definite Loops 

friends = ["Joseph","Glenn", "Sally"]
for friend in friends:
    print("Happy New Year, ", friend)
print("Donzo!")

z =  ["Joseph","Glenn", "Sally"]
for x in z:
    print("Happy New Year, ", x)
print("Donzo!")

#Looking İnside Lists
friends = ["Joseph","Glenn", "Sally"]
print(friends[1])

#lists are mutable

fruit = "Banana"
x = fruit.lower()
print(x)

#change element at index 2 from 26 to 28
lotto = [2, 14, 26 , 41, 63 ]
print(lotto)
lotto[2] = 28
print(lotto)