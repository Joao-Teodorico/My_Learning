a = 'AAAAAA'
b = 'B'
c = 1.1
#format_string = 'a={} b={} c={:.2f}'.format(a, b, c)
#format_string = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
format_string = 'a={name1} b={name2} c={name3:.2f}'.format(name1 = a,name2 =  b, name3 =c)
print(format_string)

name = "Diana Prince"
age = 100
format_string= '{n} have {a} years old'
print(format_string.format(n=name, a=age))

name = "Bruce Wayne"
age = 35
format_string= f'{name} have {age:.2f} years old'
print(format_string)