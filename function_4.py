#function
#Anonymous Functions: the lambda() Function
def edit_story(words,func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
    return word.capitalize() + '!'
edit_story(stairs,enliven)
#lambda use
print("here is the lambda method:")
def edit_story(words,func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']
edit_story(stairs,lambda word:word.capitalize() + '!')
#generators
print(sum(range(1,101)))
def my_range(first=0, last=10, step=1):
    number=first
    while number < last:
        yield number
        number += step
ranger = my_range(1,5)
for x in ranger:
    print(x)
#decorators
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ',func.__name__)
        print('Positional arguments: ',args)
        print('Keyword arguments: ',kwargs)
        result = func(*args,**kwargs)
        print('Result: ',result)
        return result
    return new_function
def add_ints(a,b):
    return a + b
cooler_add_ints = document_it(add_ints)#manual decorator assignment
cooler_add_ints(3,5)
@document_it
def add_int(a,b):
    return a + b
add_int(5,8)
#multi decorators
def square_it(func):
    def new_function(*args,**kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function
@document_it
@square_it
def add_i(a,b):
    return a + b
add_i(3,5)
@square_it
@document_it
def add_i(a,b):
    return a + b
add_i(3,5)
