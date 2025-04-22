#function exercise

def times(x, y): # Save the result object
    return x * y

x = times(3.14, 4)
x

times("hi", 4) # Functions are "typeless"




def intersect(seq1, seq2):
    res = []
    
    for x in seq1:
        if x in seq2:
            res.append(x)
            
            
    return res


s1 = "kapitülasyon"
s2 = "mastürbasyon"

son = intersect(s1, s2)
print(son)

print([x for x in s1 if x in s2])








def func():
    x = 4
    action = (lambda n: x ** n)
    return action



x = func()

print(x(2))

func()







def makeActions():
    acts = []
    for i in range(5): # Tries to remember each i
        acts.append(lambda x: i ** x) # But all remember same last i!
    return acts


acts = makeActions()
acts[0]


acts[0](2)



def tester(start):
    
    state = start
    def nested(label):
        print(label, state)
        state += 1
        
    return nested

a =tester(0)


a("deneme")
a("deneme123")








def tester(start):
    
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
        
    return nested

b =tester(0)


b("deneme")
b("deneme123")







class Tester:
    def __init__(self, start):
        self.state = start
        
    def nested(self, label):
        print(label, self.state)
        self.state += 1 
        
        
c = Tester(0)

c.nested("deneme")
        
c.nested("2. deneme")


d = Tester(100)        
d.nested("deneme")

c.nested("3. deneme")

d.nested("deneme123")

d.state
c.state





class Tester2:
    def __init__(self, start):
        self.state = start
        
    def __call__(self, label):
        print(label, self.state)
        self.state += 1 


e = tester(1000)
e("like a call function")  # So .nested() not required


e.state






#The output here is 'deneme', because the function references a global variable in the enclosing module

x = "deneme"
def func():
    print(x)
    
func()    



#use of non-local



def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)

func()



#returns none just prints deneme
"""
The output here is 'deneme' again because assigning the variable inside the function
makes it a local and effectively hides the global of the same name. The print state-
ment finds the variable unchanged in the global (module) scope.
"""

x = "deneme"

def func():
    x = "zort"
    
func() 
print(x)   


#func printz zort print, print x deneme


"""
 It prints 'zort' on one line and 'deneme' on another, because the reference to the vari-
able within the function finds the assigned local and the reference in the print
statement finds the global.
"""

x = "deneme"

def func():
    x = "zort"
    print(x)
    
func() 
print(x)  



# x = deneme is overwritten by x = zort
"""
This time it just prints 'zort' because the global declaration forces the variable as-
signed inside the function to refer to the variable in the enclosing global scope.
"""




x = "deneme"

def func():
    global x
    x = "zort"
    
    
func() 
print(x)  



"""
The output in this case is again 'zort' on one line and 'deneme' on another, because
the print statement in the nested function finds the name in the enclosing func-
tion’s local scope, and the print at the end finds the variable in the global scope.
"""

x = "deneme"

def func():
    x = "zort"
    def nested():
        print(x)
    nested()
    
    
func() #zort
print(x)  #deneme




"""
the assignment to X inside the nested function changes
X in the enclosing function’s local scope. 
"""

def func():
    x = "zort"
    def nested():
        nonlocal x
        x = "deneme"
    nested()
    print(x)
    
func() #deneme
print(x)  #deneme












def greet(name):
    """takes a name argument as input"""
    print(f"Hello, {name}!")
    
    
greet("Toygar")    

return_value = greet("Toygar")    

print(return_value)    

help(greet)






def cube(x):
    return x ** 3

cube(3)



#celsius to fahr

def convert_cel_to_fahr(c):
    fahr = (c *(9/5)) + 32
    return fahr

derece = float(input("Derece giriniz: "))

fderece = convert_cel_to_fahr(derece)
print(f"{derece} degrees Celsius: {fderece:.2f} degrees fahrenheit")


#fahr to cel

def convert_fahr_to_cel(f):
    cel = (f - 32 ) * (5/9)
    return cel


derece = float(input("Derece giriniz: "))
cderece = convert_fahr_to_cel(derece)
print(f"{derece} degrees Fahrenheit: {cderece:.2f} degrees Celsius")




#senelik compound faiz yatırım hesabı

amount = float(input("Amount invested: "))
rate = float(input("rate given: "))
years = int(input("years invested: "))



def invest( amount, rate, years):
    new_amount = amount
    for _ in range(years):
        
        moneymade = (new_amount * rate)
        new_amount += moneymade
        print(new_amount)
        
    return new_amount 
    
invest(amount,rate, years)    




#findout the root of all evil

def rootevil(n):
    import math
    e = math.sqrt(n)
    return e
    

print(rootevil(666))




#effective python ch3 functions

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum
lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_stats(lengths) # Two return values
print(f'Min: {minimum}, Max: {maximum}')





def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')






def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    return minimum, maximum, average, median, count



minimum, maximum, average, median, count = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {average}, Median: {median}, Count {count}')






"""
Key Concept: Late Binding
In Python, closures capture variables by reference, not by value. This means that the variable number 
inside myfunction is not evaluated when the function is defined but rather when the function is called. 
By the time any of the functions in the functions list are called, the loop has completed, 
and the variable number will have its final value from the loop, which is 7.

"""



functions = []

for number in range(8):
    def myfunction():
        return number
    functions.append(myfunction)
    
print(functions)
    
results = [function() for function in functions]
print(results)


# Fixing the Code to Capture the Current Value of number
functions = []

for number in range(8):
    def myfunction(number=number):
        return number
    functions.append(myfunction)
    
results = [function() for function in functions]
print(results)

    
    
    