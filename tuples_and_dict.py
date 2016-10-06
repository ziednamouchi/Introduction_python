#tuples
empty_tuple=()
print (empty_tuple)
marx_tuple='Groucho', 'Chico', 'Harpo'#the comma is mendatory after all the elements but the last
#no need to put parentheses
print(marx_tuple)
a, b, c=marx_tuple#tuples let you assign variables at once
print(a)
print(b)
print(c)
#using tuple to exchange varianbles
password='swordfish'
icecream='tuttifrutti'
password, icecream=icecream, password
print('the new password is : ',password)
print('the new icecream name is : ',icecream)
#tuple conversion
marx_list=['Groucho', 'Chico', 'Harpo']
marx_list1=tuple(marx_list)
print(marx_list1)
#Dictionaries
#create with {}
empty_dict={}
print(empty_dict)
bierce={
"day": "A period of twenty-four hours, mostly misspent",
"positive": "Mistaken at the top of one's voice",
"misfortune": "The kind of fortune that never misses",
}
print(bierce)
#convert by using dict()
#the order of keys in a dictionary is arbitrary
lol=[['a','b'], ['c','d'],['e','f']]#list of two-item lists
print(dict(lol))
lot=[('a','b'),('c','d'),('e','f')]#list of two-item tuples
print(dict(lot))
tol=(['a','b'], ['c','d'], ['e','f'])#tuple of two-item lists
print(dict(tol))
los=['ab', 'cd', 'ef']#list of two-character strings
print(dict(los))
tos=('ab', 'cd', 'ef')#tuple of two-character strings
print(dict(tos))
pythons = {
'Chapman': 'Graham',
'Cleese': 'John',
'Idle': 'Eric',
'Jones': 'Terry',
'Palin': 'Michael',
}
pythons['Gilliam']='Gerry'
print(pythons)
#combine dictionaries with update()
others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
pythons.update(others)
print(pythons)
first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)
#delete an item by key with del
del pythons['Marx']
print(pythons)
#Delete All Items by Using clear()
pythons.clear()
print(pythons)
