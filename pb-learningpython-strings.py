# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 00:40:25 2024

@author: 90530
"""


#strings
s = "Spam"

len(s)

s[0]
s[1]
s[-1]
s[-2]
s[3]
s[len(s)-1]
s[1:3]


s[1:]
s
s[0:3]
s[:3]
s[:-1]
s[:]

s
s +"xyz"
s
s * 8


#numberz

123 + 322
1.5 * 4


len(str(2 ** 1000000))

repr(3.1415 * 2)

print(3.1415 * 2)
repr?

import math
math.pi

math.sqrt(95)


import random
random.random()

random.choice([1, 2, 3,4])

s2= "z" + s[1:]
s2

k = "kapitülasyon"
liste = list(k)
liste
liste[1]= "A"
"".join(liste)


zx = bytearray(b"spam")
zx.extend(b"eggs")
zx
zx.decode()

s
s.find("pa")
s.replace("pa", "XYZ")
s


line = "aaa,bbb,ccc,ddd"
line.split(",")



s
s.upper()
s.isalpha()
s.isdigit()

line1 = "aaa,bbb,ccc,ddd "
line1.rstrip().split(",")



#strings support an advance substitution op known as formatting
#formatting

"With a  little %s and %s numbing me" % ("sweet", "simple")  #formatting expression

"With a littele {0} and {1} numbing me".format("sweet", "simple") #formatting method

"With a little {} and {} numbing me".format("sweet", "simple")  #formatting method, numbers optional


#seperators, decimal digits

"{:,.4f}".format(365258794.21564545456) 

"%.2f" % (3.14159)

"""
the built-in dir function. This
function lists variables assigned in the caller’s scope when called with no argument;
more usefully, it returns a list of all the attributes available for any object passed to it.

The dir function simply gives the methods’ names. To ask what they do, you can pass
them to the help function:
"""

d = "Toygar Par"
dir(d)

help(d.replace)
help(str.replace)

#other ways to code strings

a = "A\nB\tC" # \n is end-of-line, \t is tab
len(a) # Each stands for just one character
print(a)
ord("\n") # \n is a byte with the binary value 10 in ASCII

aa = "A\0B\0C" # \0, a binary zero byte, does not terminate string
len(aa)
print(aa)


"""
Python allows strings to be enclosed in single or double quote characters—they mean
the same thing but allow the other type of quote to be embedded with an escape (most
programmers prefer single quotes). 

triple quotes (single or double)—when this form is used, all the lines are concatenated
together, and end-of-line characters are added where line breaks appear. 
"""

aaa = """
aaaaaaaaaaaa

bbbbbbbbbbb'''bbbbbbbbbbbbbbbbbbbbbbb""bbbbbbbbb'bbbb
ccccccccccc
"""
print(aaa)



print(r"C:\deneme\deneme123") #Python also supports a raw string literal that turns off the backslash escape mechanism.






















