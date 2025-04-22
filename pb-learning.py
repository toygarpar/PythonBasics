import math
print(math.pi)
print(math.sqrt(85))

import random
print(random.random())
print(random.choice([1,2,3,4]))

S = "Spam"
print(len(S))
print(S[0])
print(S[1])
print(S[-1])
print(S[-2])
print(S[len(S)-1])
print(S[1:3])
print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])
print(S+"xyz")
print(S * 8)
print( "z" + S[1:])
print(S.find("pa"))
print(S.replace("pa", "xyz"))
print(S.upper())
print(S.isalpha())

line = "aaa,bbb,ccccc,dd"
print(line.split(","))

line = "aaa,bbb,ccccc,dd\n"
print(line.rstrip())

print("%s, eggs, and %s" % ("spam", "Spam!")) #formatting expression
print("{0}, eggs, and {1}".format ("spam", "Spam!"))  #formatting method

# print(dir(S))
# print(help(S.replace))

print(ord("\n"))








