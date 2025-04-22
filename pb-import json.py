import json

print(json.__file__)   

import requests
result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)

print(result[0]["title"])
print(result[0])
print(type(result))



print(result)

#satır satır yazdırma
for i in result:
    print(i)


for i in result:
    print(i["title"])    #sadece titlelar gelsin


print(type(result))    

for i in result:
    if i["userId"] == 1:

        
        print(i["title"])