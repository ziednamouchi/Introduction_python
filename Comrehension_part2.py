#Dictionary comprehension
word = "letters"
letter_count = {letter: word.count(letter) for letter in word}
print(letter_count)
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
#Set Comprehensions
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)
#generator comprehension (there is no tuple comprehension) 
number_thing = (number for number in range(1,7))
print(type(number_thing))
#way of iterate over generator
for number in number_thing:
    print(number)
#list way
number_things = (number for number in range(1,7))
number_list= list(number_things)
print(number_list)
#a generator doesn't keep its value in memory
#it can be run only once
number_list= list(number_things)
print(number_list)
