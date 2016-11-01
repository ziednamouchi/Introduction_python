#data
#a function that takes a python Unicode character, looks up its name, 
#and looks up the character again from the name (it should match the original character)
def unicode_test(value):
 import unicodedata
 name = unicodedata.name(value)
 value2 = unicodedata.lookup(name)
 print('value="%s", name="%s", value2="%s"' % (value, name, value2))
unicode_test('\u2603')
#unicodedata.lookup('DOLLAR SIGN')
#encode and decode with utf-8
snowman = '\u2603'
print(len(snowman))#print length of encoding
ds = snowman.encode('utf-8')#utf-8 encoding
print(len(ds))#3 byte encoding
print(ds)
#ds = snowman.encode('ascii')
#ascii encoding (generate an error; snowman is not a valid ascii character)
print(snowman.encode('ascii','ignore'))#ignore encoding exeptions
print(snowman.encode('ascii', 'replace'))#replace unknown char with ?
#Use 'backslashreplace' to produce a Python Unicode character string, like unicode-escape
print(snowman.encode('ascii', 'backslashreplace'))
#character entity strings that you can use in web pages
print(snowman.encode('ascii', 'xmlcharrefreplace'))
#decoding
place= 'caf\u00e9'
print(place)
print(type(place))
#Encode place in UTF-8 format in a bytes variable called place_bytes
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
#decode that byte string back to a Unicode string
place2 = place_bytes.decode('utf-8')
print(place2)#This worked because we encoded to UTF-8 and decoded from UTF-8
#place3 = place_bytes.decode('ascii')
#doesn't woek the encoder is different from the decoder
#The ASCII decoder threw an exception because the byte value 0xc3 is illegal in ASCII
place4 = place_bytes.decode('latin-1')
place5 = place_bytes.decode('windows-1252')
#The moral of this story: whenever possible, use UTF-8 encoding.
#It works, is supported everywhere, can express every Unicode character, and is quickly decoded and encoded
