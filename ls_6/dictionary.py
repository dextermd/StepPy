# Dictionary(dict) - pair key - value, mutablr, organized

s1 = {1}        # set
d1 = dict()     # dict
d2 = {}         # dict
d3 = {          # dict в качестве ключей неизменяемые значения 
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    10: "value4",
    3.13: "value5",
    True: "value6",
    frozenset([1,2,3]): "value7"
}
print(type(s1))
print(type(d1))
print(type(d2))
print(type(d3))

print("\n-------------------------------------------------------\n")

# проход по ключам
for i in d3:
    print(i, d3[i])
    
print("\n-------------------------------------------------------\n")

print(d3.items())

print("\n-------------------------------------------------------\n")

for key, value in d3.items():
    print(key, value)
    
print("\n-------------------------------------------------------\n")

list_values = list(d3.values())
print(list_values)
for value in d3.values():
    print(value)
    
print("\n-------------------------------------------------------\n")

list_keys = list(d3.keys())
print(list_keys)
for key in d3.keys():
    print(key)
    
print("\n-------------------------------------------------------\n")

new_dict = d3.fromkeys([1,2,3]) # формирует новый список на основе
print(new_dict)

print("\n-------------------------------------------------------\n")

d3["NOT EXIST"] = "VALUE"  # добавление пары ключ значение
d3["NOT EXIST"] = "VALUE_EDIT" # обновления значения по клюбчу 
print(d3)

print("\n-------------------------------------------------------\n")

def word_frequency(words: list) -> dict:
    freq = {}
    # 1
    # for word in words:
    #     if word in freq:
    #         freq[word] += 1
    #     else:
    #         freq[word] = 1
    # return freq
    
    #2
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

    
print(word_frequency.__doc__)
print(word_frequency(["apple", "orange", "cherry", "apple", "apple"]))

print("\n-------------------------------------------------------\n")

a = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
print(a.get(1))

print("\n-------------------------------------------------------\n")

def sort_dict_by_key_length(dict: dict) -> dict:
    sorted_dict = {}
    sorted_keys = sorted(dict.keys(), key=len)
    for key in sorted_keys:
        sorted_dict[key] = dict[key]
    return sorted_dict

print(sort_dict_by_key_length({'name': 1, 'b': 2, 'abracadabra': 3, '': 4}))

