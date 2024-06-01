# Функции высшего порядка => функция которая принимает как параметр другую функцию

# def high_order(fnc, value):
#     return fnc(value)

# def multiply(val):
#     return val * val

# def add(val):
#     return val + val

# def substract(val):
#     return val - val

# print(high_order(multiply, 10))
# print(high_order(add, 10))
# print(high_order(substract, 10))

# ----------------------------------------------------------------------------------- #

# def aggreate(value, *args):
#     return tuple(arg(value)for arg in args)


# def double(x):
#     return x * 2

# def triple(x):
#     return x * 3

# def square(x):
#     return x * x

# print(aggreate(3, double, triple, square))


# ----------------------------------------------------------------------------------- #

# def pipeline(value, *args):
#     for func in args:
#         value = func(value)
#     return value

# def add_one(value):
#     return value + 1

# def add_ten(value):
#     return value + 10

# def add_one_hundred(value):
#     return value + 100

# print(pipeline(5, add_one, add_ten, add_one_hundred))

# ----------------------------------------------------------------------------------- #

# def apply_alternating(values, *args):
#     results = []
#     funcs = [arg for arg in args]
#     for i, value in enumerate(values):
#         results.append(funcs[i](value))
#     return results
    
# def increment(x):
#     return x + 1

# def decrement(x):
#     return x - 1

# def half(x):
#     return x / 2

# print(apply_alternating([1,2,3], increment, decrement, half))

# ----------------------------------------------------------------------------------- #

# 1) Функция высшего порядка которая возращает словарь где ключ порядковый номер,а значение результат исполнения каждого вызова функции с
# неким значением
# 2) Условные Функции: Функция высшего порялка которая проверяет с помощью переданной функции свое условие,если true исполняет другую переданную функцию,
# если false последнюю переданную функцию
# 3) Создайте функцию  высшего порядка которая прнимает некую коллекцию элемент и приминяет для нее некий фильтр который является переданной функцией.Покажите
# результат работы на 4 фильтрах


# 1) Функция высшего порядка которая возращает словарь где ключ порядковый номер,а значение результат исполнения каждого вызова функции с
# неким значением
 
def higher_order_func(func, values):
    result_dict = {}
    for i, value in enumerate(values, 1):
        result_dict[i] = func(value)
    return result_dict
 
def sum(x):
    return x + x
 
values=[15, 25, 11, 44, 18]
print(higher_order_func(sum, values))
 
 
# 2) Условные Функции: Функция высшего порялка которая проверяет с помощью переданной функции свое условие,если true исполняет другую переданную функцию,
# # если false последнюю переданную функцию
 
def condition(condition, true_result, false_result):
    if condition:
        return true_result()
    else:
        return false_result()
   
def is_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False
   
def print_odd():
    print("Number is odd!")
   
def print_even():
    print("Number is even")
   
condition(is_odd(15), print_odd, print_even)
condition(is_odd(16), print_odd, print_even)
       
       
# 3) Создайте функцию  высшего порядка которая прнимает некую коллекцию элемент и приминяет для нее некий фильтр который является переданной функцией.Покажите
# # результат работы на 4 фильтрах
 
def higher_order_filter(my_collection, filter_func):
    return filter(filter_func, my_collection)
 
def is_even(x):
    if not isinstance(x, str):
        return x % 2 == 0
    return False
 
def is_uppercase(s):
    if isinstance(s, str):
        return s.isupper()
    return False
 
def is_positive(x):
    if not isinstance(x, str):
        return x > 0
    return False
 
def is_negative(x):
    if not isinstance(x, str):
        return x < 0
    return False
 
my_collection=[15, 25, 11, 44, -18, "abcdefghijklmnop", "CAPS", "HELLO"]
 
print(list(higher_order_filter(my_collection, is_even)))
print(list(higher_order_filter(my_collection, is_uppercase)))
print(list(higher_order_filter(my_collection, is_positive)))
print(list(higher_order_filter(my_collection, is_negative)))