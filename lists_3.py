#lists part III
#add an item by offset with insert()
marxes=['groucho', 'chico', 'harpo', 'zeppo']
marxes.insert(3, 'gummo')
print('updated list:',marxes)#add gummo at the third position
marxes.insert(10,'karl')
print('recently updated list',marxes)#an offset that is beyond the end of the list inserts at the end
#delete an item by offset with del
del marxes[-1]
print('newly updated list: ',marxes)
print(marxes[2])
del marxes[2]
print('newly updated list: ',marxes)
print(marxes[2])
#Delete an Item by Value with remove()
marxes=['groucho', 'chico', 'harpo', 'gummo', 'zeppo']
marxes.remove('gummo')
print(marxes)
#Get an Item by Offset and Delete It by Using pop()
marxes=['groucho', 'chico', 'harpo', 'zeppo']
print(marxes)
extracted=marxes.pop()#equivalent to pop(-1) it gives the tail of the list
print('the extracted item is: ',extracted)
print('new list is: ',marxes)
extracted1=marxes.pop(1)
print('the extracted item is: ',extracted1)
print('new list is: ',marxes)
#Find an Item’s Offset by Value with index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)
in_dex=marxes.index('Chico')
print(in_dex)
#Test for a Value with in
test='Groucho' in marxes
print(test)
test1='Bob' in marxes
print(test1)
#count occurences by using count()
marxes = ['Groucho', 'Chico', 'Harpo']
nb_occ=marxes.count('Harpo')
print(nb_occ)
nb_occ1=marxes.count('Bob')
print(nb_occ1)
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
nb_occ3=snl_skit.count('cheeseburger')
print(nb_occ3)
