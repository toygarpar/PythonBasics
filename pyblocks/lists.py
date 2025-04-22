users = [ "Dave", "John", "Sara"]

data = [ "Dave", 42, True ]

emptylist = []

print("Dave" in emptylist)

print(users[0])

print(users[-2])

print(users.index("Sara"))

print(users[0:2])

print(users[1:])

print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)



users.insert( 0, "Bob")
print(users) 

users[2:2] = ["Eddie", "Alex"]
print(users)

print("users[1:3] = [\"Robert\", \"JPJ\"]")
users[1:3] = ["Robert", "JPJ"]
print(users)
print("remove bob")
users.remove("Bob")
print(users)
print()
print(users.pop())
print(users)
print()

print("del user 0")

del users[0]
print(users)
print()

print("del data")
print(data)
data.clear()
print(data)

users[1:2] = ["dave"]
print(users)

users.sort(key=str.lower)
print(users)



nums = [ 4, 42 , 78, 1 , 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)
print()
print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]


print()
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([ 1, "Neil", True])
print(mylist)

#Tuples

mytuple = tuple(("Dave", 42, True))

anothertuple = (1 , 4, 2, 8 , 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

print()
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)



print()
(one, *two, hey) = anothertuple
print(anothertuple)
print(one)
print(two)
print(hey)

print(anothertuple.count(2))