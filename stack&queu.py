#Stack + Queue == deque
#palindrome check with deque
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False
    return True
print(palindrome('a'))#true
print(palindrome('radar'))#true
#quick palindrome check
def another_palindrome(word):
    return word == word[::-1]
print (another_palindrome('radar'))#true
print (another_palindrome('hello'))#false
#Iterate over Code Structures with itertools
import itertools
for item in itertools.chain([1,2],['a','b']):
    print(item)
#cycling between 1 and 2
#import itertools
#for item in itertools.cycle([1,2]):
#    print(item)
import itertools
for item in itertools.accumulate([1,2,3,4]):
    print(item)
import itertools
def multiply(a, b):
    return a * b
print(multiply(3,4))
for item in itertools.accumulate([1,2,3,4],multiply):
    print(item)
#print nacely with pprint()
from pprint import pprint
from collections import OrderedDict
quotes = OrderedDict([('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])
print(quotes)
pprint(quotes)
