import math 

#literal assignment

first = "Toygar"
last = "Par"

print(type(first))
print(type(first)  == str)
print(isinstance(first, str))

#constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza)  == str)
print(isinstance(pizza, str))

#concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to string

decade = str (1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade +"s."
print(statement)

multiline= '''
deneme

deneme

deneme 123
'''
print(multiline)

#escaping special characters

sentence = "I\'m back at work!\tHey!\n\nWhere\'s this at\\located?"
print(sentence)


print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("123", "321"))
print(multiline)

print(len(multiline))
multiline += ""
print(len(multiline))
multiline = "             " + multiline
print(len(multiline))
print()
print(len(multiline.strip()))
print(len(multiline.rstrip()))
print(len(multiline.lstrip()))



print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

for i in range(8):
    for j in range(8):
        
      
        print("#".rjust(8, " "), end="")
        j = i + 1

        for k in range(8):
            print(".".ljust(8, " "), end="")
            k = j - 1

print()
        
print(first[1])
print(first[1:-1])
print(first[-1])
print(first[1:])

print(first.startswith("T"))
print(first.endswith("z"), first[4:].isdigit())



#boolean data type

myvalue = True

x = bool(False)

print(type(x))

print(isinstance(myvalue, bool))


#numeric data types

price = 100

bestprice= int(80)

print(type(price))

print(isinstance(bestprice, int))

gpa = 3.28
y = float(1.14)
print(type(gpa))

#complex type

compv = 5 + 3j
print("Complex Value")
print(type(compv))
print(compv.real)
print(compv.imag)


print(abs(gpa))
print(abs(gpa * -1))
print(abs(gpa) * -1)

print(round(gpa))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


zipcode = "100001"
zipv = int(zipcode)
print(type(zipv))