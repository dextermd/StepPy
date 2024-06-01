# # Кортежи(Tuple) - Immutable and Organized, Hybrid
# a = (1,2,"True", True, "privet")
# # a[0] = 10
# print(a[-1])
# a.count
# print(a.count(2)) # метод возвращает сколько раз встречается переданный элемент в кортеже
# print(a.index(2)) # метод возвращает первый встречный индекс переданного элемента в кортеже

# print('\n-------------------------------------------------------------------------------\n')

# # синтаксис деструктуризации
# a = ("Biba", "Boba", "Triba")

# one, two, three = a

# print(one)
# print(two)
# print(three)

# print('\n-------------------------------------------------------------------------------\n')

# for i in a:
#     print(i)
    
# print('\n-------------------------------------------------------------------------------\n')

# # Множество (Set) - Mutable, Unorganized, Hybrid, Unique
# # Индекс ключ для каждого элемента и данный ключ рандомно тянет каждый раз при пересоздании множества
# mySet = {32, 41, 4, 14, 14, 21}
# mySet2 = {"Hello", "World", "Python", "Julia"}
# print(mySet)
# print(mySet2)
 
# print('\n-------------------------------------------------------------------------------\n')

# b =[1,1,2,2,3,3,4,4,5,5]
# # b = set(b) # существуют функции для измнения типов данных, у каждого типа своя функция
# b = list(b)
# print(b)


# print('\n-------------------------------------------------------------------------------\n')

# set1 = {1,10,100,"Hello", "Privet","Poka"}
# set2 = {2,20,200,"Hello","Js", "PHP"}

# # set3 = set1 | set2  # | оператор обьединения возвращает новый сет на основеконкотенации двух других
# set3 = set1 & set2 # оператор пересечения возвразает новый сет в котором присудствуют элемменты которые присудствуют в обоих элементах
# print(set3)

# set3 = set1 - set2
# set4 = set2 - set1
# set3 = set1 ^ set2 # jоператор симетричной разницы  (есть там и там)
# print(set3)
# print(set4)

# set3 = set1.union(set2) # метод обьеденения
# set3 = set1.difference(set2) # метод разницы на основе первого
# set3 = set2.difference(set1) # метод разницы на основе второго
# set3 = set1.symmetric_difference(set2) # метод симетричной разницы
# set3 = set1.intersection(set2) # метод пересечения

# print('\n-------------------------------------------------------------------------------\n')

# print(type(set1))
# print(type(set3))

# print('\n-------------------------------------------------------------------------------\n')

c = [1,1,1,1,2,2,3,3,3,4,5]
с = frozenset(c)
print(c)
print(type(c))

# print('\n-------------------------------------------------------------------------------\n')

# set1.add("AAAAAA")
# print(set1)



print('\n-------------------------------------------------------------------------------\n')
# 1) Измените неизменямое. Создайте кортеж из 5 чисел, Добавюьте в него еще два числа (200,100),переверните кортеж

a = (1, 2, 3, 4, 5)
a = a + (200, 100)
a = a[::-1]
print(a)

print('\n-------------------------------------------------------------------------------\n')
# 2) Найдите пересечение,разницу и симетричную разницу двух кортежей
a = (1, 2, 3, 4, 5)
b = (0, 2, 3, 4, 5)

intersection = set(a) & set(b)
print(intersection)
difference = set(a) - set(b)
print(difference)
symmetric_difference = set(a) ^ set(b)
print(symmetric_difference)


print('\n-------------------------------------------------------------------------------\n')
# 3) Создайте функцию которая режет ваш кортеж на n позиции: 1,2,3,4,5 ("2") -> 1,2,3
a = (1, 2, 3, 4, 5)

def d(item, n):
     return item[:n + 1]

a = d(a,2);
print(a)

# 4) Создайте компресии на основе множеств: {1,2,3,5,6,7,10,11,12} -> ['1-3','5-7','10-12']
g = {1, 2, 3, 5, 6, 7, 10, 11, 12}
sort_g = sorted(g)
res = []
start = sort_g[0]
end = sort_g[0]

for num in sort_g[1:]:
    if num == end + 1:
        end = num
    else:
        res.append(f"{start}-{end}")
        start = end = num
        
res.append(f"{start}-{end}")

print(res)

# 5) Создайте функцию которая принимает номер и ищет все его делители сохраняя их frozentset

def find_divisors(num):
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
            
    div = frozenset(div)
    return div

n = 12
div = find_divisors(n)
print(div)
 