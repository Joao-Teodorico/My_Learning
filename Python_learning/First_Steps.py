# =============================================
# My First Python File
# =============================================

#Funcion

#The print command displays the result on the screen
print ("Hello World!")

#Variables  

#INT (Integer): When we talk about integers we are talking about natural numbers
number_1 = 12
number_2 = 23
sume = (number_1 + number_2)
print (sume)

#Float (decimal): And Float is about numbers with a decimal point 
number_3 = 15.3
number_4 = 2.755
sume_2 = (number_3 + number_4)
print (sume_2)

#Str (String): A data type used to represent text, including lettersm numberrs and symblos, enclosed in quotes (" " or ' ')
Name_Student = "Daniel"
print (Name_Student)
print (type(Name_Student))
mARk = (number_3 + number_4)/2


#f"" = formatted string (used to insert variables and expressions into text)
#{} = placeholder where you put variables or calculations inside an f-string

result_1 = f"The Student : {Name_Student} got an {mARk: .2f} of 10"

print (result_1)


#Boolean (Bool): represent logical values (True or False)
Light_ON = True
Light_OFF = False
print(f"{Light_ON} and {Light_OFF}")

Age = 10
print (f"Is the student an adult? {Age >= 18}")