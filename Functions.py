#FUNCTIONS
# function without/with arguments
def make_a_sound():
    print('quack')
make_a_sound()
def agree():
    return True
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')
def echo(anything):
    return anything
print(echo('Hello friend!'))
def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "it's a green pepper."
    elif color == "bee purple":
        return "I dont know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color +"."
comment = commentary('blue')
print(comment)
def do_nothing():
    pass
print(do_nothing())
#none is usefull
thing = None
if thing:
    print("It's some thing")
else:
    print("It's nothing")
def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")
is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())
#Positional arguments
def menu(wine, entree, dessert):
    return {'wine':wine,'entree':entree,'dessert':dessert}
print(menu('beef','bagel','bordeaux'))
#keyword arguments
print(menu(entree='chicken',dessert='cake',wine='chardonnary'))
print(menu('frontenac', dessert='flan', entree='fish'))
