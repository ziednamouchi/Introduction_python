#special methods
class Word():
 def __init__(self, text):
  self.text = text
 def equals(self, word2):
  return self.text.lower() == word2.text.lower()
first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first.equals(second))
print(first.equals(third))
#ge the equals() method to the special name __eq__()
class Word():
 def __init__(self, text):
  self.text = text
 def __eq__(self, word2):
  return self.text.lower() == word2.text.lower()
first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == third)
print(first == second)
#Magic Methods For Comparison

# __eq__( self, other ) self == other
# __ne__( self, other ) self != other
# __lt__( self, other ) self < other
# __gt__( self, other ) self > other
# __le__( self, other ) self <= other
# __ge__( self, other ) self >= other

#Magic Methods For Math

# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other

#Other, miscellaneous magic methods

# __str__( self ) str( self )
# __repr__( self ) repr( self )
# __len__( self ) len( self )
