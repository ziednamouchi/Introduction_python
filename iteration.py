#iterate with for
rabbits = ['flopsy', 'mopsy','cottontail', 'peter']
current = 0
#with while
while current < len(rabbits):
    print("with while \n",rabbits[current])
    current += 1
#with for
for rabbit in rabbits:
    print("with for \n",rabbit)
#strinng iteration
word = 'cat'
for letter in word:
    print(letter)
accusation = {'room': 'ballroom', 'weapon': 'lead pipe' , 'person': 'col.mustard'}
for card in accusation: # or accusation.keys()
    print(card)
#to iterate over the values
for value in accusation.values():
    print(value)
cheeses = []
for cheese in cheeses:
    print("this shop has some lovely", cheese)
    break
else:
    print("this is not much of cheese shop, is it?")
#same effect without else
cheeses = []
found_one = False
for cheese in cheeses:
    found_one = True
    print("this shop has some lovely", cheese)
    break
if not found_one:
    print("this is not much of cheese shop, is it?")
#iterate multiple sequences with zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day,": drink", drink,"-eat", fruit, "- enjoy", dessert)
#make list/dictionary using tuple and zip()
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
t_uple = list( zip(english,french))
d_ict= dict( zip(english,french))
print(t_uple)
print(d_ict)
#generate numbber sequences with range()
for x in range(0,3):
    print("x = ",x)
print(list( range(0,3)))
for y in range(2,-1,-1):
    print("y = ",y)
print(list( range(2,-1,-1)))
