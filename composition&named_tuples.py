#composition
class Bill():
 def __init__(self, description):
  self.description = description
class Tail():
 def __init__(self, length):
  self.length = length
class Duck():
 def __init__(self, bill, tail):
  self.bill = bill
  self.tail = tail
 def about(self):
  print('This duck has a', bill.description, 'bill and a', tail.length, 'tail')
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
#Named Tuples
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange','long')
print(duck)
print(duck.bill)
print(duck.tail)
#named tuple from dictionary
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2= Duck(**parts)
print(duck2)
#Named tuples are immutable, but you can replace one or more fields and return another named tuple
duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)
