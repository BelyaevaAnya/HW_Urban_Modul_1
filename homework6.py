# Работа со словарем
my_dict = {'Vanya': 2002, 'Alex': 1993, 'Kamila': 1989, 'Olga': 2001}
print(f'Созданный словарь: {my_dict}')
# => {'Vanya': 2002, 'Alex': 1993, 'Kamila': 1989, 'Olga': 2001}
print(f'Существующий ключ: {my_dict.get('Kamila')}')    # => Существующий ключ: 1989
print(f'Отсутствующий ключ: {my_dict.get('Maga')}')     # => Отсутствующий ключ: None
my_dict.update({'Maga': 2001,
                'Igor': 2002})
# print(my_dict)
# =>{'Vanya': 2002, 'Alex': 1993, 'Kamila': 1989, 'Olga': 2001, 'Maga': 2001, 'Igor': 2002}
delete_person = my_dict.pop('Vanya')
print(f'Удаленный человек из словаря c г.р.: {delete_person}')   # => 2002
print(f'Итоговый вид словаря:{my_dict}')
# Работа с множеством
my_set = set([1, 2, 3, 3, 3, True, False, True, 'sss', 'sss', 's1', 1.0, 19.2, 1.0])
print(f'Множество:{my_set}')
# => Множество:{False, 1, 2, 3, 'sss', 19.2, 's1'}
my_set.add("Mode1")
my_set.add(1.2)
my_set.remove(1)
print(f'Модифицированное множество: {my_set}')
# => Модифицированное множество: {False, 2, 3, 'sss', 'Mode1', 1.2, 19.2, 's1'}