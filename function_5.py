#Namespaces and Scope
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)
print('at the top level:', animal)
print_global()
def change_local():
    animal = 'wombat'
    print('inside change_local: ',animal, id(animal))
change_local()
print(animal)
def change_and_print_global():#say global or python will use the local variable
    global animal
    animal= 'wombat'
    print('inside change_and_print_global:  ', animal)
print(animal)
change_and_print_global()
print(animal)
#locals() and globals()
animal= 'batfruit'
def change_local():
    animal = 'batwom'#local variable
    print('locals: ',locals())
print(animal)
change_local()
print(globals())
print(animal)
#Uses of _ and __ in names
#Names that begin and end with two underscores ( __ ) are reserved for use within Python
def amazing():
    '''this is the amazing function.
    want to see it again?'''
    print ('this function is named: ', amazing.__name__)
    print('and its docstring is: ',amazing.__doc__)
amazing()
#Handle Errors with try and except
short_list = [1,2,3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and ',len(short_list)-1,'but got', position)
short_list = [1,2,3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('bad index: ',position)
    except Exception as other:
        print('something else broke: ',other)
#make your own exceptions
class UppercaseException(Exception):
    pass
words = ['eeenie','meenie','miny','MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
