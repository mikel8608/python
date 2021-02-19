'''
  Polymorphism is when different Classes share the same method name.
  For Example: Below we call 'speak()' from two different classes.
'''

class Dog():
  def __init__(self,name):
    self.name = name
  
  def speak(self):
    return self.name + " says Woof!"


class Cat():
  def __init__(self,name) -> None:
    self.name = name
  def speak(self):
    return self.name + " says Meow"

fido = Dog("Fido")
felix = Cat("Felix")

print(fido.speak())
print(felix.speak())