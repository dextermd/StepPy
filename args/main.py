import re
from collections import Counter

# def foo(a,b = 0):
#     print(a,b)
    
# foo(1,2)

# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #

# Args - специальный параметр который позволяет принимать неограниченное количество аргументов
# Переданные данные обернутся в кортеж

# def foo(*args):
#     print(args)
#     print(type(args))
    
# foo(1,2,3,4,5,6,7,8,9,0)
# foo(1,2,3)
# foo()
# foo(1)
# foo("privet", "matvei", 24, 43.2)

# ----------------------------------------------------------------------------------------------- #

# def sum_args(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# print(sum_args(1,2,3,4,5,6,7,8,9,0))


# ----------------------------------------------------------------------------------------------- #

# def merge_dicts(*args):
#     result = {}
#     for i in args:
#         result.update(i)
#     return result

# print(merge_dicts({"a": 1}, {"b": 2}, {"c": 3}))


# ----------------------------------------------------------------------------------------------- #

# TODO not finish
# def common_elements(*args):
#     if not args:
#         return []
#     result = set(args[0])
#     for i in args[1:]:
#         result.intersection_update(i)
#     return list(result)

# print(common_elements([1,2,3], [2,1,4], [1,2,6]))


# ----------------------------------------------------------------------------------------------- #

# def check_palindrome(*args):
#     palindromes = []
#     for i in args:
#         if i == i[::-1]:
#             palindromes.append(i)
#     return palindromes

# print(check_palindrome("madam", "grisha", "mihai", "rotor", "radar"))


# ----------------------------------------------------------------------------------------------- #

# def foo(a,b,c):
#     print(a)
#     print(b)
#     print(c)
    
# foo(c = 3, a = 1, b= 2)


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #

# Kwargs - специальный параметр который позволяет принимать неограниченное кол-во ключевых аргументов
# Переданные данные обернутся в словарь

# Ключевые аргементы - передача значений в каждый параметр отдельно контролируя порядок
# передачи синтаксисом схожим с парами ключ-значение

# def kwsrg_test(**kwargs):
#     print(kwargs)
    
# kwsrg_test(a = 1, b = 2, c = 3)

# ----------------------------------------------------------------------------------------------- #

# def keys_checker(dictionary, **kwargs):
#     for key in dictionary:
#         if key in kwargs:
#             return True
#     return False

# print(keys_checker({"a": 1, "b":2, "c": 3}, a = 1, d = 4, e = 6))

# ----------------------------------------------------------------------------------------------- #

# def validate_email_and_password(*args, **kwargs):
#     for i in args:
#         if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", i):
#             print("Email is valid")
#         else:
#             print("Email is not valid")
#     for key, value in kwargs.items():
#         if len(kwargs[i]) >= 6:
#             print("Password is valid")
#         else:
#             print("Password is not valid")
            
# validate_email_and_password("", "")


# ----------------------------------------------------------------------------------------------- #

# 1) функцию которая прнимает любое количество строк и минимальную длинну.
# Верните список строк которые подходят под заданную длинну и regex паттерн на проверку если текст состоит только из букв

# def get_custtom_str(str_len, *args):
#     result = []
#     for i in args:
#         if re.match(r"^[A-Z].*$", i) and len(i) >= str_len:
#             result.append(i)
#     return result

# print(get_custtom_str(5, "Enslaver", "Fan", "Nudite", "stalagmite", "Terzet"))


# 2) напишите функцию которая принимат произвольное количество температур
# в виде ключ значений и может переводить из фаренгейта в цельсий с функционалом переключателся между ними

# def convert_temperature(to_celsius = True, **kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if to_celsius:
#             result[key] = (value - 32) * 5 / 9
#         else:
#             result[key] = (value * 9 / 5) + 32
#     return result


# print(convert_temperature(**{"a": 32, "b": 44, "c": 100}))
# print(convert_temperature(**{"a": 32, "b": 44, "c": 100} , to_celsius=False))


# 3) напишите функцию которая прнимает произвольное количество строк и возращает словари где ключи буквы каждой строки 
# а значения количества повторений,также покажите саммую часто встречаемую букву во всех строках

# def count_letters(*args):
#     all_strings = ''.join(args)
#     letter_counts = Counter(all_strings)
#     most_letter = max(letter_counts, key=letter_counts.get)
#     return most_letter

# most_letter = count_letters("apple", "banana", "orange")
# print("Most Letter:", most_letter)

# 4) напишите функцию которая принимает произвольное количество словарей и считает сред. ариф. всех значений

# def average_of_values(*args):
#     all_values = []
#     for dictionary in args:
#         all_values.extend(dictionary.values())

#     if all_values:
#         average = sum(all_values) / len(all_values)
#         return average


# average = average_of_values({'a': 10, 'b': 20, 'c': 30})
# print("Avg:", average)
