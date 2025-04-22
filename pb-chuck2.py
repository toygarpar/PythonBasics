#How long is a list?

greet = "Hello Bob!"
print(len(greet))

x = [ 1, 2 ,"joe", 99]
print(len(x))

#using the range function
print(range(4))

friends = [ "joseph", "glenn", "sally"]
print(len(friends))
print(range(len(friends)))

#a tale of two loops
for friend in friends:
    print("Happy New Year:", friend)

for i in range(len(friends)):
    friend = friends[i]
    print("Happy Fucking New Year:", friend)

#concatenating lists using +

a = [ 1, 2, 3]
b = [4, 5, 6]
c= a + b
print(c)
print(a)
print(b)

#list slicing

t = [9, 41, 12, 3 , 74, 15]
print(t[1:3])
print(t[:4])
print(t[:])

#list methods

x= list()
print(type(x))
print(dir(x))

#building a list thru scratch

stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)

#is something in a list

some = [1, 9, 21, 10, 16]
if 9 in some:
    print("Fuck Yeah!")

print(9 in some)
print(15 in some)
print(20 not in some)

#lists are in order and sort method

friends = ["Joseph", "Glenn", "Sally"]
friends.sort()
print(friends)
print(friends[1])


#built-in functions and lists

nums = [3, 41, 12, 9 ,74 ,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#a loop to find avg - uses less memory

# total = 0
# count = 0
# while True:
#     inp = input("Enter a number: ")
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value 
#     count= count + 1

# average = total /count
# print("Average", average)
      
#list avg - building loops to do avg using a list -uses more memory

# numlist = list() #assign an empty list
# while True:
#     inp = input("Enter a number: ")
#     if inp == 'done' : break
#     value = float(inp) #converts string to float
#     numlist.append(value) #adds to the list

# average = sum(numlist) / len(numlist)
# print("Average: ", average)


#best friends : strings and lists

abc = "With three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)

#split action - uses spaces to split unless specify a character to use in the splitting
line = " A lot      of spaces"
etc = line.split()
print(etc)

line =  "first;second;third"
thing = line.split()
print(thing)
thing = line.split(";")
print(thing)
print(len(thing))

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split() #split the words from the line
    email = words[1] #define email as variable
    print(email)
    pieces = email.split("@") #split email at @
    print(pieces[1]) #print email address

han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    wds = line.split()
    #guardian
    if len(wds) < 3 or wds[0] != 'From': 
        continue
    print(wds[2])
    

#Dictionaries

purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print (purse)

print(purse["candy"])
purse["candy"] = purse["candy"] + 2
print(purse["candy"])
print(purse)

#List vs Dictionary

lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst[0])
print(lst)

ddd = dict()
ddd["age"] = 21
ddd["course"] = 182
print(ddd)
ddd["age"] = 23
print(ddd)

#dict literals (constants)

jjj= {"chuck" : 1, "fred" : 42, "jan" :100}    
print(jjj)
ooo = dict()
print(ooo)

#dict - counting  most common name - making a histogram
ccc = dict()
ccc["csev"] = 1
ccc["cwen"] = 1
print(ccc)
ccc["cwen"] = ccc["cwen"] + 1
print(ccc)
print("caze" in ccc)

#add a new name or add 1 to counter
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

#simplified counting with get()

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]

for name in names:
    counts[name] = counts.get(name, 0) + 1 
print(counts)

#counting pattern

# counts = dict()
# print("Enter a line of text: ")
# line = input(" ")
# words = line.split()
# print("Words:", words)

# print("Counting...")
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print("Counts", counts)

#definite loops and dictionaries

counts = {"chuck":1, "fred": 42, "jan": 100}
for key in counts:
    print(key, counts[key])

print(counts["chuck"])

#Retrieving a lists of Keys and Values
jjj= {"chuck":1, "fred": 42, "jan": 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items()) #items in tuples

#we loop thru key-value pairs using two iteration variables
jjj= {"chuck":1, "fred": 42, "jan": 100}
for aaa,bbb in jjj.items():
    print(aaa, bbb)


#count words in files

#name = input("Enter file :")
#handle = open(name) #open the file name entered and assign to handle
handle = open("words.txt")

counts = dict() #create an empty dict
for line in handle:
    words = line.split() #split the words in line
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #add new entries to dict and count each time present


bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

    print(bigword, bigcount)

#frequency of a word and whether it's new or existing

# fname = input("E>nter file:")
# if len(fname) < 1 : fname = "words.txt"
# hand = open(fname)
hand = open("words.txt")

di = dict()

