#lists part II
#lists of lists
small_birds=['humming birds', 'finch']
extinct_birds=['dodo', 'passenger pigeon', 'norwegian blue']
carol_birds=[3, 'french hens', 2, 'turtledoves']
#elements of the list can be lists also
all_birds=[small_birds, extinct_birds, 'macaw', carol_birds]#list of lists
print(all_birds)
#first item of all_birds(list) is small_birds(list)
print('the first item is: ',all_birds[0])
#second item of all_birds(list) is extinct_birds(list)
print('the second item is: ',all_birds[1])
#first item of the first item( first item on small_birds )
print('the first item of the first item is: ',all_birds[0][0])
#first item of the second item( first item on extinct_birds )
print('the first item of the second item is: ',all_birds[1][0])
#change an item by [offset]
marxes=['Groucho', 'Chico', 'Harpo']
print('the original list is: ',marxes)
marxes[2]='Wanda'
print('the new list is: ',marxes)
#get a slice to extract items by offset range
marxes=['Groucho', 'Chico', 'Harpo']
print(marxes)
print('the new list: ',marxes[0:2])
print('slice with step',marxes[::2])#starts at the beginning and goes right by 2
print('reverse slice by 2: ',marxes[::-2])#starts at teh end and goes left by 2
print ('reverse list: ',marxes[::-1])#the trick to reverse a list
#Add an Item to the End with append()
marxes=['Groucho', 'Chico', 'Harpo']
print(marxes)
marxes.append('Zeppo')
print('the list after adding an item: ',marxes)
#Combine Lists by Using extend() or +=
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others=['gummo', 'karl']
marxes.extend(others)
print('extended list: ',marxes)
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others=['gummo', 'karl']
marxes+=others
print('extended list with +=: ',marxes)
#using append() to add a list inside a list
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print('updated list: ',marxes)#the last item of marxes is others (which is a list)
