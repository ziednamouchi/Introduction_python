#Comprehensions
#A comprehension is a compact way of creating a python data structure
#from one or more iterators.
#List comprehension
number_list = []
number_list.append(1)
number_list. append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)
#same idea with iterator
number_list = []
for number in range(1,6):
    number_list.append(number)
print("Using an iterator:\n",number_list)
#another method
number_list = list(range(1, 6))
print("Using another method:\n",number_list)
#Using list comprehension
number_list = [number for number in range(1,6)]
print("Using list comprehension:\n",number_list)
number_list = [number-1 for number in range(1,6)]
print("from 0 to 4 :\n",number_list)
#A list comprehension can include a conditional expression
a_list = [number for number in range(1,6) if number %2 == 1]
print("odd numbers:\n",a_list)
#traditional way
a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
print("traditional way:\n",a_list)
#making it a list of (row, col) tuples:traditional way
rows = range(1,4)
cols = range(1,3)
for row in rows:
  for col in cols:
    print(row,col)
#Comprehension way
rows= range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
  print(cell)
#using tuple unpacking
rows= range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for row,col in cells:
  print(row,col)
