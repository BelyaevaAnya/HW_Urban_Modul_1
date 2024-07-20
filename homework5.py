immutable_var = (1, 2.2, 'string', [0, 1], [0.00, 0.01, 0.001], ['s1', 's2', 's3'])
print(immutable_var,' ', type(immutable_var))       # => (1, 2.2, 'string', [0, 1], [0.0, 0.01, 0.001], ['s1', 's2', 's3'])   <class 'tuple'>.
# кортеж immutable_var содержит элементы разных типов данных, первый(immutable_var[0])из которых
# – неизменяемое целое число (int),
#immutable_var[0] = 2
#TypeError: 'tuple' object does not support item assignment
#объект "кортеж" не поддерживает назначение элементов
# объект float (immutable_var[1]) также неизменяемая по той же причине.
#immutable_var[1] = 2.1
# Строка 'string'(immutable_var[2]) также неизменяемая по той же причине.
#immutable_var[2] = '2.1'
# Сам со себе кортеж неизменяемый, то есть для него нет методов изменения содержимого.
# Но у списков внутри кортежа [0,1](immutable_var[3]),
# [0.00, 0.01, 0.001](immutable_var[4])
# и  ['s1', 's2', 's3'] (immutable_var[5])
# есть такие методы, поэтому их можно изменить.
immutable_var[3][0] = 1
print(immutable_var[3], ' ', type(immutable_var[3]))       # => [1, 1]   <class 'list'>
immutable_var[4][2] += 1.2
print(immutable_var[4], ' ', type(immutable_var[4]))       # => [0.0, 0.01, 1.2009999999999998]   <class 'list'>
immutable_var[5][2] += 'sss123,2'
print(immutable_var[5], ' ', type(immutable_var[5]))       # => ['s1', 's2', 's3sss123,2']   <class 'list'>
print(immutable_var)                                       # => (1, 2.2, 'string', [1, 1], [0.0, 0.01, 1.2009999999999998], ['s1', 's2', 's3sss123,2'])

mutable_list = [0.1, True, 'sss', 1, [0, 1, 2], [0.1, 0.2, 0.3], ['s', 's1', 's2']]
mutable_list[0] *= 111
mutable_list[1] &= False
mutable_list[2] *= 5
mutable_list[3] -= 5
mutable_list[4][0] = 1
mutable_list[5][1] = 2.2
mutable_list[6][2] = '2.2ss'
print(mutable_list)
# => [11.100000000000001, False, 'sssssssssssssss', -4, [1, 1, 2], [0.1, 2.2, 0.3], ['s', 's1', '2.2ss']]


