#get help from your parent with super
class Person():
 def __init__(self,name):
  self.name = name
class EmailPerson(Person):
 def __init__(self,name,email):
  super().__init__(name)
  self.email = email
bob = EmailPerson('Bob Frapples', 'bob@rapples.com')
print(bob.name)
print(bob.email)
#in self defense
class Car():
 def exclaim(self):
  print("I'm a Car!")
car = Car()
car.exclaim()
Car.exclaim(car)
#get and set attribute value with properties
class Duck():
 def __init__(self,input_name):
  self.hidden_name = input_name
 def get_name(self):
  print('inside the getter')
  return self.hidden_name
 def set_name(self,input_name):
  print('inside the setter')
  self.hidden_name = input_name
 name = property(get_name,set_name)
fowl = Duck('howard')
print(fowl.name)
#can still call get_name()
print(fowl.get_name())
#calling set_name()
fowl.name = 'Daffy'
print(fowl.name)
#define properties with decorator
class Duck():
 def __init__(self,input_name):
  self.hidden_name = input_name
 @property
 def name(self):
  print('inside second getter')
  return self.hidden_name
 @name.setter
 def name(self,input_name):
  print('inside second setter')
  self.hidden_name = input_name
fowl = Duck('howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
class Circle():
 def __init__(self,radius):
  self.radius = radius
 @property
 def diameter(self):
  return self.radius * 2
c = Circle(2)
print(c.radius)
print(c.diameter)
c.radius = 9
print(c.diameter)
