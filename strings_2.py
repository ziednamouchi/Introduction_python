#chapter1
#playing with strings
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
print(poem)
poem1=poem[:13]#first 13 characters(offsets 0 to 12)
print(poem1)
length=len(poem)#poem's length
print(length)
poem2=poem.startswith('All')#starting string
print(poem2)#boolean result
poem3=poem.endswith('that\'s all,folks!')#ending string
print(poem3)
#finding a specific string
word='the'
poem4=poem.find(word)
print(poem4)#returns position
poem5=poem.rfind(word)#offset of the last 'the'
print(poem5)
poem6=poem.count(word)#numb of occurence
print(poem6)
poem7=poem.isalnum()#checks if all characters are alphanum
print(poem7)#returns true or false
#Case and Alignment
#Case
setup='a duck goes into a bar...'
setup1=setup.strip('.')#removes the dot sequences
print(setup1)
setup2=setup.capitalize()#Capitalize the first word
print(setup2)
setup3=setup.title()#Capitalize all the words
print(setup3)
setup4=setup.upper()#Convert all characters to uppercase
print(setup4)
setup5=setup.lower()#Convert all characters to lowercase
print(setup5)
setup6=setup.swapcase()#Swap upper- and lowercase
print(setup6)
#alignment
setup7=setup.center(30)#Center the string within 30 spaces
print(setup7)
setup8=setup.ljust(30)#left justify
print(setup8)
setup9=setup.rjust(30)#right justify
print(setup9)
#Substitute with repace()
setup10=setup.replace('duck', 'marmoset')
print(setup10)
setup11=setup.replace('a ', 'a famous ', 100)
print(setup11)
