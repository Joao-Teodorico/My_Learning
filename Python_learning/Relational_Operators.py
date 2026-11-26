"""
Greater than  4>3
Greater than or equal to 4>=4
less than 3<4
less than or equal to 3<=4
equal to 4==4
not equal to 4!=5

"""
#==============True===============# 
greather_than = 4 > 3
greater_than_or_equal_to = 4 >= 4
less_than = 3 < 4 
equal_to = 4 == 4
not_equal_to = 4 != 5 
print (greather_than)
print (greater_than_or_equal_to)
print (less_than)
print (equal_to)
print (not_equal_to) 

#==============FALSE===============# 
greather_than = 5 > 3
greater_than_or_equal_to = 3 >= 4
less_than = 3 < 2 
equal_to = 4 == 1
not_equal_to = 4 != 5
print (greather_than)
print (greater_than_or_equal_to)
print (less_than)
print (equal_to)
print (not_equal_to) 

#============Exercise===============# 

N1 = int(input("Enter the first number: "))
N2 = int(input("Enter the second number: "))

if N1 > N2:
    print(f"{N1} is greater than {N2}")
else:
    print(f"{N2} is greater than {N1}")
#============Exercise===============# 

N3 = int(input("Enter the first number: "))
N4 = int(input("Enter the second number: "))

if N4 >= N3:
    print("You can go to cinema")
elif N3 == N4:
    print("You can go to cinema with supervisor")
elif  200 < N4:
    print("You are so old to go to cinema")
else:
    print("You can't go to cinema")