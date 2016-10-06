#dictionaries
#test for a key by using in
pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael'}
print ('Chapman' in pythons)
#get item by key
print(pythons['Cleese'])
print(pythons.get('Cleese'))
#get all keys by using keys()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())#dict_keys(['green', 'red', 'yellow'])
print(list(signals.keys()))#converts dict_keys to a list
#get all values by using values()
print(list(signals.values()))#values in a dictionary
#Get All Key-Value Pairs by Using items()
print(list(signals.items()))
#Assign with =, Copy with copy()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
signal = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signal = signal.copy()
signal['blue'] = 'confuse everyone'
print(original_signal)
#sets
empty_set=set()
print(empty_set)
even_numbers={0,2,4,6,8}
odd_numbers={1,3,5,7,9}
print(even_numbers,'\n',odd_numbers)
print(set('letters'))
drinks = {
'martini': {'vodka', 'vermouth'},
'black russian': {'vodka', 'kahlua'},
'white russian': {'cream', 'kahlua', 'vodka'},
'manhattan': {'rye', 'vermouth', 'bitters'},
'screwdriver': {'orange juice', 'vodka'}
}
print('---------------------drinks are: ')
for name,contents in drinks.items():
 if 'vodka' in contents:
  print(name)
print('-------------updates drinks are: ')
for name,contents in drinks.items():
 if 'vodka' in contents and not('vermouth' in contents or 'cream' in contents):
  print(name)
