#comment with #
#60 sec/min * 60 min/hr *24hr:day
seconds_per_day=86400
print(seconds_per_day)
print("no comment:quotes make the # harmless")
#continue lines with \
alphabet=''
alphabet+='abcdefg'
alphabet+='hijklmnop'
alphabet+='qrstuv'
alphabet+='wxyz'
print(alphabet)
alphabet='abcdefg'+\
'hijklmnop'+\
'qrstuv'+\
'wxyz'
print(alphabet)
#compare with if,elif and else
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")
furry = True
small = False
if furry:
    if small:
        print("it's a cat.")
    else:
        print("it's a bear!")
else:
    if small:
        print("it's a skink!")
    else:
        print("it's a human")
color="puce"
if color == "red":
    print("it's a tomato")
elif color == "green":
    print("it's a green pepper")
elif color == "bee purple":
    print("i don't know what it is")
else:
    print("I've never heard of the color", color)
