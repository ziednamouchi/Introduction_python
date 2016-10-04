#how to make empty lists
#first: empty_list=[]
empty_list=[]
print(empty_list)
#second: empty_list_1=list()
empty_list_1=list()
print(empty_list_1)
#third: empty_list_2
#not empty list
weekdays=['Monday','tuesday','wednesday','thursdau','friday','saturday','sunday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']#values don't need to be unique
print(weekdays,'\n',big_birds,'\n',first_names)
#Convert Other Data Types to Lists with list()
conversion=list('cat')
print(conversion)
#coverting a tuple to a list
tup_le=('triangle','square','circle')
print(tup_le)
lis_t=list(tup_le)
print (lis_t)
#split
birthday = '1/6/1952'
birth_spl=birthday.split('/')
print(birth_spl)
splitme = 'a/b//c/d///e'
splithim=splitme.split('/')
print(splithim)
splitme = 'a/b//c/d///e'
splither=splitme.split('//')
print(splither)
#Get an Item by Using [ offset ]
marxes = ['Groucho', 'Chico', 'Harpo']
mar=marxes[0]#first element
mar1=marxes[1]#second element
mar2=marxes[2]#third element
print(mar, mar1, mar2)

