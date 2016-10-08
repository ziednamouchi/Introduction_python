#Combinations and operators
drinks = {
'martini': {'vodka', 'vermouth'},
'black russian': {'vodka', 'kahlua'},
'white russian': {'cream', 'kahlua', 'vodka'},
'manhattan': {'rye', 'vermouth', 'bitters'},
'screwdriver': {'orange juice', 'vodka'}
}
for name, contents in drinks.items():
 if contents & {'vermouth', 'orange juice'}:
  print(name)
for name, contents in drinks.items():
 if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
  print(name)
a = {1,2}
b = {2,3}
print (a&b)#same as a.intersection(b)
print(a|b)#same as a.union(b)
print(a-b)#same as a.difference(b)
print(b-a)#same as b.difference(a)
print(a^b)#same as a.symmetric_difference(b)
print(a<=b)#same as a.issubset(b)
print(a<b)
print(a>b)
print(a>=b)#same as a.issuperset(b)
#compare date structure
marx_list=['Gruchou','Chico','Harpo']
marx_tuple='Gruchou','Chico','Harpo'
marx_dict={'Gruchou':'banjou','chico':'piano','Harpo':'harp'}
print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])
#make bigger data structure
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
tuple_of_lists=marxes,pythons,stooges
print(tuple_of_lists)
list_of_lists=[marxes,pythons,stooges]
print(list_of_lists)
dict_of_list={'marxes':marxes,'pythons':pythons,'stooges':stooges}
print(dict_of_list)
