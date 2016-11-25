#basic python commands

#Input/output
int_one = int(raw_input("give me a number: "))
print int_one
str_one = raw_input("give me a string: ")
print str_one
type str_one # type string

#print formatting
str1 = "this"
str2 = "string"
print str1 + str2 # >>this string
#str1 = "our number is : "
#str2 = 5
#print str1 + str2
#this will cause error because we can not concatenate a string object with an integer object

#Print Formatting: print "%format" % corresponding_data
str1 = "our number is : %d"
str2 = 5
print str1 %(str2) # >> our number is : 5

str1 = int(raw_input("number : "))
str2 = int(raw_input("number : "))
str3 = int(raw_input("number : "))
print "You entered %d\t%d\t%d" %(str1,str2,str3) # >> You entered ...
