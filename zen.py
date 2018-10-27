print("Hello World")
import this
print("\n") #Skip a line
#Python basic data types
print("Python basic data types\n")

#Boolean
bool_t = True
bool_f = False

#Number
#float
flt = 0.5
num = 35

string = "Hello world"

#Some data types are either mutable or immutable

#Mutable means that the datatype can be modified or changed
#Murable data type examples
#Lists
l = [True, False, 35, 0.5, "DOG"]
print(l)
print(type(l))
#dictionaries
dic = {"Kelly":"Scooter", "Robert": "Mr. Goggles", "John":"Robert"}
print(dic)
print(type(dic))


#Immutable means the datatype cannot be modified or changed
#Immutable data type examples

#Booleans
bool_t = True
print(bool_t)
print(type(bool_t))
bool_f = False
print(bool_f)
print(type(bool_f))
#Intergers
num = 35
print(num)
print(type(num))
#Floats
flt = 0.5
print(flt)
print(type(flt))
#Tuples
tup = (0,11,22)
print(tup)
print(type(tup))
#Strings
word = "Cat"
print(word)
print(type(word))

#Check datatype
type(bool_t)
