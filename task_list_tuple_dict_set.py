#exercice
#list creation
years_list=[1992,1993,1994,1995,1996,1997]
#My third birthday
print("My third birthday was in: ",years_list[3])
#the year I was the oldest
print("I was the oldest in : ",years_list[-1])
#list creation
things=["mozzarella","cinderella","salmonella"]
#upper case cinderella
things[1]=things[1].upper()
print(things)
#upper case mozzarella
things[0]=things[0].upper()
print(things)
#delete salmonella
del things[-1]
print (things)
#create another list
surprise=["Groucho","Chico","Harpo"]
#lower the last word
surprise[-1]=surprise[-1].lower()
#reverse the last word
surprise[-1]=surprise[-1][::-1]
#capitalize the last word
surprise[-1]=surprise[-1].capitalize()
print(surprise)
#make a dictionary
e2f={"dog":"chien","cat":"chat","walrus":"morse"}
print(e2f.get("walrus"))
#make a dictionary
f2e = {v: k for k, v in e2f.items()}
print(f2e)
print(f2e.get("chien"))
#create a set
print(set(e2f))
#multilevel dictionary
cat=['Henri','Grumpy','Lucy']
life={
'animals':{'cats':cat,'octopi':{},'emus':{}},
'plant':{},
'other':{}
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
