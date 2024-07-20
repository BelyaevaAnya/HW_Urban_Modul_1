# Для отображения 2 ковычек
print('"Denis"')
# Для отображения 1 ковычек
print("'Denis'")
# Конкатенация строк(+)
name = 'Denis'
print("Hello, "+name)
print("Hello, "+'Denis')
print(("Hello, "+'Denis! ')*5)
name = 'Denis'
print(name[0])  # res: D
print(name[-1]) # res: S
print(name[0:5]) # нач.: конец
print(name[0:3]) # нач.: конец(кон-1(индексация с 0))
print(name[0:3:2])  # 2-шаг вывода
print(name[:3])     # указали только конец(до 3 эл.)
print(name[2:])     # указали только начало(со 2 эл.)
print(name[::-1])   # указали только шаг(-1) (вывод: sineD)
# 41-вопрос о работе со строками Python
# Как проверить два объекта на идентичность?
animals = ['python', 'gopher']
even_more_animals = ['python', 'gopher']
more_animals = animals
print(animals == more_animals)  # => True
print(animals is more_animals)  # => True
print(animals == even_more_animals)     # => True
print(animals is even_more_animals)     # => False
# функция id(), которая возвращает идентификатор адреса памяти
name = 'object'
print(id(name))
# При вызове этой функции (id())для двух идентичных объектов будет выдан один и тот же идентификатор.
# Как проверить то, что каждое слово в строке начинается с заглавной буквы?
# istitle()
print( 'The Hilton'.istitle())      # => True
print( 'The dog'.istitle())         # => False
print( 'sticky rice'.istitle())     # => False
# Как проверить строку на вхождение в неё другой строки? оператор in
print( 'plane' in 'The worlds fastest plane')       # => True
print( 'car' in 'The worlds fastest plane')         #=> False
# Как найти индекс первого вхождения подстроки в строку?Это — find() и index()
# find()
print('The worlds fastest plane'.find('plane'))     # => 19
print('The worlds fastest plane'.find('car'))       # => -1
# index()
print('The worlds fastest plane'.index('plane'))#=> 19
# print('The worlds fastest plane'.index('car') ) #=> ValueError: substring not found
# Как подсчитать количество символов в строке? len()
print(len('The first president of the organization..'))     # => 41
# Как подсчитать то, сколько раз определённый символ встречается в строке? count()
print('The first president of the organization..'.count('o'))       # => 3
# Как сделать первый символ строки заглавной буквой? Метод capitalize()
print('florida dolphins'.capitalize())                  # => 'Florida dolphins'
# Что такое f-строки и как ими пользоваться?
#   Использование f-строк напоминает применение метода format().
#   При объявлении f-строк перед открывающей кавычкой пишется буква f.
name = 'Chris'
food = 'creme brulee'
print(f'Hello. My name is {name} and I like {food}.')
# => 'Hello. My name is Chris and I like creme brulee'
#   Как найти подстроку в заданной части строки? Метод index()
#   Метод index() можно вызывать, передавая ему необязательные аргументы,
#   представляющие индекс начального и конечного фрагмента строки,
# в пределах которых и нужно осуществлять поиск подстроки.
print('the happiest person in the whole wide world.'.index('the',10,44))        # (с ограничением по поиску)=> 23
print('the happiest person in the whole wide world.'.index('the'))                                 # (без ограничения по поиску)=> 0
# Как вставить содержимое переменной в строку, воспользовавшись методом format()?
difficulty = 'easy'
thing = 'exam'
print('That {} was {}!'.format(thing, difficulty))      # => 'That exam was easy!'
# Как узнать о том, что в строке содержатся только цифры? isnumeric()
print('80000'.isnumeric())      # => True
# Используя этот метод, учитывайте то, что знаки препинания он цифрами не считает.
print('1.0'.isnumeric())        # => False
# Как разделить строку по заданному символу? split()
print('This is great'.split(' '))
# => ['This', 'is', 'great']
print('not--so--great'.split('--'))
# => ['not', 'so', 'great']
# Как проверить строку на то, что она составлена только из строчных букв? islower()
print('all lower case'.islower())           # => True
print('not aLL lowercase'.islower())        # False
# Как проверить то, что строка начинается со строчной буквы?islower() для 0 символа
print('aPPLE'[0].islower())                 # => True
# Можно ли в Python прибавить целое число к строке? Нет TypeError
# print('Ten' + 10)#=> TypeError
# Как «перевернуть» строку?
# Для того чтобы «перевернуть» строку:
# 1) её можно разбить,представив в виде списка символов
# 2)«перевернуть» список
# 3) объединив его элементы, сформировать новую строку.
print(''.join(reversed("hello world")))     # => 'dlrow olleh'
# Как объединить список строк в одну строку, элементы которой разделены дефисами? join()
print('-'.join(['a','b','c'])) #=> 'a-b-c'
#Как узнать о том, что все символы строки входят в ASCII? isascii()
print( 'Â'.isascii() ) #=> False
print( 'A'.isascii() ) #=> True
#Как привести всю строку к верхнему или нижнему регистру?
sentence = 'The Cat in the Hat'
print(sentence.lower()) #=> 'the cat in the hat'
print(sentence.upper())#=> 'THE CAT IN THE HAT'
#Как преобразовать первый и последний символы строки к верхнему регистру?
# обращаться к символам строки по индексам
#Строки в Python иммутабельны(неизменяемы после создания объекта),
#поэтому мы будем заниматься сборкой новой строки на основе существующей.
animal = 'fish'
print(animal[0].upper() + animal[1:-1] + animal[-1].upper()) #=>FisH
#Как проверить строку на то, что она составлена только из прописных букв? isupper()
print('Toronto'.isupper()) #=> False
print('TORONTO'.isupper()) #= True
#В какой ситуации вы воспользовались бы методом splitlines()?
#Метод splitlines() разделяет строки по символам разрыва строки.(\n)
sentence = "It was a stormy night\nThe house creeked\nThe wind blew."
print(sentence.splitlines()) #=> ['It was a stormy night', 'The house creeked', 'The wind blew.']
#Как получить срез строки?
string = 'I like to eat apples'
print(string[:6]) #=> 'I like'
print(string[7:13]) #=> 'to eat'
print(string[0:-1:2]) #=> 'Ilk oetape' (каждый 2-й символ)
#Как преобразовать целое число в строку?
print(str(5)) #=> '5'
#Как узнать о том, что строка содержит только алфавитные символы?
print('One1'.isalpha(),'One'.isalpha()) #=> False,True
#Как в заданной строке заменить на что-либо все вхождения некоей подстроки?
sentence = 'Sally sells sea shells by the sea shore'
print(sentence.replace('sea', 'mountain'))
#=> 'Sally sells mountain shells by the mountain shore'
#Как вернуть символ строки с минимальным ASCII-кодом?Функция min()
print(min('strings')) #=> 'g'
#Как проверить строку на то, что в ней содержатся только алфавитно-цифровые символы?
# (isalnum()-method)
print('Ten10'.isalnum()) #=> True
print('Ten10.'.isalnum()) #=> False
# Как удалить пробелы из начала строки (из её левой части), из её конца (из правой части), или с обеих сторон строки?
# методы lstrip(), rstrip() и strip()
string = '  string of whitespace    '
print(string.lstrip()) #=> 'string of whitespace    '
print(string.rstrip()) #=> '  string of whitespace'
print(string.strip()) #=> 'string of whitespace'
#Как проверить то, что строка начинается с заданной последовательности символов,
# или заканчивается заданной последовательностью символов?
# методы startswith() и endswith()
city = 'New York'
print(city.startswith('New')) # => True
print(city.endswith('N')) # => False
# Как закодировать строку в ASCII?
# Метод encode() позволяет кодировать строки с использованием заданной кодировки.
# По умолчанию используется кодировка utf-8. Если некий символ не может быть представлен
# с использованием заданной кодировки, будет выдана ошибка UnicodeEncodeError.
print('Fresh Tuna'.encode('ascii'))
# => b'Fresh Tuna'
# print('Fresh Tuna Â'.encode('ascii'))
# => UnicodeEncodeError: 'ascii' codec can't encode character '\xc2' in position 11: ordinal not in range(128)
# Как узнать о том, что строка включает в себя только пробелы? method isspace()
print(''.isspace(), ' '.isspace(), '   '.isspace(), ' the '.isspace())     # => False,True,True,False
# Что случится, если умножить некую строку на 3?
print('dog' * 3)     # 'dogdogdog'
# Как привести к верхнему регистру первый символ каждого слова в строке? метод title()
print('once upon a time'.title())       # => 'Once Upon A Time'
# Как объединить две строки? Оператор +
print('string one' + ' ' + 'string two')   # => 'string one string two'
# Как пользоваться методом partition()? Метод partition() разбивает строку по заданной подстроке.
# После этого результат возвращается в виде кортежа.
# При этом подстрока, по которой осуществлялась разбивка, тоже входит в кортеж.
# Кортежи в Python — это не меняющиеся структуры сведений,
# применяемые для хранения сгруппированной последовательности.
# Они похожи на списки, но имеют одно важное отличие: их невозможно изменять после разработки.
sentence = "If you want to be a ninja"
print(sentence.partition(' want '))
# => ('If you', ' want ', 'to be a ninja')
#  Строки в Python иммутабельны. Что это значит?
#  говорит о том, что после того, как создан объект строки, он не может быть изменён.
#  При «модификации» строк исходные строки не меняются.
#  Вместо этого в памяти создаются совершенно новые объекты.
#  Доказать это можно, воспользовавшись функцией id().
proverb = 'Rise each day before the sun'
print(id(proverb))
# => 2945227903968
proverb_two = 'Rise each day before the sun' + ' if its a weekday'
print(id(proverb_two))
# => 2945227632784
# При конкатенации (+)'Rise each day before the sun' и ' if its a weekday'
# в памяти создаётся новый объект, имеющий новый идентификатор.
# Если бы исходный объект менялся бы, тогда у объектов был бы один и тот же идентификатор.
# Если объявить одну и ту же строку дважды (записав её в 2 разные переменные)
# — сколько объектов будет создано в памяти? 1 или 2?
animal = 'dog'
pet = 'dog'
# При таком подходе в памяти создаётся лишь один объект.
# Когда я столкнулся с этим в первый раз, мне это не показалось интуитивно понятным.
# Но этот механизм помогает Python экономить память при работе с длинными строками.
# Доказать это можно, прибегнув к функции id().
print(id(animal))
print(id(pet))
# Как пользоваться методами maketrans() и translate()?
# Метод maketrans() позволяет описать отображение одних символов на другие, возвращая таблицу преобразования.
# Метод translate() позволяет применить заданную таблицу для преобразования строки.
# создаём отображение
mapping = str.maketrans("abcs", "123S")
# преобразуем строку
print("abc are the first three letters".translate(mapping))   # => '123 1re the firSt three letterS'
# Обратите внимание на то, что в строке произведена замена символов a, b, c и s,
# соответственно, на символы 1, 2, 3 и S
# Как убрать из строки гласные буквы?
# пользуясь механизмом List Comprehension
# Символы проверяют, сравнивая с кортежем, содержащим гласные буквы
# Если символ не входит в кортеж — он присоединяется к новой строке.
string = 'Hello 1 World 2'
vowels = ('a', 'e', 'i', 'o', 'u')
print(''.join([c for c in string if c not in vowels]))         # => 'Hll 1 Wrld 2'
# В каких ситуациях пользуются методом rfind()?
# Метод rfind() похож на метод find(),
# но он, в отличие от find(), просматривает строку не слева направо, а справа налево
# возвращая индекс первого найденного вхождения искомой подстроки
story = 'The price is right said Bob. The price is right.'
print(story.rfind('is'))         # => 39
