#OOP

#class

list1 = [ 1 , 2 , 3]
list2 = [1, 2, 3, 4]

result = type(list)

print(result)


#class => Person(name, surname, birthday, calculateAge())    örmek person class'ı
#instance(object)



#class

class Person:
    
    
    #class attributes
    address = "no info"
    
    
    
    #constructor (yapıcı metot)
    def __init__(self, name, year):
        #object attributes - 
        self.name = name
        self.year =  year
        
        print("init metodu çalıştı.")
        
        
        
        
        
        
    #methods
    def intro(self):
        print("Hello There " + self.name)


    def calculateAge(self):
        return 2023 - self.year



#object, instance

p1 = Person("ali", 1990)
p2 = Person("yağmur", 1995)
p3 = Person(name= "veli", year  = 1997)

p1.intro()
p2.intro()

print(f"Adım: {p1.name}, Yaşım : {p1.calculateAge()}.")
print(f"Adım: {p2.name}, Yaşım : {p2.calculateAge()}.")

#updating
p1.name = "ahmet"
p1.address = "karabük"

#accessing object attributes
print(f"p1: name:{p1.name}, year: {p1.year}, address: {p1.address}")
print(f"p2: name:{p2.name}, year: {p2.year}, address: {p2.address}")
print(f"p3: name:{p3.name}, year: {p3.year}, address: {p3.address}")

print(p1)
print(p2)


print(type(p1))
print(type(p2))

print(p1 == p2)  #farklı objeler : False verir







class Circle:
    #class obj attribute
    pi = 3.14
    
    
    def __init__(self, yaricap=1):
        self.yaricap = yaricap 
        
        
    #methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap
    
    
    def alanHesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle()  #yarıcap=1
c2  = Circle(5)

print(f"c1 : alan = {c1.alanHesapla()}, çevre = {c1.cevreHesapla()}")
print(f"c2 : alan = {c2.alanHesapla()}, çevre = {c2.cevreHesapla()}")




#Inheritance - Kalıtım : miras alma

#Person ,=> name, lastname, age, eat(), run(), drink()

#Student, Teacher  üstteki özelliklerin hepsini isterim
#Student(Person), Teacher(Person)

#ANimal => Dog(ANimal), Cat(ANimal)


class Person():
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Person Created")
        
    def whoami(self):
        print("I am a doggie")

    def eat(self):
        print("Yummy Yummy")
            
            
            
            
class Student(Person):        
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentno = number
        print("Student Created")
        
    
    #override
    def whoami(self):
        print("I am a student")
    
    def sayHello(self):
        print("Hello I am a student")


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
        
    def whoami(self):
        print(f" I am a {self.branch} teacher.")



p1 = Person("taco", "par")
s1 = Student("böcüsh", "par", 1256)
t1 = Teacher("Çıtır", "Par", "dogmaster")

print(p1.firstname + " " + p1.lastname)
print(s1.firstname + " " + s1.lastname + " " + str(s1.studentno))

p1.whoami()
s1.whoami()
p1.eat()
s1.eat()
s1.sayHello()
t1.whoami()



#özel metotlar

mylist = [1, 2, 3]

print(len(mylist))
print(type(mylist))

mystring = "My String"
print(len(mystring))
print(type(mystring))


class Movie():
    def __init__(self, title, director, duration):
        self.title =  title
        self.director =  director
        self.duration = duration
        print("Movie objesi oluşturuldu")


    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("movie silindi")


m = Movie("titanik", "james cmaeron", 220)





print(mylist)
print(m)
print(str(m))
print(len(m))


del m















#quiz uygulaması

#question

class Question:
    def __init__(self, text, choices, answer):
        self. text = text
        self.choices =  choices
        self.answer =  answer
        
    def checkAnswer(self, answer):
        return self.answer == answer 
        
     
        



#quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")
        
        
        for q in question.choices:
            print("-" + q)
        
        answer = input("Cevap: ")
        print(question.checkAnswer(answer))
        
        self.quess(answer)
        self.loadQuestion()
        
    def quess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def showScore(self):
        print("score: ", self.score)
        
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print("Quiz Bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100, "*"))
        
q1 = Question("en iyi programlama dili hangisi?", ["C#", "python", "javascript", "java"], "python")
q2 = Question("en popüler programlama dili hangisi?", ["python", "javascript", "java", "C#"], "python")
q3 = Question("en çok kazandıran programlama dili hangisi?", ["C#", "javascript", "java", "python"], "python")
q4 = Question("en sevilen programlama dili hangisi?", ["C#", "javascript", "java", "python"], "python")
q5 = Question("en kolay programlama dili hangisi?", ["C#", "javascript", "java", "python"], "python")


questions = [q1, q2, q3, q4, q5]

# print(q1.checkAnswer("python"))
# print(q2.checkAnswer("C#"))

quiz = Quiz(questions)
# question = quiz.getQuestion()
# print(question.text)
# print(question.choices)


quiz.loadQuestion()





















































