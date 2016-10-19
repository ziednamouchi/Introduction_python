#task of chapter 4
#4.1
guess_me = 7
value = input('Give a string[q to quit] ')
while value != 'q':
    if len(value) < guess_me:
        print('Too low')
        break
    elif len(value) > guess_me:
        print('Too high')
        break
    else:
        print('just right')
        break
#4.2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('Too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oups')
        break
    start += 1
#4.3
val_list = [3,2,1,0]
for val in val_list:
    print(val)
#4.4
comp_lists = [comp_list for comp_list in range(0,10,2)]
print(comp_lists)
#4.5
comp_dicts = {comp_dict: comp_dict*comp_dict for comp_dict in range(10)}
print(comp_dicts)
#4.6
set_odd={number for number in range(1,10,2)}
print(set_odd)
#4.7
gen_comp = (number for number in range(10))
for gen_com in gen_comp:
    print('got ',gen_com)
#4.8
fun_list= ['Harry', 'Ron', 'Hermione']
def good():
    print(fun_list) 
good()
#4.9
def get_odds(first=1,last=10,step=2):
    number=first
    while number<last:
        yield number
        number+=step
get_odd=get_odds()
for number in get_odd:
    print(number)
#4.10
def test(func):
    if func:
        print('start')
    else:
        print('end')
@test
def add_int(a,b):
    return a + b
#4.11
class OopsException(Exception):
    pass
words = ['AB', 'hello', 'hallo', 'tschuss']
for word in words:
    if word.isupper():
        try:
            raise OopsException(word)
        except OopsException as other:
            print(other)
#4.12
titles =['Creature of Habit', 'Crewel Fate']
plots =['A nun turns into a monster', 'A haunted yarn shop']
print(dict(zip(titles,plots)))
