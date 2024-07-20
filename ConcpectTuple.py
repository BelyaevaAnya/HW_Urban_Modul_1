# Кортежи
# Особенности: неизменяемость, упорядоченность, тип элементов внутри кортежа может быть разный
tuple_ = 1, 2, 3, 4, True, "string"
print(tuple_)
# кортеж - не изменяемая последовательность
tuple_2 = (1, 2, 3, 4)
print(tuple_2)
tuple_3 = tuple([1, 2, 3, 4])
print(tuple_3)
print(type(tuple_), type(tuple_2), type(tuple_3))
print(tuple_3[0])
# tuple_3[0] = 21 TypeError: 'tuple' object does not support item assignment
# Хранилище списка без изменений
# В памяти занимает меньше места чем список
list = [1, 2, 3, 4, True, "string"]
tuple_ = 1, 2, 3, 4, True, "string"
print(tuple_.__sizeof__())
print(list.__sizeof__())
# Может хранить внутри себя изменяемые объекты
tuple_ = ([1, 2], 3, 4, True, "string")
print(tuple_)
tuple_[0][0] = 2
print(tuple_)
# Конкатенация строк(+) поддерживается(сложение кортежей)
tuple_ = tuple_ + tuple_2
print(tuple_)
tuple_ *= 3
print(tuple_)


