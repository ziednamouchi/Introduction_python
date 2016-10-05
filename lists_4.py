#lists part VI
#convert to string with join
marxes = ['Groucho', 'Chico', 'Harpo']
joined=','.join(marxes)
print(joined)
separator='*'
joined1=separator.join(marxes)
print(joined1)
#reconvert into list with split
separated=joined1.split(separator)
print(separated)
print(separated==marxes)#must retur true
#reorder items with sort()/sorted()
#sorted(): return a sorted copy of the list it doesn't change the original list
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
#sort(): sorts the list itself
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.sort()
print(marxes)
numbers = [2, 1, 4.0, 3]#mixed types
numbers.sort()
print(numbers)
numbers.sort(reverse=True)#descending order
print(numbers)
#Get Length by Using len()
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))
#Assign with =
a = [1, 2, 3]
print(a)
b=a
print(b)
a[0]='surprise'
print(a)
print(b)#because b just refers to the same object as a 
#any change in any of them cause a change in both
# Copy with copy()/list()/[:]
a = [1, 2, 3]
b=a.copy()
c=list(a)
d=a[:]
print(a,'\n',b,'\n',c)
a[0] = 'integer lists are boring'
print(a,'\n',b,'\n',c)#tonly a has changed
