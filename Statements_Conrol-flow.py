#Statements/control flow/itterator

#import (modulename.elementname)
import socket
print(dir(socket))
a = socket.AF_INET
print(help(socket))

#if statement
bool1 = True
if bool1:
    print "True" # >>True
bool2 = False
if bool2:
    print "True" # >>Nothing to print on the screen
if bool2:
    print "True"
else:
    print "False" # >>False

#while Statement
bool1 = True
while (bool1 is True):
    print "True" # >> True (infinite loop)
    break # >> Stop the infinite loop

#functions
def func1():
    print "hello world!"
func1() # >> hello world!

#for (itterator)
list_word = ["this","is","a","list"]
print list_word # >> ["this","is","a","list"]

for word in list_word:
    print word # returns the word from list
    print list_word, # returns the list as much as there are words in it
    print word, # return this is a list

for i in range(101): #range is non-inclusif / 101 isn't computed
    print(i) # this will print numbers from 0 to 100

list_word = ["m","y","a","d"]
for letter in list_word:
    if letter == 'a' :
        print "found a!"

#expressions
# = assign value
# == compare egality
# != compare inegality
# <> greater than , smaller than
