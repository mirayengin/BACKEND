import os
os.system('cls' if os.name == 'nt' else 'clear')
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("--------------------------------------")

#! Topics to be Covered:
#* Everything in Python is class
#* Defining class
#* Defining class attributes
#* Difference between class attributes and instance attributes
#* SELF keyword
#* Defining methods
#* Class Methods vs. Static Methods and Instance Methods
#* Special methods (init, str)
#* 4 pillars of OOP:
    #? Encapsulation
    #? Abstraction
    #? Inheritance
        #? Multiple inheritance
    #? Polymorphism
        #? Overriding methods
#* Inner class
#* Overloading an operator (optional)
#* Abstract base class 


#! What is OOP?
""" # Object Oriented programming (OOP) is a programming paradigm that relies on the concept of classes and objects.
# It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects.
# significantly reduces code repetition by classifying similar structures (dont repeat yourself)
# Easier to debug, classes often contain all applicable information to them
# Secure, protects information through encapsulation """


#! Everything in Python is class
""" # Python >generally class based  vs.  javascript >generally function based
def print_types(data):
    for i in data:
        print(i, type(i))
        
test = [122, "victor", [1, 2, 3], (1,2,3), {1,2,3}, True, lambda x:x]

print_types(test) """

#! defining class:
# Class oluştururken isimlendirmede PascalCase yapı kullanılır. (Her kelimenin ilk harfi büyük ve bitişik.)

# class keyword for defining

# class Person :
#   name="Erhan" #? class attributes/property
#   age=31

# person1 = Person() #? create object/instance
# person2 = Person()

# print(person1.name) #? instance inherites class attrıbutes
# print(person2.age)

# print(person1.job)  # ?burda eklenen görülmez python yukarıdan aşağıya doğru run olur


# Person.job = "developer"  #? burda object e attrıbute ekledik

# print(person1.job)  #? görüldüğü gibi instance  ve object(class) arasında bağ var ve eklemeler instance ları etkiler

#?HOCANIN

#! "class" keyword for defining 
#! There is a convention among languages that the class name should be capitalized.

# class Person:
#     name = "victor"  #? class attrinutes/properties
#     age = 33

# person1 = Person()  # ?creating object or instance
# person2 = Person()

# print(person1.name) #? instances inherites class atributes
# print(person2.age)

# Person.job = "developer" 
# print(person1.job)  #? there is connection between classes and insttances



# class Person :
#   compony = "clarusway"


# person1 = Person()
# print(person1.compony)

# person2 = Person()
# print(person2.compony)


# person1.compony = "tesla" #! Bu sadece bu instance i etkiler ve sadece compony bu person da değişir.
# print(person1.compony)

# person2.location = "Turkey"
# print(person2.location)
# print(person1.location) #! Burda olmaz


#! SELF keyword and methods

# class Person :
#   compony = "clarusway"

#   def test(self):
#     print("test")

#   def set_details(self, name, age):
#          self.name = name
#          self.age = age


#   def get_details(self):
#     print(f"{self.name} - {self.age}")


#! staticmethod: self'e ihtiyaç duymayacağımız metodlarda kullabiliriz. Self sonuçta büyük bir instanceı temsil edebilir, yani performans için kullanılabilir.
  # @staticmethod #? bunu yapınca instance göre değişmiyor hep aynı çalışıyor her zaman ve parametre almazlar
#   def salute():
#     print("Hı there!")



# person1 = Person()
# person2 = Person()


#! burada self keyword u person1 ve person2
# person1.test()
# person2.test()

# person1.name = "erhan"
# person1.age = 31

# person1.get_details() 

# person2.name = "asli"
# person2.age = 27

# person2.get_details() 

#! Yukarıdaki gibi self hangi instance ile çalışıyorsa o olur


# person2.set_details("erhan", 33)
# person2.get_details()


#? JS'deki "setter" ve "getter" methodları, pythonda da mevcuttur.
#! get_method_name(self)
#! set_method_name(self, parameters)



#! SPECİAL METHODS (DUNDER METHODS)
class Person:
  compony = "clarusway"
  person_count = 0

  #! Otomatik run olur biz instance ı oluşturduğumuzda
  def __init__(self,name,age, gender="male"):
      self.name = name
      self.age = age
      self.gender = gender
      Person.person_count = Person.person_count + 1
      


  def __str__(self):
    return f"{self.name} - {self.age}"

  def get_details(self):
    print(f"{self.name} - {self.age} - {self.gender}")


person1 =Person("victor", 37)
person2 =Person("henry", 37)

# print(Person.person_count)
# person1.get_details()


#! __str__
print(person1)
print(person2)



#! OOP PRİNCİPLES

#? Encapsulation
 # The princible in which we determine how much of the classes, data and methods can be viewed and how much can be changed by the user.

 # kullanıcı tarafından sınıfların, verilerin ve metodların ne kadarının görüntülenebileceğini, ne kadarının değiştirilebileceğini belirlendiğimiz yapı


    # public - private - protected (not in python or js)
    # there is not a complete encapsulation in python






#? Abstraction
  # Abstraction is the process of hiding the internal complex details of an application from the outer world. Abstraction is used to describe things in simple terms. It's used to create a boundary between the application and the client programs.  
    # like coffee machine in real life. you dont need to know how it works but you know its functionality
    
    # kullanıcı gereksiz detaylardan ve bilmesine ihtiyaç olmayan yapıdan uzaklaştırarak yormamak - soyutlama














