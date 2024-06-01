# Переменные и типы данных
# int,float,str,bool

# Синтаксис для создания переменных
# name = value

# age = 24
# height = 189.3
# name = "Pavel"
# is_married = True

# print(age, height, name, is_married)
# print(f"Age is: {age},\nHeight is: {height},\nName is: {name},\nIs married: {is_married}\n")

# Взаимодействие типов данных
# print(1 + "1") # int + str -> error
# print(3 * "str") # повторять строку n кол-во раз

# /  -> Всегда дает дробную часть
# // -> Оператор целочисленного деления
# print(f"10 / 5: {10 / 5}")
# print(f"10 // 5: {10 // 5}")
# print(f"10 / 6: {10 / 6}")
# print(f"10 // 6: {10 // 6}")
# print(10 % 7) # остаток от деления
# print(3 ** 4) # возведение в степень
# print(4 ** 2) # возведение в степень

# Ввод пользователя
# number =  input("Please enter a number: ")
# print(int(number) + 10)

# name = input("Tel mee ur name so could wish u something: ")
# age = input("Tel me ur age so i could u make u with one year older: ")
# print(f"Dear {name} today u r turning {int(age) + 1}. Congrats!")

# Логические операторы и условия
# Операторы сравнения == != >= <=
# (&&) and -> Возвращает  True если слева и справа также True
# (||) or -> Возвращает True если хоть один операнд также True
# (!) not -> Логическое "не", разворачивает значение наоборот
# fast = True
# beautiful = False
# print(fast and beautiful)
# print(not fast)

# В Python важна табуляция так как она и разделяет вложенности
# if 10 > 2:
#     print(True)
# else:
#     print(False)

# примеры
# car_type = "Civil"
# speed = int(input("Enter the speed of the car: "))

# if car_type == "Police" and (speed > 100 or speed < 100):
#     print("Police can do everything")
# elif car_type != "Police" and speed > 100:
#     print(f"{car_type} car is not allowed to drive like this")
# else:
#     print(f"{car_type} car is allowed to drive slow")


# match (switch case)
# number = int(input("Enter number: "))
# match number:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case _:
#         print("default")

import math
# math.sqrt()
# 1) Создайте калькулятор квадратного урованения

# cof_one = float(input("Input cof one: "))
# cof_two = float(input("Input cof two: "))
# cof_three = float(input("Input cof three: ")) 

# res = (cof_two**2) - (4*cof_one*cof_three)

# root_one = (-cof_two + math.sqrt(res)) / (2*cof_one)
# root_two = (-cof_two - math.sqrt(res)) / (2*cof_one)

# print("Root 1:", root_one)
# print("Root 2:", root_two)

# 2) Создайте калькулятор который принимает оператор и операнды от пользователя на все виды операции

# number_one = float(input("Input number one: "))
# operator = input("Input operator: ")
# number_two = float(input("Input number two: "))

# match operator:
#     case "/":
#         print(number_one / number_two)
#     case "+":
#         print(number_one + number_two)
#     case "-":
#         print(number_one - number_two)
#     case "*":
#         print(number_one * number_two)

# 3) Создайте конвертор температуры

# far = float(input("Input temperature in far: "))
# cels = (far - 32) / 1.8
# print(f"{far} Фаренгейт = {cels:} Цельсий ")

# cel = float(input("Enter a cel: "))
# result = cel * 9/5 + 32
# print(result)

# 4) Создайте face-control функционал который проверяет все возможные случаи для прохода человека на рок-концерт
# 5) Создайте функционал который проверяет все возможные случаи для прохода вождение машины 