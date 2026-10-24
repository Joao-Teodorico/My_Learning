#Converts '1' to the integer 1.
print(int('1'), type(int('1'))) 

#Converts '1' to 1.0 and adds 1, resulting in 2.0.
print(float('1') + 1) 

#Returns True because any non-empty string is truthy.      
print(bool(' '))   
print(bool(''))   

#Calculanting BMI
name = 'Hal Jordan'
high = 1.78
weight = 80
bmi = weight / (high ** 2)
print(f'BMI of {name} is {bmi:.2f}')