#what is true
some_list = []
if some_list:
    print("there is something in here ")
else:
    print ("hey, it's empty!")
#repeat with while
count = 1
while count <= 5:
    print(count)
    count += 1
#cancelling with break
while True:
    stuff= input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
#skip Ahead with continue
while True:
    value = input("Integer, please [q to quit]")
    if value == 'q': #quit
        break
    number = int(value)
    if number % 2 == 0: # an even number
        continue
    print(number,"squared is ", number*number)
#check break use with else
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('found even number: ',number)
        break
    position += 1
else:
    print("no even number found")
