name = "Urban"
print(name, type(name))     # => Urban <class 'str'>
name = 5
print(name, type(name))     # => 5 <class 'int'>
name = 5.5
print(name, type(name))     # => 5.5 <class 'float'>
name = [1, 2]
print(name, type(name))     # => [1, 2] <class 'list'>
age = 30
new_age = '30'
#print(age+new_age)         TypeError: unsupported operand type(s) for +: 'int' and 'str'