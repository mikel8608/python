"""
  Class: Cammel case: class NameOfClass():
  
  Method: These are Functions inside the Class. Operations you perform against the object
  
  Attributes: These are variables inside the class that get assigned values.
    They are referenced with self.<attr>
    e.g. self.breed = param2   
    ...breed is the attribute, mybread is a parameter containing a value
    ...by convention. param2 would have the same name as the attribute. 
    ...So you would have self.breed = breed, where 'breed' is a parameter in a function inside the class

    To access the attribute outside of the class, 
    ...1st assign the class to an object name, mydog=<class>(params), then use: mydog.<attr>

    You can specify attributes, outside of functions so they don't have to be parameters.

  __init_ is called when the class is called & allows you to create an instance of the object/class.
    def __init__(self,param1, param2)
    you require __init__ so parse in parameters to the object. e.g: val = classname(<parameter in __init_ function>)

  self parameter is a hidden variable parsed as the 1st arg in other languages. 
    In python you must put something as the first param that will be used to identify the class inside it's code.
    The convention is ot use 'self', but you can put anything here
    So generally parameters are assigned to attributes inside a class, so you can then access the values in code.
    You don't need to put self. infront of your attributes in the class, because it is set by default
"""

class Sample:
    pass


myClass = Sample()
print(type(myClass))


class Dog():
    # Since age is defined outside of a function, ie not created with self.<attr>,
    # it is a 'class object attribute' that will be the same for ALL instances of the class.
    age = 10

    # This is called to instanciate the class and imput attributes
    def __init__(self, breed):
        # because this attribute is defined inside the function,
        # it is an instance class object that changes per instance of the object
        self.breed = breed

    # This is a method, because it references self.
    def bark(self,name):
      # Note here that 'age' is a class attribute, and name is just a variable, since it doesn't reference 'self.'
      print("WOOF!, I am {} years old. My name is {}".format(self.age,name))

breedOfDog = Dog(breed="Shephard")
print(type(breedOfDog))
print("Breed is {} and age = {}".format(breedOfDog.breed, breedOfDog.age))
breedOfDog.bark("harry")



class Circle:
    pi = 3.142

    def __init__(self, radius=1):
        self.radius = radius
        # Attributes don't have to be parameters.
        self.area = self.pi * self.radius * self.radius
        # 'pi' can also be access as follows since it is a 'Class Object Attribute'
        # Note also that 'radius' is using the function input rather than the assigned Attribute: self.radius
        self.area2 = Circle.pi * radius * radius

    def get_circumference(self):
        # TypeError: circumference() takes 0 positional arguments but 1 was given
        # - this is because I had not used 'self' in the function definition above.
        return self.pi * self.radius * 2


def run_circle_class():
  msg="Running Circle Class"
  line="-"
  underline=line * len(msg)
  print(f"\n{msg}")
  print(underline)
  my_circle = Circle(2)
  # <bound method Circle.circumference of <__main__.Circle object at 0x0000021E36BE7880>>a
  # - this is because I called the method without ()
  print("circumference is", my_circle.get_circumference())
  print("pi value is", my_circle.pi)
  print("area is", my_circle.area, ". area2 is",my_circle.area2)

run_circle_class()

#
# Inheritance
#
class Animal:
  
  def __init__(self):
    print("Animal Class Created")

  def what_am_i(self):
    print("I'm an Animal")

  def eat(self):
    print("I'm eating")  

# Inherit Animal into other Class
class Dog(Animal):
  def __init__(self):
    Animal.__init__(self)
    print("Dog Class") 

def run_animal_dog_class():
  line='-'
  msg="Running Dog Class Inheriting from Animal Class"
  underline = line * len(msg)
  print("\nRunning Dog Class Inheriting from Animal Class")
  print(underline)
  my_animal = Dog()
  my_animal
  my_animal.what_am_i()
 
run_animal_dog_class()