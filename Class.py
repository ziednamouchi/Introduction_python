#chapter 6
#class creation
class Person():
 def __init__(self,name):
  self.name = name
#object creation
hunter = Person('Elmur Fudd')
print('the mighty hunter: ', hunter.name)
#inheritance
class Car():
 def exclaim(self):
  print("I'am a car!")
class Yugo(Car):
 pass
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
#override a method
class Car():
 def exclaim(self):
  print("I'am a car!")
class Yugo(Car):
 def exclaim(self):
  print("I'm a hugo")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
class Person():
 def __init__(self,name):
  self.name = name
class MDPerson(Person):
 def __init__(self,name):
  self.name = "Doctor " + name
class JDPerson():
 def __init__(self,name):
  self.name = name+", Esquire"
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)
#add a method
class Car():
 def exclaim(self):
  print("I'm a print!")
class Yugo(Car):
 def exclaim(self):
  print("I'm a Yugo")
 def need_a_push(self):
  print("a little help here?")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()
#give_me_a_car.need_a_push() will give an error since the fonction is not define inside the class Car()
