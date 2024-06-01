# Декоратор - замыкание высшего порядка которое изменяет поведение ффункции не затрагивая ее изначальный функционал

# def outer(func):
#     def inner():
#         print('Hello !')
#         func()
#     return inner

# @outer
# def say_hello():
#     print('Hi !')
    
# say_hello()

# ----------------------------------------------------------------------------------------------------------------- #

# def html_decor(func):
#     def wrapper(text):
#         print('<h1>')
#         func(text)
#         print('</h1>')
#     return wrapper
    
    
# @html_decor
# def say_hello(text):
#     print(text)
    
    
# say_hello("Privet")
# say_hello("I Love Python")

# ----------------------------------------------------------------------------------------------------------------- #

# def log_to_file(file_path):
#     def log_decorator(func):
#         def wrapper(*args, **kwargs):
#             with open(file_path, 'a') as f:
#                 f.write(f'Called function {func.__name__} with argumnents: {args}, {kwargs} \n')
#             return func(*args, **kwargs)
#         return wrapper
#     return log_decorator

# @log_to_file("log.txt")
# def say_hello(text):
#     return(text)


# @log_to_file("log.txt")
# def multiply(a, b):
#     return a * b

# print(say_hello('Bounjur'))
# print('--------------------------------')
# print(multiply(10, 2))

# ----------------------------------------------------------------------------------------------------------------- #

"""
1) Декоратор который ограничивает возможность вызова функции переданного количетсва раз
2) Декоратор который отслеживает и выдает сообщения о начале работе функции и конца работе функции
3) Декоратор который прнимиает только позитивные значения.Если переданные значения подходят то они записываются в файл со своим порядковым номером в файле.Подсчитайте количество записей в файл
4) Декоратор который подсчитывает количество вызовов функции.Записывайте в файл название функий и их количество вызовов.Считайте информацию из файла и покажите в виде словаря
5) Декоратор который повторяет вызов функции переданное количество раз

"""
# ----------------------------------------------------------------------------------------------------------------- #
#1) Декоратор который ограничивает возможность вызова функции переданного количетсва раз

# def count_restrict(count):
#     def print_decor(func):
#         cur_count = 0
#         def wrapper(text):
#             nonlocal cur_count
#             if cur_count < count:
#                 cur_count += 1
#                 print(f'---> {func(text)} <---')
#             else: 
#                 print(f"Function {func.__name__} limited.")
#         return wrapper
#     return print_decor


# @count_restrict(5)
# def say_hello(text):
#     return text


# for i in range(7):
#     say_hello(f"Go {i+1}")
    
# ----------------------------------------------------------------------------------------------------------------- #
# 2) Декоратор который отслеживает и выдает сообщения о начале работе функции и конца работе функции


# def print_start_end_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'----- Start {func.__name__}  ------')
#         func(*args, **kwargs)
#         print(f'-----  End {func.__name__} ------')
#     return wrapper


# @print_start_end_decorator
# def say_hello(text):
#     print(text)

# @print_start_end_decorator
# def multiply(a, b):
#     print(a * b)


# say_hello('Bon')
# print('--------------------------------')
# multiply(10, 2)

# ----------------------------------------------------------------------------------------------------------------- #
# 3) Декоратор который прнимиает только позитивные значения.
# Если переданные значения подходят то они записываются в файл со своим порядковым номером в файле.
# Подсчитайте количество записей в файл


# def save_pos_values(file_path):
#     def log_decorator(func):
#         def wrapper(*args, **kwargs):
#             pos_count = 0
#             with open(file_path, 'a') as f:
#                 for num in args:
#                     if num > 0:
#                         pos_count += 1
#                         f.write(f'{pos_count}. {num}\n')
#             result =  func(*args, **kwargs)
#             print(f'Количество положительных записей: {pos_count}')
#             return result
#         return wrapper
#     return log_decorator


# @save_pos_values("pos.txt")
# def numbers(*args):
#     return args


# numbers(10, -10, 2, -1, 3)

# ----------------------------------------------------------------------------------------------------------------- #
# 4) Декоратор который подсчитывает количество вызовов функции.
# Записывайте в файл название функий и их количество вызовов.
# Считайте информацию из файла и покажите в виде словаря


# import os

# def log_count_calls():
#     def print_decor(func):
#         cur_count = 0
#         def wrapper(*args, **kwargs):
#             nonlocal cur_count
#             cur_count += 1
#             result = func(*args, **kwargs)
#             file_name = f'{func.__name__}.txt'
#             call_counts = {}
            
#             if os.path.exists(file_name):
#                 with open(file_name, 'r') as f:
#                     for line in f:
#                         name, count = line.strip().split(', count = ')
#                         call_counts[name] = int(count)
            
#             call_counts[func.__name__] = cur_count
            
#             with open(file_name, 'w') as f:
#                 for name, count in call_counts.items():
#                     f.write(f'{name}, count = {count}\n')
            
#             print(call_counts)
            
#             return result
#         return wrapper
#     return print_decor


# @log_count_calls()
# def say_hello(text):
#     return text


# for i in range(7):
#     say_hello(f"Go")

# ----------------------------------------------------------------------------------------------------------------- #
# 5) Декоратор который повторяет вызов функции переданное количество раз