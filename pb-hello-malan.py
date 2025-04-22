print("hello, world!")

#functions - actions or verbs that do stuff for you in the program
#argument - an input to a function that somehow influences its behavior
#side-effects - what these functions do
#bugs - mistake in a program

def my_map(myfunc, iter):
    result = []
    for item in iter:
        newitem = myfunc(item)
        result.append(newitem)
    
    return result


nums =[ 1 , 2 , 3 , 4]

cubed = my_map(lambda x : x ** 3, nums)

print(cubed)


def for_loop(n):
    my_list = []
    for x in range(n):
        my_list.append(x)
    return my_list



zet = for_loop(10)
print(zet)

cubed2 = my_map(lambda x : x ** 3, zet)
print(cubed2)

z = [s for s in range(100)]
print(z)
print(hash(z))