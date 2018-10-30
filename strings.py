#List of illegal variables
#Cannot start with number
#name 13 = "something"
#Cannot be reserved word
#for= "yes"
#Cannot be special characters
#!omg = "word"
#Cannot have spaces
#my var = "variable"


#String syntax

#Strings can either be enclosed in quotation marks

vari = "Word"

# Or they can be enclosed in apostrophes

var2 = 'word'

#String data type methods and attributes

yelling = "i am yelling"
whispering = "I AM WHISPERING"
book = "the story of john"

print (yelling.upper() , whispering.lower())
print (book.title())

#Multiplying strings

lines = "-" * 50

#String cocatination

sen1 = "I went to the store. "
sen2 = "I bought an apple."

print(sen1 + sen2)
print("{} {}".format(sen1,sen2))

print("\n\t\tSonnet16")
print(lines)

v1 = "Shall I compate thee to a summer's day?"
v2 = "\nThou art more lovely and more temperate."

print (v1 + v2)

#Stripping whitespace
whitespace = "password                                 "
nospace = "password"

#.strip() does both sides
print (whitespace.strip())
#.rstrip() only does the right
print(whitespace.rstrip())
#.lstrip() only does the left
print(whitespace.lstrip())
