#dog class


class Dog:
    species = "loveable species"
    
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.coat_color = color
        self.breed = breed
        
    
    # Replace .description() with __str__()    
    def __str__(self):
        return f"{self.name} is {self.age} years old and belongs to {self.species} family"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class Chihuahua(Dog):
    pass

class Terrier(Dog):
    pass

class Jrt(Dog):
    pass
    
        


taco = Dog("Taco", 17, "brown", "chihuahua")       
buzz = Dog("Buzz", 23, "brown","chihuahua")
citir = Dog("Çıtır", 16, "white", "terrier")
bocush = Dog("Böçüş", 10, "black-white", "jack russell terrier çakması")


taco.name

taco.breed

print(taco)

taco.speak("hevhev")



#doggy class


class Doggy:
    species = "loveable species"
    
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.coat_color = color
        
        
    
    # Replace .description() with __str__()    
    def __str__(self):
        return f"{self.name} is {self.age} years old and belongs to {self.species} family"
    
    def __repr__(self):
        #return f"Doggy({self.name!r}, {self.age!r}, {self.coat_color!r})"
        return (f"{self.__class__.__name__}({self.name!r}, {self.age!r}, {self.coat_color!r})")
    
    def speak(self, sound):
        return f"{self.name} barks {sound}"
    
class Chihuahua(Doggy):
    def speak(self, sound="hev"):
        return f"{self.name} says {sound}"

class Terrier(Doggy):
    def speak(self, sound="grrrrr"):
        return f"{self.name} says {sound}"

class Jrt(Doggy):
    def speak(self, sound="harfv"):
        return super().speak(sound)




taco = Chihuahua("Taco", 17 , "light brown")
bocush = Jrt("Böçüsh", 10, "black-white")
citir = Terrier("Çıtır", 16, "white")
buzz = Chihuahua("BUzz", 23,"brown")

taco.species
buzz.name

type(taco)
type(bocush)
type(citir)


isinstance(taco, Doggy)

isinstance(taco, Jrt)
taco.speak()
bocush.speak()


repr(taco)
str(taco)














#custom error class




class NameTooShortError(ValueError):
    pass
def validate(name):
    if len(name) < 10:
            raise NameTooShortError(name)






#easily create class with 2 lines of code

class Computer:
    pass

class PC(Computer):
    pass

"""
defines a class named Computer containing no attribute and no
method, though it automatically inherits all the attributes and methods of the
generic object class in the built- in module of Python
"""


help(Computer)

help(PC)

#use the setattr function to add an attribute called CPU to an instance of the Computer class

c = Computer()

setattr(c, "CPU", "Intel I7")  #use dunder setattr(o,a,v)

c.CPU  #outputs 'Intel I7'

"""
 In our simplest definition of class Computer, we did not
define the __init__ method, but it has been automatically inherited from class
builtins.object.
"""

#use special attribute __dict__ of instance c of class Computer to check the attribute and value of object c
print(c.__dict__)


#pyappwith OOP - class definition with overriding

class Form:
    """ design  abstract class for shape"""
    
    def perimeter(self):   #method to be overridden
        pass
    
    def zone(self):  #method to be overridden
        pass
    
    
class Daire(Form):
    def __init__(self, radius):
        self.radius = radius
        
    def perimeter(self):   #◙ this overrides the method defined in Form
        return self.radius * 2 * 3.14   
    
    def zone(self):    #◙ this overrides the method defined in Form
        return self.radius ** 2 * 3.14
    
    
class Rect(Form):    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def perimeter(self):
        return (self.width +self.length) * 2
    
    def zone(self):
        return self.width * self.length
    
    def is_Sq(self):
        return self.width == self.length
        
        
        


d1 = Daire(25)

print(f"A circle with a radius of {d1.radius} has an area of {d1.zone()},")
print(f"and the perimeter of the cicle is {d1.perimeter()}")



repr(d1.perimeter)
str(d1.perimeter)

"""
Instead, attributes are introduced within the definition of the __init__
method by assignment statements or by using the built- in function setattr(o,
a, v), which are all the attributes of the particular instance created by the
constructor of the class. 
"""



rect1 = Rect(25, 50)


print(f"Are of the rectangle  has an area of {rect1.zone()},")
print(f"and the circumference of the rectangle is {rect1.perimeter()}")
print(f"Is the rectangle a square?: {rect1.is_Sq()}")





#inheritance : subclass and superclass

#class myClass(base_1, base_2, base_3):  #↨add all the base classes to the list of inheritances enclosed in a pair of parentheses
    #pass



class myClassA:
    pass

dir(myClassA)



class myClassB(object):
    pass

dir(myClassB)

#In particular,  need to override the dunder methods __init__ __str__, and __repr__

"""
The method __init__ is a dunder method used as constructor called internally by PVM whenever a new instance of a class needs
to be created. 

The method __str__ is a dunder method called internally whenever an object of a class needs to be converted to a string, such as for printout.

 __repr__ is a dunder method called internally when an object needs to be converted to a representation for 
 serialization— a process that converts a Python object into a byte stream that can be stored or transmitted.
 
"""
 



















































