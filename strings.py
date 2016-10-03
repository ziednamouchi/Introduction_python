#chapter1
#string
#first try
bottles=99
base=''
base+='current inventory: '
base+=str(bottles)
print(base)
#Convert Data Types by Using str()
a=str(98.6)
b=str(1.0e4)
c=str(True)
print(a,b,c)
#Escape with \
palindrome='A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)
print('\tabc')
print('a\tbc')
testimony="\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(testimony)
speech='Today we honor our friend, the backslash: \\.'
print(speech)
#Combine with +
print('release the kraken! '+'At one!')
print("My word!","A gentleman caller!")
a='Duck.'
b='Grey Duck!'
print(a+b)
print(a,b)
#Duplicate with *
start='Na' *4 +'\n'
middle='Hey'*3+'\n'
end='Goodbye.'
print(start+start+middle+end)
#Extract a Character with []
letters='abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[5])
print(letters[-1])
#replacing H with P
name='Henny'
name1=name.replace('H','P')
name2='P'+name[1:]
print(name1,name2)
#Slice with [ start : end : step ]
letters='abcdefghijklmnopqrstuvwxyz'
first=letters[:]#from start to the end
second=letters[10:]
third=letters[12:15]#goes from 12 to 14, doesn't include 15
fourth=letters[::7]#from start to the end, by 7
fifth=letters[:21:5]#From the start to offset 20 by 5
sixth=letters[::-1]#from the end to the start
print(first,'\n',second,'\n',third,'\n',fourth,'\n',fifth,'\n',sixth)
#Get Length whith len()
a=len(letters)
empty=""
b=len(empty)
print(a,b)
#split with split()
todos='get gloves,get mask,give cat vitamines,call ambulance'
res1=todos.split(',')
res2=todos.split()
print(res1,'\n',res2)
#combine whith join(), the opposite of split()
crypto_list=['Yeti', ' Bigfoot', ' Loch ness monster']
crypto_string=','.join(crypto_list)
print('Found and signing book deals:', crypto_string)
