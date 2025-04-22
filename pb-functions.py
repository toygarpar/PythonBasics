

def f1():
    print("called f1")
    
def f2(f):
    f()


f2(f1)    



def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
     
    return wrapper

@f1
def f(a, b=9):
    print(a, b)    

@f1 
def add(x, y):
    return x + y    
    
f1(f)
f1(f)()    #this let us decorate a function


f = f1(f) #this line can be replaced bu decorator

f("hi")

print(add(4,5))








def sum_naturals(n):
    total, k = 0 , 1
    
    while k <= n:
        total ,k = total + k , k + 1
    
    return total


sum_naturals(100)
print(sum_naturals(100))


def sum_cubes(n):
    total, k = 0, 1 
    while k <= n:
        total, k = total + k**3, k + 1
        
    return total

sum_cubes(3)
    
    
    
    
    
    
    
def pi_sum(n):
    
    total, k = 0, 1 
    while k <= n:
        total , k = total + 8/((4*k-3)*(4*k-1)), k+1
        
    return total


pi_sum(100)
    
    
    
       



def summation(n, term):

    total, k = 0, 1 
    while k <= n:
        total, k = total + term(k), k + 1
        
    return total    
    
    
def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n, cube)
 
sum_cubes(3)  
    
    
    
    
def apply_each(func, iterable):
    return ( func(x) for x in iterable)    # as a generator

def sq(x):
    return x*x
    
    
nums = [1, 2, 3, 4, 5]    

sq_nums =  apply_each(sq, nums) #sq nums is the generator
print(next(sq_nums))
    







def apply_each(func, iterable):
    return [ func(x) for x in iterable]    # as a list

def sq(x):
    return x*x
    
def cubbe(x):
    return x*x*x
    
nums = [1, 2, 3, 4, 5]    

funked_nums =  apply_each(cubbe, nums)
print(funked_nums)  





def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))

print(squared_numbers) # [1, 4, 9, 16, 25]
    
    
    
    
def func_builder(x):
    return lambda num : num + x


add10 = func_builder(10)    

print(add10(7))
    




s= "audacity"

print(s[1:].capitalize())


    
    
    
    
    
#prompt user for input of anno domini    cs50 week 3 problem set 4

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]    
    

while True:
    date = input("Enter a date in the form of Month DD,YYYY or dd/mm/yy: ")
    
    try: 
        month = date[0: (date.find(" "))]
        if month.isalpha():
            
            month  = months.index(month) + 1
            day, year = date[date.find(" ")+1 : ].split(",")    
            print(f"{int(year)}-{int(month):02}-{int(day):02}")    
            
        elif date[0:2].isdigit():
            
            day,month,year = date.split("/")
            1 <= int(day) <= 31 
            int(month) <= 12
             
            print(f"{int(year)}-{int(month):02}-{int(day):02}")    
        
                
            
    except Exception as ex:
        print(ex)
        pass
        
        
            
        

print(f"{int(year)}-{int(month):02}-{int(day):02}")        
    
    
    
    
    
    
    
    
    
date = input("Enter a date in the form of MM D,YYYY or dd/mm/yy: ")


date= "January 17,1974"
date = "19/3/1974"
month = date[0: (date.find(" "))]
if month.isalpha():
    
    month  = months.index(month) + 1
    day, year = date[date.find(" ")+1 : ].split(",")    
    print(month, day , year) 
elif date[0:2].isdigit():
    
    day,month,year = date.split("/")
        
     
    print(month, day , year) 
else:
     print("you failed")   
    
   
    
   

#join text fonksiyonu
def join_text(*strings, sep: str) -> str:
    return sep.join(strings)
    
# def join_text(text1: str, text2: str, text3: str, * , sep: str) -> str:
    # return sep.join([text1, text2, text3])

def main() -> None:
    print(join_text("A", "B", "C", sep="-"))
    
if __name__ == "__main__":
    main()
    
    
    
    
    