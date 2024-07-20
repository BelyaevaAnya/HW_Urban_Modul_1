# Переменная
a = 15
# названине - переменной; 15 - значение int
b = 30
print(a+b)
# Арифметические операторы
# / - деление
# // - целочисленное деление
# %  - деление с сохранением остатка
# +  - сложение
# -  - вычитание
# *  - умножение
# ** - возведение в степень
# Функция ввода input('Инструкция')
# name = input('Как вас зовут? ')
# print(f'Здравствуйте, {name}!')
# либо
# print('Здравствуйте'+', ',name)
first = 'Вторник'
second = 'Понедельник'
print(f'{second}, {first}')
# Условные операторты
if(a<b):
    print('A<B')
else:
    print('A=>B')

# =>A<B
c = 10
a = 10
b = 10

if  a==b==c:
    print(3)
elif a==b or b==c or b==c:
    print(2)
else:
    print(0)

#a = int(input('Введите 1 число: '))
#b = int(input('Введите 2 число: '))

if a>b:
    print(a)
if b>a:
    print(b)

print(type(b))

# Множества
# Пустой список
a = [1, 2, 3]
a.append('a')
print(a)
print(a[-1])
print(a[0])
print(a[0:3:2])
print(a[::-1])
# Множества - это неизменяемый список с уникальными значениями
mnzh = {1,2,3,4,5,61,111,1,2,3,'a', 'b', False, True}
print(mnzh)
# Оценки и студенты
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a = [1, 2, 3, 4]
print(sum(a)/4)
print(sum(a)/len(a))
# grades_m = sum(grades)
# TypeError: unsupported operand type(s) for +: 'int' and 'list'
# т.к. список в списке
grades_m = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
           sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
           sum(grades[4])/len(grades[4])]
students_sort = sorted(students)

dict_students = {'a': 5, 'b':10}
print(type(dict_students))

dict1 = zip(students_sort, grades_m)
print(dict1)    # =><zip object at 0x000001748C333A80>
dict1 = dict(zip(students_sort, grades_m))
print(dict1)    # =>{'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

print(zipped_list)
# => [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]

# Циклы
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_m = []
students_sort = sorted(students)
for num in grades:
    s = sum(num)/len(num)
    grades_m.append(s)

print(grades_m)

a = 1
b = 20
while a < b:
    a += 1
print(a)    # =>20
