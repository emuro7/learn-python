import this
print("\n")#Skip a line  
#Python basic data types
print("Python basic data types\n")
#Boolean 
bool_t = True
bool_f = False

#Number
#Float
flt = 0.5
#Interger
num = 35


string = "Hello world"


#Some data types are either mutable or immutable

#Mutable means that the datatype can me modified or changed
#Mutable data type examples
#Lists
l = [True, False, 35,0.5, "Dog"]
print(l)
print(type(l)) 
#dictionaries
dic  = {"Kelly":"Scooter", "Robert": "Mr. Giggles", "John":"Robert" }
print(dic)
print(type(dic))

#Immutable means that the datatype can not be modified or changed
#Immutable data type exampes
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
#String
word = "Cat"
print(word)
print(type(word))


#Check data type
type(bool_t)
