#function_2
#specifying default parameter values
def menu(wine,entree,dessert='pudding'):
    return{'wine':wine,'entree':entree,'dessert':dessert}
print(menu('chardonnary','chicken'))#the default is used 
print(menu('dunkelfelder', 'duck', 'doughnut'))#if you do provide an argument,it's used instead of the default
def buggy(arg, result=[]):#the list is empty only on the first run
    result.append(arg)
    print(result)
buggy('a')
buggy('b')
buggy('c')
def works(arg):#now result run each time with a fresh empty list
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))
print(works('c'))
#The fix is to pass in something else to indicate the first call
def nonbuggy(arg, result = None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')
#Gather Positional Arguments with * (tuple)
def print_args(*args):
    print('Positional argument tuple: ',args)
print_args()
print_args(3,2,1,'wait','go!')
def print_more(required1,required2,*args):
    print('Need this one: ',required1)
    print('Need this one too: ',required2)
    print('All the rest:',args)
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
#Gather Keyword Arguments with **
def print_kwargs(**kwargs):#inside the function kwargs is a dictionary
    print('Keyword arguments:',kwargs)
print_kwargs(wine='merlot',entree='mutton',dessert='macaroon')
#Docstrings
def echo(anything):
    'echo returns its input argument'
    return anything
#To print a function’s docstring
help(echo)
#see the raw docstring, without the formatting
print(echo.__doc__)