for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)

    for w in wds:
        #print(w)
        #print("***", w, di.get(w, -99))
        # oldcount = di.get(w, 0)
        # print(w, "old", oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        di[w]= di.get(w, 0) + 1 
        #print(w, "new", di[w])



    # if w in di:
    #     di[w] = di[w] + 1
    #     print("**existing")
    # else:
    #     di[w] = 1
    #     print("**new**")
    # print(w, di[w])

print(di)    

#find the most common word
largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k
print("Done", theword, largest)

        

#TUPLES
print("TUPLES>>>>>>>>>>>>>>>>>")
x = ("Glenn", "Sally", "Joseph")
print(x[2])
y = (1, 9, 2)
print(y)
for iter in y:
    print(iter)
#list example compared to tuple - mutable. tuples are immutable
x = [9, 8, 7]
print(x)
x[2] = 6
print(x)

l = list()
print(dir(l))

t = tuple()
print(dir(t))

#tuples and assignment

(x, y) = (4, "fred")
print(x,y)
print(y)
print(x)

(a, b) = (99, 98)
print(a,b)
print(a)
print(b)

#tuples and dictionaries
d= dict()
d["csev"] = 2
d["cwen"] = 4

for (k, v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(("Jones", "Sally") < ("Jones", "Sam"))
print(("Jones", "Sally") > ("Adams", "Sam"))

#sorting lists of Tuples
d = {"a": 10, "b": 1, "c": 22}
print(d.items())
print(sorted(d.items()))
t = sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print (k,v)


#sort by values instead of keys
c = {"a": 10, "b": 1, "c": 22}
print(c)
tmp = list()
for k,v in c.items():
    tmp.append((v, k)) #append them in a list by sorting by value instead of keys
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

#top ten most common words
fhand = open("mbox-short.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val ,key) #making anew tuple
    lst.append(newtup) #append that tuple to the list

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

#even a shorter version
c = {"a": 10, "b": 1, "c": 22}
print( "Shorter Version:", sorted([ (v,k)for k,v in c.items()])) #using lambdas - list comprehension
lst = sorted([ (v,k)for k,v in c.items()])
print(lst)


#severance hodja example
#find the most common words and frequency
hand = open("words.txt")

di= dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

print(di)
#--------------------------------------------

x= sorted(di.items())
print(x[:5])

tmp = list() #make a flipped list
for k,v in di.items():
    print(k ,v )
    newtuple = (v ,k)
    tmp.append(newtuple)

print("Flipped", tmp)

tmp = sorted(tmp, reverse=True) #then sort the flipped list

print("Sorted", tmp[:5])

for v, k in tmp[:5]:
    print(v,k)

#REGULAR EXPRESSIONS
#smart extractions thru wild card expressions

#using re.search() and find()

hand = open("mbox-short.txt")

for line in hand:
    line = line.rstrip()
    if line.find("From:") >= 0:
        print(line)

import re

hand = open("mbox-short.txt")

for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)

#using re.search() like starswith()

for line in hand:
    line = line.rstrip
    if line.startswith("From:"):
        print(line)

for line in hand:
    line =line.rstrip
    if re.search("^From:", line):
        print(line)

#searching one or more digits/letters of character
import re
x = " My 2 favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print( y )
y = re.findall("[AEIOU]+", x) #returns an empty list
print( y )

#greedy matching - the repeat characters * and + push outward in both directions 
# to match the largest possible string
#anytime it has a choice, it chooses the longer
import re
x = "From: Using the : character"
y = re.findall("^F.+:", x)
print (y)
#non-greedy - not greedy by using(adding) ?
z = re.findall("^F.+?:", x)
print(z)

#fine-tuning string extraction - using \S non whitespace character and +(one or more)
x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("\S+@\S+", x)
print(y)
#or
y = re.findall("^From (\S+@\S+)", x)
print(y)

#string parsing examples
#previously what we have done

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ", atpos)
print(sppos)
host = data[atpos +1 : sppos]
print(host)

#then we used double split pattern
words = data.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])

#regex version
import re
lin = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y= re.findall("@([^ ]*)", lin) # [^ ] means not a blank character
z = re.findall("^From .*@([^ ]*)", lin)
evencooler = re.findall("^From .*@([^ ]*)", lin)
print(y)
print (z)
print(evencooler)

#spam confidence

import re
hand = open("mbox-short.txt")
numlist = list()
for line in hand:
    line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print("MAximum:", max(numlist))


#escape character - if you want to special regular expression to just behave normally
#prefix it with \
import re
x = "We just received $10.00 for cookies."
y = re.findall("\$[0-9.]+", x)
print(y)


