    #Comments are written using 
    # """ """ are use for multi - line strings 

#=============================================#

#variables 

#the PRINT command displays the result on the screen
print ("Hello world!!")

#INT (Integer): When we talk about integers we are talk about natural numbers
nuMBer_1 = 12 
nuMBer_2 = 22 
sume = (nuMBer_1 + nuMBer_2) 
print (sume)

# Float (decimal): And Float is about numbers with a decimal point
nuMBer_3 = 1.4
nuMBer_4 = 1.6
sume_2 = (nuMBer_3 + nuMBer_4) 
print (sume_2)

# Str (String): A string is a sequence of characters used to represent text
#It can include letters, numbers, symbols, and spaces, and must be written inside quotes(" " or ' ')
Name_Student = "Daniel"
mEAn = (nuMBer_1 + nuMBer_2) / 2 

# f " " = formatted string (used to insert variables and expression into text)
#{} = placeholder where you put variables or calculatons inside an f-string
result_1 = f"The Student : {Name_Student} got an {mEAn: .2f}"

print (result_1)


"""
pi = 3.14

ciRCle = 17

Sume_value = (pi + ciRCle)

meSSage = "The radius value is"

result_2 = meSSage + str(Sume_value)

print (result)
"""

#Boolean (Bool) : Represent logical values (True of False)
Light_ON = True
Light_OFF = False 

print(f"{Light_ON} and {Light_OFF}")

#List : An ordered and mutable collection (can be changed)
nuMBers_list = [1,2,3]

print(f"before: {nuMBers_list}")

# U can Add elements
nuMBers_list.append(4)

print(f"After: {nuMBers_list}")

#Tuple: An ordered but immutable collection (cannot be changed)
nuMBers_tuple = (1,2,3)

print (nuMBers_tuple)

#Set: An unordered collection with no duplicate values
nuMBers_set = {1,23,3,4,23,1,6,8,9} 

print(nuMBers_set) # duplicates are removed automatically

#Dictionary (dict): Stores data in key-value pairs
student = {
"name" : "Daniel",
"Age": 20 
}
print (student)
print (student["Age"]) #access value by key (name or Age)

# None: Represents the absence of a value
result = None

print(result)