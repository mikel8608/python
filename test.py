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