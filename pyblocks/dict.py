band = {
    "vocals": "Plant",
    "guitar": "Page"

}

band2 = dict(vocals="Plant", guitar="Page")


print(band)
print(band2)

print(type(band))
print(len(band))

print(band["vocals"])
print(band.get("guitar"))
print()
#list all keys
print(band.keys())
#list all values
print(band.values())
#list key value pairs as tuples
print(band.items())
#verify if a key exists
print("guitar" in band)
print("ass" in band)
#change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)
print()
#remove items

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())
print(band)
print()


#delete and clear

band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

#create a reference

band2 = band
print("bad copy")
print(band2)
print(band)

band2 =  band.copy()
band2["drums"] = "Dave"
print("Good copy")
print("Band:", band)
print("Band2:", band2)

#dict() constructor function
band3 = dict(band)
print(band3)

#nested dicts
print("Nested Dicts")

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

print()
#sets
print("Sets")
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)

nums = {1, True, 2, False, 3, 4, 0}
print(nums)
print(2 in nums)

nums.add(8)
print(nums)

#merge two sets

one = {1 ,2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

kume1 = {1, 2, 3}
kume2 = {2, 3, 4}

kume1.intersection_update(kume2)
print(kume1)

kume1 = {1, 2, 3}
kume2 = {2, 3, 4}
kume1.symmetric_difference_update(kume2)
print(kume1)