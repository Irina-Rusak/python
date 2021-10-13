"""
Практическое задание к уроку 2
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

user_number = 100
user_string = 'Hello'
user_list = [1, 2, 3, 4, 5, 6]
user_list_in_list = [[1, 2, 3], [4, 5, 6]]
user_tuple = (1, 2, 3, 4, 5, 6)
user_set = set('abc')
user_dict = {1: 'a', 2: 'b', 3: 'c'}

print(f' user_number is {type(user_number)}')
print(f' user_string is {type(user_string)}')
print(f' user_list is {type(user_list)}')
print(f' user_list_in_list is {type(user_list_in_list)}')
print(f' user_tuple is {type(user_tuple)}')
print(f' user_set is {type(user_set)}')
print(f' user_dict is {type(user_dict)}')

"""
2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""

count_element = True
while count_element:
    count_element = input('Введите количество элементов списка (целое положительное число): ')
    if count_element.isdigit() and int(count_element) > 0 and int(count_element) % 1 == 0:
        count_element = int(count_element)
        break
    else:
        count_element = True
        print(f'Необходимо ввести целое положительное число!')

user_list = []

i = 1
while i <= count_element:
    user_list.append(input(f'Введите {i}й элемент списка: '))
    i += 1
print(f'Первоначальный список: {user_list}')

i = 0
while i < count_element - 1:
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i = i + 2
print(f'Измененный список {user_list}')

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""

user_month = True
while user_month:
    user_month = input('Введите номер месяца от 1 до 12: ')
    if user_month.isdigit() and 1 <= int(user_month) <= 12 and int(user_month) % 1 == 0:
        user_month = int(user_month)
        break
    else:
        user_month = True
        print(f'Необходимо ввести целое положительное число от 1 до 12!')

# Вариант 1 - через словарь
season_dict = {(12, 1, 2): 'зима',
               (3, 4, 5): 'весна',
               (6, 7, 8): 'лето',
               (9, 10, 11): 'осень'
               }

for key, value in season_dict.items():
    if user_month in key:
        print(f'Пора года (через словарь) - {value}')

# Вариант 2 - через лист
season_list = ['зима', 'весна', 'лето', 'осень']
element = 0
if 1 <= user_month <= 2 or user_month == 12:
    element = 0
elif 3 <= user_month <= 5:
    element = 1
elif 6 <= user_month <= 8:
    element = 2
elif 9 <= user_month <= 11:
    element = 3
else:
    print('Пора года не найдена')
print(f'Пора года (через лист) - {season_list[element]}')

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""

user_string = input('Введите строку из нескольких слов, разделенных пробелами: ')
user_list = user_string.split(' ')

for ind, element in enumerate(user_list):
    print(ind + 1, element[:10])

"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

user_list = [7, 5, 3, 3, 2]

new_element = True
while new_element:
    new_element = input('Введите новый элемент рейтинга (целое число): ')
    if new_element.isdigit():
        new_element = int(new_element)
        break
    else:
        new_element = True
        print(f'Необходимо ввести целое число!')

user_list.append(new_element)
user_list.sort(reverse=True)
print(f'Рейтинг: {user_list}')

"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами,
то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
"""

print('-------------- Каталог товаров --------------')
catalog_product = []
count_product = 0
choice = True

while choice:
    print(f'Товар {count_product + 1}')
    name_product = input('Введите наименование товара: ')
    price_product = input('Введите стоимость товара: ')
    count_items = input('Введите количество единиц товара: ')
    unit_product = input('Введите единицу измерения товара: ')
    product = {'название': name_product,
               'цена': price_product,
               'количество': count_items,
               'единица измерения': unit_product}
    catalog_product.append(product)
    choice = input('Хотите добавить еще один товар? Если да - введите yes: ')
    if choice == 'yes':
        choice = True
        count_product += 1
    else:
        break

catalog_product_list = []

for ind, element in enumerate(catalog_product):
    item_product = ind + 1, element
    catalog_product_list.append(tuple(item_product))

print('-------------- Каталог товаров --------------')

for element in catalog_product_list:
    print(element)

"""
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""

names_product = []
prices_product = []
counts_items = []
units_product = []

for element in catalog_product_list:
    names_product.append(element[1]['название'])
    prices_product.append(element[1]['цена'])
    counts_items.append(element[1]['количество'])
    units_product.append(element[1]['единица измерения'])

print('-------------- Аналитика о товарах --------------')

statistic_product = {
    'название': list(set(names_product)),
    'цена': list(set(prices_product)),
    'количество': list(set(counts_items)),
    'единица измерения': list(set(units_product))
}

print(statistic_product)
