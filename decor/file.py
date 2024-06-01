# ----------------------------------------------------------------------------------------------------------------- #
# with - оператор который автоматом закрывает файл

file = "new.txt"

with open(file, 'w') as f: # Создание и запись
    f.write('Hello world\n')
    
with open(file, "r") as f: # Чтение
    print(f.read())
    
with open(file, "a") as f: # Добавление
    f.write('New Content')