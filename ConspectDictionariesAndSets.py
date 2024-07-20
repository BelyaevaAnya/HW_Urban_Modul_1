# Словарь
phone_book = {'Denis': 88005553535, 'Max': 88005554949}     # указываем 'ключ':значение
print(phone_book)   # {'Denis': 88005553535, 'Max': 88005554949}
# Методы для работы со словарями
phone_book['Denis'] = 11513213211
print(phone_book)   # {'Denis': 11513213211, 'Max': 88005554949}
phone_book['Anton'] = 11513213211
print(phone_book)   # {'Denis': 11513213211, 'Max': 88005554949, 'Anton': 11513213211}
del phone_book['Max']
print(phone_book)   # {'Denis': 11513213211, 'Anton': 11513213211}
# Метод update()-необходим для обновления нескольких пар сразу
phone_book.update({'Sasha': 111,
                   'Alex': 122})
print(phone_book)   # {'Denis': 11513213211, 'Anton': 11513213211, 'Sasha': 111, 'Alex': 122}
# Словарь неупорядоченная коллекция
print(phone_book.get('Denis'))  # 11513213211
# Особенность есть: если ключ не будет найден
print(phone_book.get('Kamila'))     # => None
# Метод pop
a = phone_book.pop('Anton')     # вывод значения
print(phone_book)   # {'Denis': 11513213211, 'Sasha': 111, 'Alex': 122}
print(a)
list_ = [1, 2, 3]
list_.pop(0)    # достали из списка элемент с индексом 0
print(list_)
# Метод .keys() получение ключей из коллекции словарика
print(phone_book.keys())    # dict_keys(['Denis', 'Sasha', 'Alex'])
# Метод .values() для получения значений
print(phone_book.values())  # dict_values([11513213211, 111, 122])
# Если нужен и ключ, и значение метод - .items()
print(phone_book.items())   # dict_items([('Denis', 11513213211), ('Sasha', 111), ('Alex', 122)])
# Словарь может включать в себя несколько значений(список)
phone_book = {'Denis': [88005553535, 000], 'Max': 88005554949}
print(phone_book)   # {'Denis': [88005553535, 0], 'Max': 88005554949}
# Пример использования: хранение логина и пароля
# Множества НЕ СОДЕРЖИТ ПОВТОРЯЮЩИЕСЯ ЭЛЕМЕНТЫ
# Хранит в себе только уникальные значения
set_ = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 'ss', True, (1, 2, 3)}
print(set_)         # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, (1, 2, 3), 'ss'}
# Как из листа сделать множество
list_ = [1, 1, 1, 2, 3, 4, 5]
print(set(list_))   # {1, 2, 3, 4, 5}
print(list_[0])     # 1
list_ = set(list_)
print(list_)
# print(list_[0]) TypeError: 'set' object is not subscriptable
# Методы для работы со множествами .discard и .remove
print(list_.discard(1))     # удаление элемента =1 множества
print(list_)
print(list_.remove(5))     # удаление элемента =5 множества
print(list_)
# разница в том, что discard при удалении ненайденного элемента выдаст None, а remove выдаст ошибку
# метод pop применим к множествам
list_1 = [1, 1, 1, 2, 3, 4, 5, 222]
list_1 = set(list_1)
list_1 = list_1.add(5)     # удаление элемента =5 множества
print(list_1)