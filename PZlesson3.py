"""
Практическое задание к уроку 3:
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(*args):
    try:
        result = float(args[0]) / float(args[1])
    except ZeroDivisionError:
        result = 'Деление на ноль!'
    except Exception as e:
        result = f'Ошибка: {e}'
    return result


a = input('Введите число a: ')
b = input('Введите число b: ')

print(division(a, b))

"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def person(**kwargs):
    result = ''
    for key, value in kwargs.items():
        result += f'{key}: {value} '
    return result


print(person(name='Irina', surname='Rusak', birthday='04.02.1993', region='Minsk', email='irina@gmail.com',
             mobile=375441234567))

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    try:
        elements = list(args)
        max_1 = max(elements)
        elements.remove(max_1)
        max_2 = max(elements)
        result = float(max_1) + float(max_2)
    except Exception as e:
        result = f'Ошибка: {e}'
    return result


print(my_func(10, 25.5, 25.5))

"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_v1(x, y):
    try:
        result = x ** y
    except Exception as e:
        result = f'Ошибка: {e}'
    return result


def my_func_v2(x, y):
    try:
        result = x
        for i in range(-y - 1):
            result = result * x
        result = 1 / result
    except Exception as e:
        result = f'Ошибка: {e}'
    return result


print(my_func_v1(25, -2))
print(my_func_v2(25, -2))

"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

result = 0
while True:
    user_list = input('Введите строку чисел, разделенных пробелами: ')
    elements = user_list.split()
    try:
        for element in elements:
            result += float(element)
        print(f'Сумма всех элементов = {result}.')
    except:
        print(f'Сумма всех элементов = {result}.\nКонец программы (введено не число).')
        break

"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(user_string):
    result = ''
    for element in user_string.split():
        result += f'{element.capitalize()} '
    return result


print(int_func('rusak irina stanislavovna'))
