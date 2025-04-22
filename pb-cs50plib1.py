import sys

#bunları vscodeta çalıştır


#che3ck for errors

if len(sys.argv) < 2:
    print("too fex arguments")
elif len(sys.argv) > 2:
    print("too many arguments")

#print name tags
print("hello, my name is ", sys.argv[1])   



# sys.exit
#check for errors

if len(sys.argv) < 2:
    sys.exit("too fex arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

#print name tags
print("hello, my name is ", sys.argv[1])   




#slices
#che3ck for errors

if len(sys.argv) < 2:
    sys.exit("too fex arguments")

for arg in sys.argv[1:-1]:  # -1 is not inclusive
    print("hello, my name is ", arg)    
    
    
    
   #cowsay 
import cowsay
import sys

if len(sys.argv) ==2:
    cowsay.cow("Hello, " + sys.argv[1])    

#trex
if len(sys.argv) ==2:
    cowsay.trex("Hello, " + sys.argv[1])
    
    
 #APIs

# https://itunes.apple.com/search?entity=song&limit=1&term=weezer   

"""
JSON - javascript object notation

nowadays being used  as a language agnostic format for exchanging data between computers

text based format

text is formatted in a standard way

access data in some other server and incorporate into your own program
    
"""

#requests

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())    
    
    
 #python    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    