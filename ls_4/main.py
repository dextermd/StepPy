# String - Immutable, organized
name = "Unifun"
# name[0] = "W" Ошибка
print(name[0])
print(name)

# Методы
copy = name.upper()
print(copy)

name2 = "unifun,is,the,best,company,in,chisinau"
cap = name2.capitalize()
print(cap)

count_c = name2.count('c')
count_c_params = name2.count('c', 20)
print(count_c)
print(count_c_params)

index = name2.index("c")
print(index)

words = name2.split(',')
print(words)

# case converter


def camel_to_snake_case(str):
    result = [str[0].lower()]
    for char in str[1:]:
        if char.isupper():
            result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    print(''.join(result))


camel_to_snake_case("helloWorldMyNameIsChuck")


# Longest common prefix

def longest_common_prefix(strings: list) -> str:
    if not strings:
        return -1
    prefix = strings[0]
    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    print(prefix)


longest_common_prefix(["flower", "flow", "flight"])


print('_________________________________________________________________')
# 1) создайте функцю которая ищет все возможные палиндромы внутри переданной строки
# abra-cadabra -> ['a','aca','ada,'ara','abba']

cl= "abra-cadabra"
arr = ['a','aca','ada', 'ara','abba']
def find_palindrome(arr: list):
    for i in range(len(arr)):
        if cl.count(arr[i]):
            print(arr[i])


find_palindrome(arr)

print('_________________________________________________________________')

# 2) Найди все анаграммы в группе
# ['eat','tea','ate','tan','bat','nat'] -> [[eat,tea,ate], [tan,bat,nat]]

print('_________________________________________________________________')
# 3) Разворот строки циклом for
word_t = "akva"
def string_back(str):
    return str[::-1]


print(string_back(word_t))

print('_________________________________________________________________')
# 4) Подсчитайте количество глассных и соглассных в строке
name_p = "unifun,is,the,best"

def counts_vowel_consonant(str):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowel_count = 0
    consonant_count = 0
    for c in vowels:
        for cc in str.lower():
            if c is cc:
                vowel_count += 1

    for c in consonants:
        for cc in str.lower():
            if c is cc:
                consonant_count += 1
    print(f"vowel = {vowel_count}\nconsonant = {consonant_count}")


counts_vowel_consonant(name_p)
print('_________________________________________________________________')
# 5) Сокращение строк,создайте функцю которая удаляет глассные в строке и сохраняет каждую первую букву каждого слова
# "hello world" -> "hll wrld"
name_pp = "hello world"
def replace_volves(str):
    vowels = "aeiou"
    for c in vowels:
        str = str.replace(c, '')
    print(str)


replace_volves(name_pp)

print('_________________________________________________________________')

# 6) Подсчитайте количество цифр больше и меньше n в зависимости от выбора пользователя в строке
# custom_count(string,n,True)

str_num = "46, 10, 5, 58, 99, 105, 99, 105, 99, 105, 99, 1, 33"
def custom_count(string, n, is_max: bool = True):
    arr = string.split(',')
    for i in range(len(arr)):
        if is_max:
            if int(arr[i]) > n:
                print(arr[i])
        else:
            if int(arr[i]) < n:
                print(arr[i])


custom_count(str_num, 50, False)


